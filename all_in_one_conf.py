from bs4 import BeautifulSoup

with open('merged/ConvolutionalNeuralNetworks_41-50.html', 'r', encoding='utf-8') as file:
    html = file.read()

soup = BeautifulSoup(html, 'lxml')

app_records = soup.find_all('app-record')

for app_record in app_records:

    first_conf_span = app_record.find('span', attrs={'name': "conf_title"})

    if first_conf_span:

        first_conf_text = first_conf_span.get_text()

        
        font_wrapper = soup.new_tag('font', **{
            'class': 'notranslate immersive-translate-target-wrapper',
            'data-immersive-translate-translation-element-mark': '1',
            'lang': 'zh-CN'
        })

        # 添加换行标签
        br_tag = soup.new_tag('br')
        font_wrapper.append(br_tag)

        # 创建第二层的 <font> 标签
        font_translation_wrapper = soup.new_tag('font', **{
            'class': 'notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper',
            'data-immersive-translate-translation-element-mark': '1'
        })
        font_wrapper.append(font_translation_wrapper)

        # 创建第三层的 <font> 标签
        font_inner = soup.new_tag('font', **{
            'class': 'notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner',
            'data-immersive-translate-translation-element-mark': '1'
        })
        font_translation_wrapper.append(font_inner)

        chinese_conf = "test conf 测试会议"

        font_inner.string = chinese_conf
        
        first_conf_span.insert_after(font_wrapper)  # 将翻译结构插入在原标签之后

    second_conf_span = app_record.find('span', class_='summary-source-title noLink ng-star-inserted')

    if second_conf_span:

        second_conf_text = second_conf_span.get_text()

        
        font_wrapper = soup.new_tag('font', **{
            'class': 'notranslate immersive-translate-target-wrapper',
            'data-immersive-translate-translation-element-mark': '1',
            'lang': 'zh-CN'
        })

        # 添加换行标签
        br_tag = soup.new_tag('br')
        font_wrapper.append(br_tag)

        # 创建第二层的 <font> 标签
        font_translation_wrapper = soup.new_tag('font', **{
            'class': 'notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper',
            'data-immersive-translate-translation-element-mark': '1'
        })
        font_wrapper.append(font_translation_wrapper)

        # 创建第三层的 <font> 标签
        font_inner = soup.new_tag('font', **{
            'class': 'notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner',
            'data-immersive-translate-translation-element-mark': '1'
        })
        font_translation_wrapper.append(font_inner)

        chinese_conf2 = "test conf 测试会议2"

        font_inner.string = chinese_conf2
        
        second_conf_span.insert_after(font_wrapper)  # 将翻译结构插入在原标签之后



modified_html = soup.prettify()

with open("formatted_html.html", "w", encoding="utf-8") as file:
    file.write(modified_html)

print("HTML 已保存为 formatted_html.html")
