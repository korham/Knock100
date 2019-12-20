# 36. 単語の出現頻度

# 文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．

import os
from collections import Counter
from operator import itemgetter
from mecabAnalysys import MecabAnalysys

if __name__ == "__main__":
    src = os.path.join(os.path.dirname(__file__), r"../Output/Chapter4/neko.txt.mecab")
    with open(src, encoding="utf-8") as f:
        ma = MecabAnalysys("\n".join(f.readlines()))
    ma.load()
    morph = ma.get_all_morphemes()

    words = ["{}\t{}\t{}".format(m["base"], m["pos"], m["pos1"]) for m in morph]
    counter = Counter(words)
    ordered = sorted(counter.items(), key=itemgetter(1), reverse=True)

    output = os.path.join(os.path.dirname(__file__), r"../Output/Chapter4/q36.txt")
    with open(output, mode="w", encoding="utf-8") as f:
        for word in ordered:
            f.write(word[0] + ": " + str(word[1]) + "\n")