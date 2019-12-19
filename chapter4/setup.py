# 夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をMeCabを使って形態素解析し，
# その結果をneko.txt.mecabというファイルに保存

import os
import MeCab

mecab = MeCab.Tagger()
path = os.path.join(os.path.dirname(__file__), r"../DataSource/neko.txt")
output = os.path.join(os.path.dirname(__file__), r"../Output/Chapter4/neko.txt.mecab")

with open(path, encoding="utf-8") as f, open(output, encoding="utf-8", mode="w") as o:
    length = len(f.readlines())
    f.seek(0)
    for i,r in enumerate(f):
        result = mecab.parse(r)
        o.write(result)
        print(i+1, length)

