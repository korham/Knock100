import unittest
from unittest import mock
import tempfile, gzip, os, time, textwrap, re, json

import q20, q21, q22, q23, q24, q25, q26, q27, q28, q29

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

    def test_q24(self):
        article = "[[ファイル:ファイル１]]\n" + \
                  "[[:ファイル:ファイル２]]\n" + \
                  "[[File:ファイル３|サムネイル|説明文]]\n" + \
                  "[[Media:ファイル４]]\n" + \
                  "aiueo[[Media:ファイル５]]aiueo\n" + \
                  "[ファイル:記述ミス１]\n" + \
                  "[::ファイル:記述ミス２]\n"
        result = q24.pick_media_refference(article)
        self.assertListEqual(["ファイル１",
                              "ファイル２",
                              "ファイル３",
                              "ファイル４",
                              "ファイル５"], result)

    def test_q25_pick_basic_info_template(self):
        article = "{{redirect|aiueo}}\n" + \
                    "{{基礎情報 国\n" + \
                    "|略名 = 某国\n" + \
                    "|複数行 = あいう<br>\n" + \
                    "えお\n" + \
                    "}}\n" + \
                    "{{別テンプレート\n" + \
                    "|key = value\n" + \
                    "|key2 = value2\n" + \
                    "}}\n" + \
                    "\n"              
        result = q25.pick_basic_info_template(article)
        expected = "{{基礎情報 国\n" + \
                    "|略名 = 某国\n" + \
                    "|複数行 = あいう<br>\n" + \
                    "えお\n" + \
                    "}}"
        self.assertEqual(expected, result)

    def test_q25_pick_basic_info_template_nesting(self):
        article = "{{redirect|aiueo}}\n" + \
                    "{{基礎情報 国\n" + \
                    "|略名 = 某国\n" + \
                    "|入れ子 = {{あいう}}\n" + \
                    "}}\n" + \
                    "{{別テンプレート\n" + \
                    "|key = value\n" + \
                    "|key2 = value2\n" + \
                    "}}\n" + \
                    "\n"              
        result = q25.pick_basic_info_template(article)
        expected = "{{基礎情報 国\n" + \
                    "|略名 = 某国\n" + \
                    "|入れ子 = {{あいう}}\n" + \
                    "}}"
        self.assertEqual(expected, result)

    def test_q25_to_dict_wiki_template(self):
        template = "{{基礎情報 国\n" + \
                    "|略名 = 某国\n" + \
                    "|複数行 = あいう<br>\n" + \
                    "えお\n" + \
                    "|国章画像 = [[ファイル:ファイル名.jpg|85px|某国の国章]]\n" + \
                    "|国歌 = [[某歌|あいうえお]]\n" + \
                    "}}"
        result = q25.to_dict_wiki_template(template)
        self.assertDictEqual({"略名":"某国",
                              "複数行":"あいう<br>\nえお",
                              "国章画像": "[[ファイル:ファイル名.jpg|85px|某国の国章]]",
                              "国歌": "[[某歌|あいうえお]]"}, result)

    def test_q26_remove_markup_emphasis(self):
        template = "{{基礎情報 国\n" + \
                    "|キー = これは''弱い強調''です\n" + \
                    "|キー２ = これは'''強調'''と'''''強い強調'''''です\n" + \
                    "}}"
        result = q26.remove_markup_emphasis(template)
        self.assertEqual("{{基礎情報 国\n|キー = これは弱い強調です\n" + \
                         "|キー２ = これは強調と強い強調です\n}}"
                         , result)

    def test_q27_remove_markup_innerlink(self):
        template = "{{基礎情報 国\n" + \
                    "|ファイル１ = [[ファイル:ファイル名.jpg|85px|ファイル１]]\n" + \
                    "|ファイル２ = [[File:ファイル名.jpg|ファイル２]]\n" + \
                    "|ファイル３ = [[Media:ファイル名.jpg]]\n" + \
                    "|カテゴリー = [[Category:カテゴリー|aiueo]]\n" + \
                    "|内部リンク１ = これは[[内部リンク１]]です\n" + \
                    "|内部リンク２ = これは[[hoge|内部リンク２]]です\n" + \
                    "}}"       
        result = q27.remove_markup_innerlink(template)
        self.assertEqual("{{基礎情報 国\n" + \
                         "|ファイル１ = [[ファイル:ファイル名.jpg|85px|ファイル１]]\n" + \
                         "|ファイル２ = [[File:ファイル名.jpg|ファイル２]]\n" + \
                         "|ファイル３ = [[Media:ファイル名.jpg]]\n" + \
                         "|カテゴリー = [[Category:カテゴリー|aiueo]]\n" + \
                         "|内部リンク１ = これは内部リンク１です\n" + \
                         "|内部リンク２ = これは内部リンク２です\n" + \
                         "}}"
                         , result)

    def test_q28_replace_markup_outerlink(self):
        template = "{{基礎情報 国\n" + \
                    "|ファイル１ = [[ファイル:ファイル名.jpg|85px|ファイル１]]\n" + \
                    "|内部リンク２ = これは[[https:dummy|内部リンク２]]です\n" + \
                    "|外部リンク１ = URLです→[https://google.com]\n" + \
                    "|外部リンク２ = 名前です→[https://google.com google]\n" + \
                    "|カテゴリー = [[Category:カテゴリー|aiueo]]\n" + \
                    "}}"  
        pattern = r"""
                    (?<!\[)\[               # OK "[http...]" NG "[[http...]]"
                    (?P<val>http.+?)
                    ([ ](?P<disp>.+?))?
                    \]
                """
        result = q28.replace_markup(template, pattern, "val", "disp", re.VERBOSE)
        self.assertEqual("{{基礎情報 国\n" + \
                            "|ファイル１ = [[ファイル:ファイル名.jpg|85px|ファイル１]]\n" + \
                            "|内部リンク２ = これは[[https:dummy|内部リンク２]]です\n" + \
                            "|外部リンク１ = URLです→https://google.com\n" + \
                            "|外部リンク２ = 名前です→google\n" + \
                            "|カテゴリー = [[Category:カテゴリー|aiueo]]\n" + \
                            "}}", result)

    def test_q28_replace_markup_category(self):
        template = "{{基礎情報 国\n" + \
            "|ファイル２ = [[File:ファイル名.jpg|ファイル２]]\n" + \
            "|カテゴリー = [[Category:カテゴリー|aiueo]]\n" + \
            "}}"
        pattern = r"""
                    \[\[
                    Category:(?P<val>.+?)
                    (\|.+?)
                    \]\]
                """
        result = q28.replace_markup(template, pattern, "val", re_flag=re.VERBOSE)
        self.assertEqual("{{基礎情報 国\n" + \
                         "|ファイル２ = [[File:ファイル名.jpg|ファイル２]]\n" + \
                         "|カテゴリー = カテゴリー\n" + \
                         "}}"
                         , result)   

    def test_q28_replace_markup_file(self):
        template = "{{基礎情報 国\n" + \
                    "|ファイル１ = [[ファイル:ファイル名.jpg|85px|ファイル１]]\n" + \
                    "|ファイル２ = [[File:ファイル名.jpg|ファイル２]]\n" + \
                    "|ファイル３ = [[Media:ファイル名.jpg]]\n" + \
                    "|カテゴリー = [[Category:カテゴリー|aiueo]]\n" + \
                    "|内部リンク１ = これは[[内部リンク１]]です\n" + \
                    "|内部リンク２ = これは[[hoge|内部リンク２]]です\n" + \
                    "}}"  
        pattern = r"""
                    \[\[
                    (ファイル|File|Media):(?P<val>.+?)
                    (\|(?P<disp>[^\|]+?))?              # 最後の"|"以降（説明文）を表示
                    \]\]
                    """
        result = q28.replace_markup(template, pattern, "val", "disp", re.VERBOSE)
        self.assertEqual("{{基礎情報 国\n" + \
                         "|ファイル１ = ファイル１\n" + \
                         "|ファイル２ = ファイル２\n" + \
                         "|ファイル３ = ファイル名.jpg\n" + \
                         "|カテゴリー = [[Category:カテゴリー|aiueo]]\n" + \
                         "|内部リンク１ = これは[[内部リンク１]]です\n" + \
                         "|内部リンク２ = これは[[hoge|内部リンク２]]です\n" + \
                         "}}"
                         , result)

    def test_q29_get_national_flag(self):
        template = "{{基礎情報 国\n" + \
                    "|国旗画像 = Flag of the United Kingdom.svg\n" + \
                    "|国章画像 = イギリスの国章\n" + \
                    "|国章リンク = （国章）\n" + \
                    "}}"
        result = q29.get_national_flag(template)
        self.assertEqual("Flag of the United Kingdom.svg", result)

    @mock.patch('q29.requests')
    def test_request_to_mediawiki_for_imageinfo_url(self, mock_request):
        res_json = r'''
                    {
                        "batchcomplete":"",
                        "query":
                        {
                            "normalized": 
                            [
                                {
                                    "from":"File:Billy_Tipton.jpg",
                                    "to":"File:Billy Tipton.jpg"
                                }
                            ],
                            "pages":
                            {
                                "36266497":
                                {
                                    "pageid":36266497,
                                    "ns":6,
                                    "title":"File:Billy Tipton.jpg",
                                    "imagerepository":"local",
                                    "imageinfo":
                                    [
                                        {
                                            "url":"url_here",
                                            "descriptionurl":"descriptionurl",
                                            "descriptionshorturl":"descriptionshorturl"
                                        }
                                    ]
                                }
                            }
                        }
                    }
                    '''
        mock_request.Session().get().json.return_value = json.loads(res_json)
        result = q29.request_to_mediawiki_for_imageinfo_url('url_here', 'url_valid')
        self.assertEqual("url_here", result)

if __name__ == "__main__":
    unittest.main()