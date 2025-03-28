from bs4 import BeautifulSoup
from bs4.element import Tag  # 用于类型检查

# 读取本地 HTML 文件
with open('merged/ConvolutionalNeuralNetworks_1-10.html', 'r', encoding='utf-8') as file:
    html = file.read()

# 创建 BeautifulSoup 对象
soup = BeautifulSoup(html, 'lxml')

# 查找第一个 <app-jcr-sidenav> 元素
first_app_jcr_sidenav = soup.find('app-jcr-sidenav')

# 如果找到了 <app-jcr-sidenav> 元素
if first_app_jcr_sidenav:
    # 使用 find_all 获取所有 <span> 标签
    all_spans = first_app_jcr_sidenav.find_all('span')
    
    # 过滤出没有 class 和 style 属性的 <span> 标签
    first_span_no_class_style = next(
        (span for span in all_spans if isinstance(span, Tag) and not span.has_attr('class') and not span.has_attr('style')),
        None
    )
    
    # 输出第一个没有 class 和 style 属性的 <span> 标签
    if first_span_no_class_style:
        print("Found <span> without class and style attributes:")
        print(type(first_span_no_class_style.parent))  # 打印出直接父元素
        # 查找该 <span> 标签的父元素 <a> 标签
        parent_a = first_span_no_class_style.find_parent('a')
        
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

            font_inner.string = "test journey"

            font_wrapper.append(font_inner)

            first_span_no_class_style.append(font_wrapper)


        else:
            print("No parent <a> tag found.")
    else:
        print("No <span> without class and style attributes found.")
else:
    print("No <app-jcr-sidenav> element found.")


modified_html =soup.prettify()
# 保存格式化后的 HTML 到文件
with open("formatted_html.html", "w", encoding="utf-8") as file:
    file.write(modified_html)

print("HTML 已保存为 formatted_html.html")
