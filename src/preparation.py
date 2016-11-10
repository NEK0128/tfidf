# -*- coding:utf-8 -*-
import MeCab
import csv

# setting
class_num = 0
word_classes = [u'名詞', u'動詞', u'形容詞', u'副詞', u'助詞', u'助動詞']
word_class = word_classes[class_num]
input_file_path = "../data/precaution_code_utf8.csv"
row_num = 2


def extract_keywords(line):
    """
    指定した品詞のみ抽出する関数.
    @param  line:  1行の文字列
    @return keywords_list: 指定した品詞を抽出したリスト
    """
    tagger = MeCab.Tagger('-Ochasen')
    node = tagger.parseToNode(line)
    keywords_list = []
    while node:
        if node.feature.split(",")[0] == word_class:
            keywords_list.append(node.surface)
        node = node.next
    return keywords_list


def main():
    csv_reader = csv.reader(open(input_file_path, "r"), delimiter=",", quotechar='"')
    for row in csv_reader:
        keywords = extract_keywords(row[row_num])
        keyword_str = map(str, keywords)
        print(" ".join(keyword_str))

if __name__ == "__main__":
    main()
