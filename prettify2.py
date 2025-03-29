from bs4 import BeautifulSoup

# 原始 HTML
html_content = '''
<a class="title title-link font-size-18 ng-star-inserted" 
   data-pendo="data-pendo-Summary-record-title" 
   data-ta="summary-record-title-link" 
   href="https://webofscience.clarivate.cn/wos/alldb/full-record/WOS:001319955900001">
    A short report on ADHD detection using 
    <mark>convolutional</mark> 
    <mark>neural</mark> 
    <mark>networks</mark>
</a>
'''

# 解析 HTML
soup = BeautifulSoup(html_content, 'html.parser')

# 获取 <a> 标签
a_tag = soup.find('a')

# 提取 <mark> 标签内容并去掉 <mark> 标签
for mark in a_tag.find_all('mark'):
    mark.unwrap()  # 去掉 <mark> 标签，保留内容

# 输出修改后的 HTML
print(str(soup))
modified_html = soup.prettify()

# 保存格式化后的 HTML 到文件
with open("formatted_html.html", "w", encoding="utf-8") as file:
    file.write(modified_html)

print("HTML 已保存为 formatted_html.html")
