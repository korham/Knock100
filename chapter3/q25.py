# 25. テンプレートの抽出

# 記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．

import os, re
import q20


def pick_basic_info_template(article):
    """
    wiki記事から基礎情報のテンプレートを抜き出す
    """
    pattern = r"\{\{基礎情報.*?\s\}\}"
    m = re.search(pattern, article, re.DOTALL)

    return m[0]

def to_dict_wiki_template(template):
    """
    テンプレート記法の文字列から辞書に変換
    """
    pattern = r"(\s\|)(?P<key>.+?) = (?P<value>.+?(?=\s[\||}]))"
    result = dict()
    for m in re.finditer(pattern, template, re.DOTALL):
        result[m.group("key")] = m.group("value")
    return result

if __name__ == "__main__":
    file = os.path.join(os.path.dirname(__file__), r"..\DataSource\jawiki-country.json.gz")
    article = q20.get_article_from_gzip_json(file, "イギリス")
    template = pick_basic_info_template(article)
    result = (to_dict_wiki_template(template))

    for k,v in result.items():
        print(k,":",v)
