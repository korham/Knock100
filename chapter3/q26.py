# 26. 強調マークアップの除去

# 25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を
# 除去してテキストに変換せよ（参考: マークアップ早見表）．

import os, re
import q20, q25


def remove_markup_emphasis(template):
    """
    テンプレートから強調マークアップを除去した文字列を返す
    """
    pattern = r"('{5}|'{2,3})(?P<emphasized>.+?)('{5}|'{2,3})"
    sub = re.sub(pattern, r"\g<emphasized>", template)
    return sub

if __name__ == "__main__":
    file = os.path.join(os.path.dirname(__file__), r"..\DataSource\jawiki-country.json.gz")
    article = q20.get_article_from_gzip_json(file, "イギリス")
    template = q25.pick_basic_info_template(article)

    fixed = remove_markup_emphasis(template)

    result = (q25.to_dict_wiki_template(fixed))
    for k,v in result.items():
        print(k,":",v)