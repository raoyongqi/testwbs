import asyncio
from bs4 import BeautifulSoup, Tag
import os
import re
import time

# 模拟翻译函数，直接返回传入的文本（或者你可以按照需求修改这个函数）
async def google_translate_long_text_async(text: str, target_language: str = "zh-CN") -> str:
    # 这里直接返回传入的文本作为"翻译后的文本"，你可以模拟翻译结果
    return text  # 直接返回原文本

translation_cache = {}

async def translate_with_cache(text: str, target_language: str = "zh-CN") -> str:
    # 使用缓存来存储已翻译的文本
    if text not in translation_cache:
        translation_cache[text] = await google_translate_long_text_async(text, target_language)
    return translation_cache[text]

# 保持现有创建 font 标签的函数
def create_font_tag(soup, content, lang="zh-CN"):
    font_tag = soup.new_tag('font', **{
        'class': 'notranslate immersive-translate-target-wrapper',
        'data-immersive-translate-translation-element-mark': '1',
        'lang': lang
    })
    font_inner_tag = soup.new_tag('font', **{
        'class': 'notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner',
        'data-immersive-translate-translation-element-mark': '1'
    })
    font_inner_tag.string = content
    font_tag.append(font_inner_tag)
    return font_tag

# 批量处理应用记录
async def process_app_records_batch(soup, app_records, start_time):
    text_blocks = []
    text_targets = []

    for app_record in app_records:
        title_tag = app_record.find('app-summary-title')
        if title_tag:
            title_a_tag = title_tag.find('a')
            if title_a_tag:
                title_marks = title_a_tag.find_all('mark')
                title_old_text = ''.join(mark.get_text() for mark in title_marks)

                title_new_text = ' '.join(mark.get_text() for mark in title_marks)
                list(map(lambda mark: mark.unwrap(), title_marks))

                title_a_tag.string = title_a_tag.text.replace(title_old_text, title_new_text)

                title_a_text = title_a_tag.get_text(strip=True)
                text_blocks.append(title_a_text)
                text_targets.append(('title', title_a_tag))


        app_jcr_sidenav = app_record.find('app-jcr-sidenav')
        
        if app_jcr_sidenav:
            journey_span = next(
                (span for span in app_jcr_sidenav.find_all('span') if isinstance(span, Tag) and not span.has_attr('class') and not span.has_attr('style')),
                None
            )
            if journey_span:
                journey_text = journey_span.get_text()
                text_blocks.append(journey_text)
                text_targets.append(('journey', journey_span))

        conf_span = app_record.find('span', attrs={'name': 'conf_title'})
        if conf_span:

            conf_text = conf_span.get_text()
            text_blocks.append(conf_text)
            text_targets.append(('conf', conf_span))

        second_conf_span = app_record.find('span', class_='summary-source-title noLink ng-star-inserted')
        if second_conf_span:

            second_conf_text = second_conf_span.get_text()
            text_blocks.append(second_conf_text)
            text_targets.append(('second_conf', second_conf_span))

        content_span = app_record.find('span', attrs={'cdxanalyticsaction': 'Search', 'id': True, 'cdxanalyticscategory': True, 'lang': True})
        if content_span:

            parent = content_span.find_parent()
            
            grandparent = parent.find_parent() if parent else None
            
            if grandparent:
                
                grandparent['style'] = grandparent.get('style', '') + ' height:auto!important'

            content_p_tag = content_span.find('p')
        
            if content_p_tag:
                
                content_marks = content_p_tag.find_all('mark')

                content_p_old_text = ''.join(mark.get_text() for mark in content_marks)

                content_p_new_text = ' '.join(mark.get_text() for mark in content_marks)


                list(map(lambda mark: mark.unwrap(), content_marks))

                content_p_tag.string = content_p_tag.text.replace(content_p_old_text, content_p_new_text)

                content_p_text = content_p_tag.get_text(strip=True)

                text_blocks.append(content_p_text)
                
                text_targets.append(('content', content_p_tag, content_span))

    batch_text = "\n".join(text_blocks)
    translated_batch = await translate_with_cache(batch_text, "zh-CN")
    translated_texts = translated_batch.split("\n")

    for info, translated in zip(text_targets, translated_texts):
        
        if info[0] == 'title':
            font_tag = create_font_tag(soup, translated)
            info[1].append(font_tag)
            info[1]['data-immersive-translate-paragraph'] = '1'
            info[1]['data-immersive-translate-walked'] = '6486b4bb-16ed-40ff-86fa-b7e1ab33e2a7'
        elif info[0] == 'journey':
            font_tag = create_font_tag(soup, translated)
            info[1].append(font_tag)
        elif info[0] in ('conf', 'second_conf'):
            font_tag = create_font_tag(soup, translated)
            info[1].insert_after(font_tag)
        elif info[0] == 'content':
            font_tag = create_font_tag(soup, translated)
            info[1].append(font_tag)
            info[2]['style'] = 'max-height:50px'
            info[2]['data-immersive-translate-walked'] = '6486b4bb-16ed-40ff-86fa-b7e1ab33e2a7'

    print(f"\n✅ 已完成回填 {len(app_records)} 个 app-record")

# 文件排序
def sort_files_by_number(files):
    return sorted(files, key=lambda x: [int(i) if i.isdigit() else i.lower() for i in re.split('(\d+)', x)])

# 主函数
if __name__ == "__main__":
    input_file_path = "test_webofsci/ConvolutionalNeuralNetworks_1.html"
    


    with open(input_file_path, 'r', encoding='utf-8') as file:
        html = file.read()

    soup = BeautifulSoup(html, 'lxml')
    app_records = soup.find_all('app-record')

    start_time = time.time()
    asyncio.run(process_app_records_batch(soup, app_records, start_time))

    # 清理多余元素
    selectors_to_remove = [
        {'method': 'find_all', 'args': {'class_': '_pendo-step-container-size'}},
        {'method': 'select', 'args': {'selector': '[aria-label="Open Resource Center, 19 new notifications"]'}},
        {'method': 'select', 'args': {'selector': '[class="show-more show-more-text wos-new-primary-color"]'}}
    ]

    for selector in selectors_to_remove:
        method = getattr(soup, selector['method'])
        elements_to_remove = method(**selector['args'])
        for element in elements_to_remove:
            element.decompose()

    modified_html = soup.prettify()

    with open("formatted_html.html", "w", encoding="utf-8") as file:

        file.write(modified_html)

    print("HTML 已保存为 formatted_html.html")

    print("HTML 已保存为 formatted_html.html")
    print(f"⏱️ 执行时间: {time.time() - start_time:.2f} 秒")
