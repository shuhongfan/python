"""
@Time ： 2021/11/16 15:32
@Auth ： 021321752215舒洪凡
@File ：25.py
@IDE ：PyCharm
"""

import re
import collections
def analyze_text(text):
    paragraphs = re.split("\n\n", text)  #2个换行为段落标记
    paragraph_count = len(paragraphs)
    print("段落数：{0}".format(paragraph_count))
    lines = re.split("\n", text) #1个换行为行标记
    line_count = len(lines)
    print("行数：{0}".format(line_count))
    sentences = re.split("[.?!]", text) #标点为句标记
    sentence_count = len(sentences)
    print("句数：{0}".format(sentence_count))
    words = re.split(r"\W+", text)
    word_count = len(words)
    print("单词数：{0}".format(word_count))
    freqs = collections.Counter(words)
    print("频率最高的10个单词：")
    for (w, n) in freqs.most_common(10):
        print("{0:10}:{1:10}".format(w, n))


if __name__ == "__main__":
    filename = "D:\Develop\demo.txt"   #文件有汉字，用utf-8编码打开
    try:
        with open(filename,'r', encoding='utf-8') as f:
            text = f.read()
            analyze_text(text.strip())
    except:
        print(filename,' 不存在')
