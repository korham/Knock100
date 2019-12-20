# 37. 頻度上位10語

# 出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．

import os
from collections import Counter
from operator import itemgetter
from matplotlib import pyplot as plt
from mecabAnalysys import MecabAnalysys

if __name__ == "__main__":
    src = os.path.join(os.path.dirname(__file__), r"../Output/Chapter4/neko.txt.mecab")
    with open(src, encoding="utf-8") as f:
        ma = MecabAnalysys("\n".join(f.readlines()))
    ma.load()
    morph = ma.get_all_morphemes()

    # 頻度上位10件抽出
    words = ["{} {} {}".format(m["base"], m["pos"], m["pos1"]) for m in morph]
    counter = Counter(words).most_common(10)
    x = [word[0] for word in counter]
    y = [word[1] for word in counter]

    # グラフ描画
    plt.rcParams["font.family"] = "IPAexGothic"
    fig = plt.figure(figsize=(12,5))
    ax = fig.add_subplot()
    ax.barh(x, y)
    ax.set_title("最頻出10語")
    ax.set_xlabel("出現頻度")
    ax.set_ylabel("単語")
    ax.invert_yaxis()
    plt.show()
