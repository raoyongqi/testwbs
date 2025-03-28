from bs4 import BeautifulSoup

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

# 处理 <a> 标签，添加 'data-immersive-translate-*' 属性
a_tag = soup.find('a')
a_tag['data-immersive-translate-paragraph'] = '1'
a_tag['data-immersive-translate-walked'] = '6486b4bb-16ed-40ff-86fa-b7e1ab33e2a7'

# 处理 <mark> 标签，添加 'data-immersive-translate-walked' 属性
for mark_tag in soup.find_all('mark'):
    mark_tag['data-immersive-translate-walked'] = '6486b4bb-16ed-40ff-86fa-b7e1ab33e2a7'

# 添加 <font> 标签及其属性
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
font_inner_inner_tag.string = '使用 ADHD 检测的简短报告'

# 在翻译部分中加入 <mark> 标签并设置属性
for word in ['卷积', '神经', '网络']:
    mark_tag = soup.new_tag('mark', **{
        'data-immersive-translate-walked': '6486b4bb-16ed-40ff-86fa-b7e1ab33e2a7'
    })
    mark_tag.string = word
    font_inner_inner_tag.append(mark_tag)

# 将所有部分拼接
font_tag.append(font_inner_tag)
font_inner_tag.append(font_inner_inner_tag)

# 将 <font> 标签插入到 <a> 标签中
a_tag.append(font_tag)

# 获取修改后的 HTML
modified_html = soup.prettify()

# 保存格式化后的 HTML 到文件
with open("formatted_html.html", "w", encoding="utf-8") as file:
    file.write(modified_html)

print("HTML 已保存为 formatted_html.html")
