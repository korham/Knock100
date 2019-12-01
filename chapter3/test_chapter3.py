import unittest
import tempfile, gzip, os, time

import q20, q21, q22, q23

class TestChapter3(unittest.TestCase):
    
    def setUp(self):
        self.td = tempfile.TemporaryDirectory()
        
    def tearDown(self):
        self.td.cleanup()

    def test_q20(self):
        file = os.path.join(self.td.name, "test.json.gz")
        with gzip.open(file, mode="wt", encoding="utf-8") as gz:
            gz.write(r'{"text": "１について\n記事本文です。", "title": "タイトル１"}' + "\n")
            gz.write(r'{"text": "２について\n記事本文である。", "title": "タイトル２"}' + "\n")
            gz.write(r'{"text": "３について\n記事本文だよ。", "title": "タイトル３"}' + "\n")
        result = q20.get_article_from_gzip_json(file, "タイトル２")
        self.assertEqual("２について\n記事本文である。", result)

    def test_q20_no_result(self):
        file = os.path.join(self.td.name, "test.json.gz")
        with gzip.open(file, mode="wt", encoding="utf-8") as gz:
            gz.write(r'{"text": "１について\n記事本文です。", "title": "タイトル１"}' + "\n")
            gz.write(r'{"text": "２について\n記事本文である。", "title": "タイトル２"}' + "\n")
            gz.write(r'{"text": "３について\n記事本文だよ。", "title": "タイトル３"}' + "\n")
        result = q20.get_article_from_gzip_json(file, "タイトル４")
        self.assertIsNone(result)

    def test_q21(self):
        article = "あいうえお\n" + \
                  "[aiueo]\n" + \
                  "{12345}\n" + \
                  "[[Category:カテゴリー１]]\n" + \
                  "[[Category:カテゴリー２]]\n" + \
                  "[[Dammy:ダミー]]\n"
        result = q21.pick_category_rows(article)
        self.assertListEqual(["[[Category:カテゴリー１]]\n","[[Category:カテゴリー２]]\n"], result)

    def test_q22(self):
        article = "あいうえお\n" + \
                  "[aiueo]\n" + \
                  "{12345}\n" + \
                  "[[Category:カテゴリー１]]\n" + \
                  "[[Category:カテゴリー２]]\n" + \
                  "[[Dammy:ダミー]]\n"
        result = q22.pick_categories(article)
        self.assertListEqual(["カテゴリー１","カテゴリー２"], result)

    def test_q23(self):
        article = "= 見出し =\n" + \
                  "== セクション1 ==\n" + \
                  "aiueo\n" + \
                  "=== サブセクション1.1 ===\n" + \
                  "== セクション2 ==\n" + \
                  "=== サブセクション2.1 ===\n" + \
                  "==== サブサブセクション2.1.1 ====\n" + \
                  "=== サブセクション2.2 ===\n"
        result = q23.pick_sections(article)
        self.assertListEqual([("セクション1", 1), 
                              ("サブセクション1.1", 2),
                              ("セクション2", 1),
                              ("サブセクション2.1", 2),
                              ("サブサブセクション2.1.1", 3),
                              ("サブセクション2.2", 2)], result)

if __name__ == "__main__":
    unittest.main()