import re

class MecabAnalysys():
    """
    src:        MeCabで解析した結果の文字列
    load():     srcを元に解析結果文字列をpythonのリスト・辞書に変換してdataに格納する.
    data:       loadによる変換結果. data[sentence_idx][morpheme_idx]["dict_key"]
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

    def __init__(self, src:str):
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
        self._data = []

    @property
    def data(self):
        return self._data

    def sentence(self, index:int):
        return self._data[index]

    def load(self):
        result = []
        sentence = []
        for r in self.src.split("\n"):
            if r.strip() == "EOS":
                result.append(sentence)
                sentence = []
            else:
                d = self._to_dict(r)
                if d:
                    sentence.append(d)

        self._data = result

    def _to_dict(self, mecab:str):
        """
        MeCabの分析結果1行をdictにして返す。フォーマット外ならNoneを返す。
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

    def get_all_morphemes(self):
        res = []
        for sentence in self._data:
            res.extend(sentence)
        return res