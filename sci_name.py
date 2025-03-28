from bs4 import BeautifulSoup
from translate import google_translate_long_text

# 原始HTML代码
html = '''
<a _ngcontent-evj-c284="" aria-haspopup="menu" cdxanalyticsaction="Search" cdxanalyticscategory="wos-recordCard_Journal_Info" cdxanalyticsevent="" class="mat-menu-trigger font-size-14 summary-source-title-link source-title-link remove-space no-left-padding section-label-data identifiers-link ng-star-inserted" color="primary" data-ta="jcr-link-menu" lang="en" tabindex="0">
  <span _ngcontent-evj-c284="">FRONTIERS IN PSYCHIATRY</span>
  <mat-icon _ngcontent-evj-c284="" aria-hidden="true" class="mat-icon notranslate font-size-26 icon-position material-icons mat-ligature-font mat-icon-inline mat-icon-no-color" data-mat-icon-type="font" inline="true" role="img">arrow_drop_down</mat-icon>
</a>
'''

# 创建BeautifulSoup对象
soup = BeautifulSoup(html, 'lxml')

# 找到span标签，并将其内容替换为英文和中文
span = soup.find('span')
span.string = span.get_text()  # 保证英文内容不变

# 添加中文翻译
font_wrapper = soup.new_tag('font', **{
    'class': 'notranslate immersive-translate-target-wrapper',
    'data-immersive-translate-translation-element-mark': '1',
    'lang': 'zh-CN'
})

# 创建一个嵌套的font标签
font_inner = soup.new_tag('font', **{
    'class': 'notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner',
    'data-immersive-translate-translation-element-mark': '1'
})
font_inner.string = google_translate_long_text(span.string)

font_wrapper.append(font_inner)

# 将中文翻译插入到span标签中
span.append(font_wrapper)

modified_html =soup.prettify()
# 保存格式化后的 HTML 到文件
with open("formatted_html.html", "w", encoding="utf-8") as file:
    file.write(modified_html)

print("HTML 已保存为 formatted_html.html")
