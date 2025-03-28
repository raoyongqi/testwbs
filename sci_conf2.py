from bs4 import BeautifulSoup

# 原始HTML
original_html = '''<span _ngcontent-evj-c284="" class="summary-source-title noLink ng-star-inserted" lang="en">SECURITY AND PRIVACY IN COMMUNICATION NETWORKS (SECURECOMM 2020), PT I</span>'''

# 创建BeautifulSoup对象
soup = BeautifulSoup(original_html, 'lxml')

# 找到 <span> 元素
span_tag = soup.find('span', class_='summary-source-title noLink ng-star-inserted')

# 修改 lang 属性
span_tag['lang'] = 'en'
span_tag['data-immersive-translate-walked'] = '6486b4bb-16ed-40ff-86fa-b7e1ab33e2a7'
span_tag['data-immersive-translate-paragraph'] = '1'

# 创建 <font> 标签来包裹翻译后的文本
font_tag = soup.new_tag('font', class_='notranslate immersive-translate-target-wrapper', lang='zh-CN')
font_tag.string = '通信网络中的安全与隐私（SECURECOMM 2020），PT I'

# 将 <font> 标签加入到 <span> 标签中
span_tag.append(font_tag)

# 打印修改后的HTML
print(soup.prettify())
