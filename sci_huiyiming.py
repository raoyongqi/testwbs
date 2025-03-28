from bs4 import BeautifulSoup

# 原始HTML代码
html = '''
<span class="ng-star-inserted" name="conf_title">16th EAI International Conference on Security and Privacy in Communication Networks (SecureComm)</span>
'''

# 创建BeautifulSoup对象
soup = BeautifulSoup(html, "lxml")

# 找到 <span> 标签
span_tag = soup.find('span')

# 提取文本
text = span_tag.get_text()

font_wrapper = soup.new_tag('font', **{
    'class': 'notranslate immersive-translate-target-wrapper',
    'data-immersive-translate-translation-element-mark': '1',
    'lang': 'zh-CN'
})

# 添加换行标签
br_tag = soup.new_tag('br')
font_wrapper.append(br_tag)

# 创建第二层的 <font> 标签
font_translation_wrapper = soup.new_tag('font', **{
    'class': 'notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper',
    'data-immersive-translate-translation-element-mark': '1'
})
font_wrapper.append(font_translation_wrapper)

# 创建第三层的 <font> 标签
font_inner = soup.new_tag('font', **{
    'class': 'notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner',
    'data-immersive-translate-translation-element-mark': '1'
})
font_translation_wrapper.append(font_inner)

# 中文翻译
chinese_translation = "第 16 届 EAI 通信网络安全与隐私国际会议 (SecureComm)"
font_inner.string = chinese_translation

# 将新的翻译结构插入到原 <span> 标签之后，保留原始内容
span_tag.insert_after(font_wrapper)  # 将翻译结构插入在原标签之后

# 输出最终结果
print(soup.prettify())
