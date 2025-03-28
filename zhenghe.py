from bs4 import BeautifulSoup

# 原始 HTML
html = """
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
"""

# 翻译后的文本（模拟翻译结果）
translated_html = """
<a class="title title-link font-size-18 ng-star-inserted" data-pendo="data-pendo-Summary-record-title" data-ta="summary-record-title-link" href="https://webofscience.clarivate.cn/wos/alldb/full-record/WOS:001319955900001" data-immersive-translate-walked="6486b4bb-16ed-40ff-86fa-b7e1ab33e2a7" data-immersive-translate-paragraph="1">A short report on ADHD detection using <mark data-immersive-translate-walked="6486b4bb-16ed-40ff-86fa-b7e1ab33e2a7">convolutional</mark> <mark data-immersive-translate-walked="6486b4bb-16ed-40ff-86fa-b7e1ab33e2a7">neural</mark> <mark data-immersive-translate-walked="6486b4bb-16ed-40ff-86fa-b7e1ab33e2a7">networks</mark><font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-CN"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">使用 ADHD 检测的简短报告<mark data-immersive-translate-walked="6486b4bb-16ed-40ff-86fa-b7e1ab33e2a7">卷积</mark><mark data-immersive-translate-walked="6486b4bb-16ed-40ff-86fa-b7e1ab33e2a7">神经</mark><mark data-immersive-translate-walked="6486b4bb-16ed-40ff-86fa-b7e1ab33e2a7">网络</mark></font></font></font></a>
"""

# 解析原始 HTML
soup = BeautifulSoup(html, 'html.parser')

# 修改 HTML，添加翻译的属性
def add_translation_attributes(soup):

    # 添加翻译的 <font> 标签
    font_tag = soup.new_tag('font', 
                            class_='notranslate immersive-translate-target-wrapper',
                            lang='zh-CN')
    font_tag.string = '使用 ADHD 检测的简短报告'

    # 替换内容为翻译后的文本
    a_tag = soup.find('a')
    if a_tag:
        a_tag.append(font_tag)

    return soup

# 添加翻译后的属性并打印结果
translated_soup = add_translation_attributes(soup)
print(translated_soup.prettify())
