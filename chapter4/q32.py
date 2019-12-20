# 32. 動詞の原形

# 動詞の原形をすべて抽出せよ．

import os
from mecabAnalysys import MecabAnalysys

if __name__ == "__main__":
    src = os.path.join(os.path.dirname(__file__), r"../Output/Chapter4/neko.txt.mecab")
    with open(src, encoding="utf-8") as f:
        ma = MecabAnalysys("\n".join(f.readlines()))
    ma.load()

    morph = ma.get_all_morphemes()
    verbs = list(filter(lambda x: x["pos"] == "動詞", morph))
    disp = [v["base"] for v in verbs]

    output = os.path.join(os.path.dirname(__file__), r"../Output/Chapter4/q32.txt")
    with open(output, mode="w", encoding="utf-8") as f:
        f.write("\n".join(disp))