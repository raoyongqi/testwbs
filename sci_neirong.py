from bs4 import BeautifulSoup
# from translator import google_translate_long_text

# 原始 HTML 代码
html = '''
<span cdxanalyticsevent="" cdxanalyticsaction="Search" cdxanalyticscategory="wos-recordCard_ExpandAbstract" class="abstract-size ng-star-inserted" style="max-height:50px" id="rec2AbstractPart0" lang="en"><p>ABS T R A C T Hybrid quantum and classical classification algorithms have provided a new solution to the classification problem with machine learning methods under a hybrid computing environment. Enlightened by the potential powerful quantum computing and the benefits of <mark>convolutional</mark> <mark>neural</mark> network, a quantum analog of the <mark>convolutional</mark> kernel of the classical <mark>convolutional</mark> <mark>neural</mark> network, i.e</p></span>
'''

soup = BeautifulSoup(html, 'lxml')

span_tag = soup.find('span')

content_p_tag = span_tag.find('p')

title_marks = content_p_tag.find_all('mark')

p_text = content_p_tag.get_text()


print(p_text)


# font_wrapper = soup.new_tag('font', **{
#     'class': 'notranslate immersive-translate-target-wrapper',
#     'data-immersive-translate-translation-element-mark': '1',
#     'lang': 'zh-CN'
# })

# br_tag = soup.new_tag('br')
# font_wrapper.append(br_tag)

# font_translation_wrapper = soup.new_tag('font', **{
#     'class': 'notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper',
#     'data-immersive-translate-translation-element-mark': '1'
# })
# font_wrapper.append(font_translation_wrapper)

# font_inner = soup.new_tag('font', **{
#     'class': 'notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner',
#     'data-immersive-translate-translation-element-mark': '1'
# })
# font_translation_wrapper.append(font_inner)

# # 步骤5：在最内层的 <font> 标签内插入中文翻译内容
# chinese_translation = google_translate_long_text(p_text)
# font_inner.append(chinese_translation)

# content_p_tag.append(font_wrapper)

# span_tag['style'] = 'max-height:50px'

# span_tag['data-immersive-translate-walked'] = '6486b4bb-16ed-40ff-86fa-b7e1ab33e2a7'

# modified_html =soup.prettify()

# with open("formatted_html.html", "w", encoding="utf-8") as file:
#     file.write(modified_html)

# print("HTML 已保存为 formatted_html.html")
