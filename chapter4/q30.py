# 30. 形態素解析結果の読み込み

# 形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
# ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，
# 1文を形態素（マッピング型）のリストとして表現せよ．第4章の残りの問題では，ここで作ったプログラムを活用せよ．

import os, re

class MecabAnalysys():
    """
    src:    MeCabで解析した結果の文字列
    load:   srcを元に解析結果文字列をpythonのリスト・辞書に変換してdataに格納する.
    data:   loadによる変換結果. data[{sentence_idx}][{morpheme_idx}][{dict_key}]
                    [
                        [
                            {"surface": "吾輩", "base": "吾輩", "pos":"名詞", "pos1":"代名詞"},
                            {"surface": "は", "base": "は", "pos":"助詞", "pos1":"係助詞"},
                        ],
                        [
                            {"surface": "猫", "base": "猫", "pos":"名詞", "pos1":"一般"},
                            {"surface": "で", "base": "だ", "pos":"助動詞", "pos1":"*"},
                            {"surface": "ある", "base": "ある", "pos":"助動詞", "pos1":"*"},
                        ],
                    ]        
    """

    def __init__(self, src):
        self.src = src
        self.analysys_format = r"""
                                (?P<surface>.+?)\t  # 表層形
                                (?P<pos>.+?),       # 品詞
                                (?P<pos1>.+?),      # 品詞細分類1
                                (.+?),              # 品詞細分類2
                                (.+?),              # 品詞細分類3
                                (.+?),              # 活用形
                                (.+?),              # 活用型
                                ((?P<base>.+?),      # 原形
                                (.+?),              # 読み
                                (.+?))?               # 発音
                                """
        self.regex = re.compile(self.analysys_format, flags=re.VERBOSE)
        self.data = []

    def load(self):
        result = []
        sentence = []
        for r in self.src:
            if r.strip() == "EOS":
                result.append(sentence)
                sentence = []
            else:
                d = self._to_dict(r)
                if d:
                    sentence.append(d)

        self.data = result

    def _to_dict(self, mecab):
        """
        MeCabの分析結果1行をDictにして返す。フォーマット外ならNoneを返す。
        surface: 表層形，
        base: 基本形
        pos: 品詞
        pos1: 品詞細分類1
        """
        match = self.regex.match(mecab) 
        if match:
            res = {}
            res["surface"] = match.group("surface") if match.group("surface") else ""
            res["base"] = match.group("base") if match.group("base") else ""
            res["pos"] = match.group("pos") if match.group("pos") else ""
            res["pos1"] = match.group("pos1") if match.group("pos1") else ""
            return res
        else:
            return None

if __name__ == "__main__":
    src = os.path.join(os.path.dirname(__file__), r"../Output/Chapter4/neko.txt.mecab")
    with open(src, encoding="utf-8") as f:
        ma = MecabAnalysys(f.readlines())
        ma.load()
    print(len(ma.data))
    print(ma.data[2][1]["surface"])