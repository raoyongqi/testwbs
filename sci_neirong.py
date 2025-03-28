from bs4 import BeautifulSoup
from translate import google_translate_long_text

# 原始 HTML 代码
html = '''
<span cdxanalyticsaction="Search" cdxanalyticscategory="wos-recordCard_ExpandAbstract" cdxanalyticsevent="" class="abstract-size ng-star-inserted" id="rec502AbstractPart0" lang="en" style="max-height:100px">
  <p>Understanding road conditions is essential for implementing effective road safety measures and driving solutions. Road situations encompass the day-to-day conditions of roads, including the presence of vehicles and pedestrians. Surveillance cameras strategically placed along streets have been instrumental in monitoring road situations and providing valuable information on pedestrians, moving ve</p>
</span>
'''

soup = BeautifulSoup(html, 'lxml')

span_tag = soup.find('span')

p_tag = span_tag.find('p')

p_text = p_tag.get_text()



font_wrapper = soup.new_tag('font', **{
    'class': 'notranslate immersive-translate-target-wrapper',
    'data-immersive-translate-translation-element-mark': '1',
    'lang': 'zh-CN'
})

br_tag = soup.new_tag('br')
font_wrapper.append(br_tag)

font_translation_wrapper = soup.new_tag('font', **{
    'class': 'notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper',
    'data-immersive-translate-translation-element-mark': '1'
})
font_wrapper.append(font_translation_wrapper)

font_inner = soup.new_tag('font', **{
    'class': 'notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner',
    'data-immersive-translate-translation-element-mark': '1'
})
font_translation_wrapper.append(font_inner)

# 步骤5：在最内层的 <font> 标签内插入中文翻译内容
chinese_translation = google_translate_long_text(p_text)
font_inner.append(chinese_translation)

# 将新创建的中文翻译内容插入到 <p> 标签的末尾
p_tag.append(font_wrapper)

span_tag['style'] = 'max-height:50px'

span_tag['data-immersive-translate-walked'] = '6486b4bb-16ed-40ff-86fa-b7e1ab33e2a7'

modified_html =soup.prettify()

with open("formatted_html.html", "w", encoding="utf-8") as file:
    file.write(modified_html)

print("HTML 已保存为 formatted_html.html")
