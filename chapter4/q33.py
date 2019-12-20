# 33. サ変名詞

# サ変接続の名詞をすべて抽出せよ．

import os
from mecabAnalysys import MecabAnalysys

if __name__ == "__main__":
    src = os.path.join(os.path.dirname(__file__), r"../Output/Chapter4/neko.txt.mecab")
    with open(src, encoding="utf-8") as f:
        ma = MecabAnalysys("\n".join(f.readlines()))
    ma.load()

    morph = ma.get_all_morphemes()
    sahen = list(filter(lambda x: x["pos"] == "名詞" and x["pos1"] == "サ変接続", morph))
    disp = [v["surface"] for v in sahen]

    output = os.path.join(os.path.dirname(__file__), r"../Output/Chapter4/q33.txt")
    with open(output, mode="w", encoding="utf-8") as f:
        f.write("\n".join(disp))