from bs4 import BeautifulSoup
from bs4.element import Tag  # 用于类型检查

# 读取本地 HTML 文件
with open('merged/ConvolutionalNeuralNetworks_1-10.html', 'r', encoding='utf-8') as file:
    html = file.read()

soup = BeautifulSoup(html, 'lxml')

app_jcr_sidenav_list = soup.find_all('app-jcr-sidenav')

for app_jcr_sidenav in app_jcr_sidenav_list:

    all_spans = app_jcr_sidenav.find_all('span')
    
    # 过滤出没有 class 和 style 属性的 <span> 标签
    journey_span = next(
        (span for span in all_spans if isinstance(span, Tag) and not span.has_attr('class') and not span.has_attr('style')),
        None
    )
    
    # 输出第一个没有 class 和 style 属性的 <span> 标签
    if journey_span:
        print("Found <span> without class and style attributes:")
        print(type(journey_span.parent))  # 打印出直接父元素
        # 查找该 <span> 标签的父元素 <a> 标签
        parent_a = journey_span.find_parent('a')
        
        if parent_a:
            print(type(parent_a))  # 打印出直接父元素

            font_wrapper = soup.new_tag('font', **{
                    'class': 'notranslate immersive-translate-target-wrapper',
                    'data-immersive-translate-translation-element-mark': '1',
                    'lang': 'zh-CN'
                })
            font_inner = soup.new_tag('font', **{
                'class': 'notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner',
                'data-immersive-translate-translation-element-mark': '1'
            })

            font_inner.string = "test journey 测试内容"

            font_wrapper.append(font_inner)

            journey_span.append(font_wrapper)
        else:
            print("No parent <a> tag found.")
    else:
        print("No <span> without class and style attributes found.")

# 保存格式化后的 HTML 到文件
modified_html = soup.prettify()

with open("formatted_html.html", "w", encoding="utf-8") as file:
    file.write(modified_html)

print("HTML 已保存为 formatted_html.html")
