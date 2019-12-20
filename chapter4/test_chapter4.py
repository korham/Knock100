import unittest
from mecabAnalysys import MecabAnalysys

class TestChapter4(unittest.TestCase):

    def test_mecab_analysys_to_dict(self):
        """
        一般的な動詞の解析
        """
        test = "入っ\t動詞,自立,*,*,五段・ラ行,連用タ接続,入る,ハイッ,ハイッ"
        ma = MecabAnalysys(test)
        result = ma._to_dict(test)
        expection = {"surface": "入っ", "base": "入る", "pos":"動詞", "pos1":"自立"}
        self.assertEqual(expection, result)

    def test_mecab_analysys_to_dict_comma(self):
        """
        解析対象にカンマが入ったケース
        """
        test = ",\t名詞,サ変接続,*,*,*,*,*"
        ma = MecabAnalysys(test)
        result = ma._to_dict(test)
        expection = {"surface": ",", "base": "", "pos":"名詞", "pos1":"サ変接続"}
        self.assertEqual(expection, result)

    def test_mecab_analysys_load(self):
        """
        mecabファイルを読み込んで分析結果をdataに保持する
        """
        test = "吾輩\t名詞,代名詞,一般,*,*,*,吾輩,ワガハイ,ワガハイ\n"
        test += "は\t助詞,係助詞,*,*,*,*,は,ハ,ワ\n"
        test += "EOS\n"
        test += "猫\t名詞,一般,*,*,*,*,猫,ネコ,ネコ\n"
        test += "で\t助動詞,*,*,*,特殊・ダ,連用形,だ,デ,デ\n"
        test += "ある\t助動詞,*,*,*,五段・ラ行アル,基本形,ある,アル,アル\n"
        test += "EOS"
        ma = MecabAnalysys(test)
        ma.load()
        expection = [
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
        self.assertEqual(expection, ma.data)

    def test_mecab_analysys_get_all_morphemes(self):
        """
        data全文の形態素解析結果を1つのリストにまとめて返す
        """
        test = "吾輩\t名詞,代名詞,一般,*,*,*,吾輩,ワガハイ,ワガハイ\n"
        test += "は\t助詞,係助詞,*,*,*,*,は,ハ,ワ\n"
        test += "EOS\n"
        test += "猫\t名詞,一般,*,*,*,*,猫,ネコ,ネコ\n"
        test += "で\t助動詞,*,*,*,特殊・ダ,連用形,だ,デ,デ\n"
        test += "ある\t助動詞,*,*,*,五段・ラ行アル,基本形,ある,アル,アル\n"
        test += "EOS"
        ma = MecabAnalysys(test)
        ma.load()
        expection = [
                        {"surface": "吾輩", "base": "吾輩", "pos":"名詞", "pos1":"代名詞"},
                        {"surface": "は", "base": "は", "pos":"助詞", "pos1":"係助詞"},
                        {"surface": "猫", "base": "猫", "pos":"名詞", "pos1":"一般"},
                        {"surface": "で", "base": "だ", "pos":"助動詞", "pos1":"*"},
                        {"surface": "ある", "base": "ある", "pos":"助動詞", "pos1":"*"},
                    ]
        self.assertEqual(expection, ma.get_all_morphemes())
        
if __name__ == "__main__":
    unittest.main()