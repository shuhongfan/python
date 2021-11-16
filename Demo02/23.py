"""
@Time ： 2021/11/16 14:56
@Auth ： 021321752215舒洪凡
@File ：23.py
@IDE ：PyCharm
"""

from docx import Document
from docx.shared import RGBColor

boldText = []
redText = []
#打开Word文件，遍历所有段落
doc = Document('D:\\Develop\\demo.docx')
for p in doc.paragraphs:
    for r in p.runs:
        #加粗字体
        if r.bold:
            boldText.append(r.text)
        #红色字体
        if r.font.color.rgb == RGBColor(255,0,0):
            redText.append(r.text)

result = {'red text': redText,
           'bold text': boldText,
           'both': set(redText) & set(boldText)}

# 输出结果
for title in result.keys():
    print(title.center(30, '='))
    for text in result[title]:
        print(text)
