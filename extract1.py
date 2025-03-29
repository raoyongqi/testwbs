from bs4 import BeautifulSoup
from translator import google_translate_long_text
# 原始 HTML 内容
html_content = '''
<h3 class="ng-star-inserted" lang="en">
    <a class="title title-link font-size-18 ng-star-inserted" 
       data-pendo="data-pendo-Summary-record-title" 
       data-ta="summary-record-title-link" 
       href="https://webofscience.clarivate.cn/wos/alldb/full-record/WOS:001319955900001">
        A short report on ADHD detection using 
        <mark>convolutional</mark> 
        <mark>neural</mark> 
        <mark>networks</mark>
    </a>
</h3>
'''

# 解析 HTML
soup = BeautifulSoup(html_content, 'html.parser')

# 提取 <a> 标签中的文本，排除 <mark> 标签
a_tag = soup.find('a')


mark_texts = [mark.get_text() for mark in a_tag.find_all('mark')]


for mark_tag in a_tag.find_all('mark'):
    
    mark_tag.decompose()

text = a_tag.get_text(strip=True)





soup = BeautifulSoup(html_content, 'html.parser')

a_tag = soup.find('a')
a_tag['data-immersive-translate-paragraph'] = '1'
a_tag['data-immersive-translate-walked'] = '6486b4bb-16ed-40ff-86fa-b7e1ab33e2a7'


for mark_tag in soup.find_all('mark'):
    mark_tag['data-immersive-translate-walked'] = '6486b4bb-16ed-40ff-86fa-b7e1ab33e2a7'

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

font_inner_inner_tag.string =  google_translate_long_text(text)

for word in mark_texts:
    
    mark_tag = soup.new_tag('mark', **{
        'data-immersive-translate-walked': '6486b4bb-16ed-40ff-86fa-b7e1ab33e2a7'
    })
    
    mark_tag.string =  google_translate_long_text(word)
    
    font_inner_inner_tag.append(mark_tag)

font_tag.append(font_inner_tag)

font_inner_tag.append(font_inner_inner_tag)

a_tag.append(font_tag)

modified_html = soup.prettify()

with open("formatted_html.html", "w", encoding="utf-8") as file:

    file.write(modified_html)

print("HTML 已保存为 formatted_html.html")
