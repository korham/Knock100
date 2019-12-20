# 34. 「AのB」

# 2つの名詞が「の」で連結されている名詞句を抽出せよ．

import os
from mecabAnalysys import MecabAnalysys

if __name__ == "__main__":
    src = os.path.join(os.path.dirname(__file__), r"../Output/Chapter4/neko.txt.mecab")
    with open(src, encoding="utf-8") as f:
        ma = MecabAnalysys("\n".join(f.readlines()))
    ma.load()

    morph = ma.get_all_morphemes()
    noun_phrases = []
    for i,m in enumerate(morph):
        if m["pos"] == "名詞" and i+1 <= (len(morph)-2):
            if morph[i+1]["surface"] == "の" and morph[i+2]["pos"] == "名詞":
                noun_phrases.append(m["surface"] + morph[i+1]["surface"] + morph[i+2]["surface"] )

    output = os.path.join(os.path.dirname(__file__), r"../Output/Chapter4/q34.txt")
    with open(output, mode="w", encoding="utf-8") as f:
        f.write("\n".join(noun_phrases))
