from bs4 import BeautifulSoup

# HTML 内容
html_content = '''
<app-summary-title>
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
</app-summary-title>
'''

# 解析 HTML
soup = BeautifulSoup(html_content, 'html.parser')

# 获取文本信息（去掉 <mark> 标签的文本）
title = soup.find('a').get_text()

# 输出结果
print(title)
