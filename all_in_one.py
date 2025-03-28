from bs4 import BeautifulSoup

# 读取本地 HTML 文件
with open('merged/ConvolutionalNeuralNetworks_1-10.html', 'r', encoding='utf-8') as file:
    html = file.read()

soup = BeautifulSoup(html, 'lxml')

first_app_record = soup.find('app-record')

title_tag = first_app_record.find('app-summary-title')

title_a_tag = title_tag.find('a')

title_mark_texts = [mark.get_text() for mark in title_a_tag.find_all('mark')]

text = title_a_tag.get_text(strip=True)



title_a_tag['data-immersive-translate-paragraph'] = '1'

title_a_tag['data-immersive-translate-walked'] = '6486b4bb-16ed-40ff-86fa-b7e1ab33e2a7'


# 添加翻译部分的 <font> 标签
font_tag = soup.new_tag('font', **{
    'class': 'notranslate immersive-translate-target-wrapper',
    'data-immersive-translate-translation-element-mark': '1',
    'lang': 'zh-CN'
})


font_inner_tag = soup.new_tag('font', **{
    'class': 'notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper',
    'data-immersive-translate-translation-element-mark': '1'
})
font_inner_inner_tag = soup.new_tag('font', **{
    'class': 'notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner',
    'data-immersive-translate-translation-element-mark': '1'
})
font_inner_inner_tag.string = 'test_title'

font_tag.append(font_inner_tag)

font_inner_tag.append(font_inner_inner_tag)

for word in title_mark_texts:
    mark_tag = soup.new_tag('mark', **{
        'data-immersive-translate-walked': '6486b4bb-16ed-40ff-86fa-b7e1ab33e2a7'
    })
    mark_tag.string = word
    font_inner_inner_tag.append(mark_tag)
    
title_a_tag.append(font_tag)

modified_html = soup.prettify()

with open("formatted_html.html", "w", encoding="utf-8") as file:

    file.write(modified_html)

print("HTML 已保存为 formatted_html.html")

