import time
from bs4 import BeautifulSoup

start_time = time.time()

with open('merged/ConvolutionalNeuralNetworks_41-50.html', 'r', encoding='utf-8') as file:
    html = file.read()

soup = BeautifulSoup(html, 'lxml')

app_records = soup.find_all('app-record')

for app_record in app_records:
    iter_start_time = time.time()

    first_content_span = app_record.find('span', attrs={'cdxanalyticsaction': 'Search', 'id': True, 'cdxanalyticscategory': True, 'lang': True})
    
    if first_content_span:
    
        parent = first_content_span.find_parent()

        grandparent = parent.find_parent() if parent else None

        if grandparent:
    
            if 'style' in grandparent.attrs:
    
                grandparent['style'] += ' height:auto!important'
            else:
    
                grandparent['style'] = 'height:auto!important'

        content_p_tag = first_content_span.find('p')

        if content_p_tag:
            content_p_text = content_p_tag.get_text()
            print(content_p_text)

            font_wrapper = soup.new_tag('font', **{
                'class': 'notranslate immersive-translate-target-wrapper',
                'data-immersive-translate-translation-element-mark': '1',
                'lang': 'zh-CN'
            })

            br_tag = soup.new_tag('br')
            font_wrapper.append(br_tag)

            font_translation_wrapper = soup.new_tag('font', **{
                'class': 'notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper',
                'data-immersive-translate-translation-element-mark': '1'
            })
            font_wrapper.append(font_translation_wrapper)

            font_inner = soup.new_tag('font', **{
                'class': 'notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner',
                'data-immersive-translate-translation-element-mark': '1'
            })
            font_translation_wrapper.append(font_inner)

            chinese_translation = 'test content 测试内容'
            font_inner.append(chinese_translation)

            content_p_tag.append(font_wrapper)

        first_content_span['style'] = 'max-height:50px'
        first_content_span['data-immersive-translate-walked'] = '6486b4bb-16ed-40ff-86fa-b7e1ab33e2a7'



    iter_end_time = time.time()
    iter_duration = iter_end_time - iter_start_time
    print(f"Time taken for this app-record: {iter_duration:.4f} seconds")

end_time = time.time()


selectors_to_remove = [
    {'method': 'find_all', 'args': {'class_': '_pendo-step-container-size'}},
    {'method': 'select', 'args': {'selector': '[aria-label="Open Resource Center, 19 new notifications"]'}}
]

for selector in selectors_to_remove:
    method = getattr(soup, selector['method'])
    elements_to_remove = method(**selector['args'])


    for element in elements_to_remove:
        element.decompose()


total_duration = end_time - start_time
print(f"Total time taken for processing all app-records: {total_duration:.4f} seconds")

modified_html = soup.prettify()

with open("formatted_html.html", "w", encoding="utf-8") as file:
    file.write(modified_html)

print("HTML 已保存为 formatted_html.html")
