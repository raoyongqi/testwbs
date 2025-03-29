from bs4 import BeautifulSoup

# 读取本地 HTML 文件
with open('test_webofsci/ConvolutionalNeuralNetworks_1.html', 'r', encoding='utf-8') as file:
    html = file.read()

soup = BeautifulSoup(html, 'lxml')
app_records = soup.find_all('app-record')

for app_record in app_records:


    title_tag = app_record.find('app-summary-title')

    title_a_tag = title_tag.find('a')

    title_marks = title_a_tag.find_all('mark')


    title_old_text = ''.join(mark.get_text() for mark in title_marks)

    title_new_text = ' '.join(mark.get_text() for mark in title_marks)

    list(map(lambda mark: mark.unwrap(), title_marks))

    title_a_tag.string = title_a_tag.text.replace(title_old_text, title_new_text)

    title_a_text = title_a_tag.get_text(strip=True)


    title_a_tag['data-immersive-translate-paragraph'] = '1'

    title_a_tag['data-immersive-translate-walked'] = '6486b4bb-16ed-40ff-86fa-b7e1ab33e2a7'


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

    font_inner_inner_tag.string = title_a_text

    font_tag.append(font_inner_tag)

    font_inner_tag.append(font_inner_inner_tag)

    title_a_tag.append(font_tag)

modified_html = soup.prettify()

with open("formatted_html.html", "w", encoding="utf-8") as file:

    file.write(modified_html)

print("HTML 已保存为 formatted_html.html")

