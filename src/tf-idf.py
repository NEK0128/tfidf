#!/usr/bin/env python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import Normalizer
import csv

input_file_docs = ""
column_num = 0
input_file_docs_mecab = ""
output_file = ""
threshold = 0.5


def tfidf(docs):
    '''
    tfidf
    :param docs 文章のリスト:
    :return features vectorの値
            terms vectorの対象の単語
    '''
    vectorizer = TfidfVectorizer(min_df=1, max_df=50, token_pattern=u'(?u)\\b\\w+\\b')
    features = vectorizer.fit_transform(docs)
    terms = vectorizer.get_feature_names()

    return features, terms


def cosine_similarity(v1, v2):
    """
    ベクトルv1, v2のcos類似度の算出
    """
    return sum([a * b for a, b in zip(v1, v2)]) / (
    sum(map(lambda x: x * x, v1)) ** 0.5 * sum(map(lambda x: x * x, v2)) ** 0.5)


if __name__ == '__main__':

    csv_reader = csv.reader(open(input_file_docs, "r"), delimiter=",", quotechar='"')
    lines = []
    for row in csv_reader:
        lines.append(row[column_num])

    f = open(input_file_docs_mecab)
    lines_mecab = f.readlines()
    f.close()

    docs = []

    for line in lines_mecab:
        docs.append(line)

    [features, terms] = tfidf(docs)

    targets = features.toarray()
    objects = features.toarray()

    f = open(output_file, 'w')
    csvWriter = csv.writer(f)

    i = 0
    for target in targets:
        j = 0
        for object in objects:
            similarity = cosine_similarity(target, object)
            listData = []
            if similarity > threshold:
                listData.append(lines[i])
                listData.append(lines[j])
                listData.append(str(similarity))
                csvWriter.writerow(listData)

            j += 1

        i += 1

    f.close()
