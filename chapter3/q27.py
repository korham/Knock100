# 27. 内部リンクの除去

# 26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ
# （参考: マークアップ早見表）．


import os, re
import q20, q25

def remove_markup_innerlink(template):
    """
    テンプレートから内部リンクマークアップを除去した文字列を返す。
    ファイル、カテゴリはそのまま。
    """
    pattern = r"""
                \[\[(?!(ファイル|File|Media|Category):)   #ファイルでもカテゴリーでもない[[ ]]
                (?P<link>.+?)
                (\|(?P<disp>.+?))?
                \]\]
                """
    rec = re.compile(pattern, re.VERBOSE)
    pre = ""
    result = template
    # 記事名｜表示名　のパターンなら表示名を優先する。
    while pre != result:
        pre = result
        match = rec.search(result)
        if match and match.group("disp"):
            result = rec.sub(r"\g<disp>", result, count=1)
        else:
            result = rec.sub(r"\g<link>", result, count=1)
    return result

if __name__ == "__main__":

    file = os.path.join(os.path.dirname(__file__), r"..\DataSource\jawiki-country.json.gz")
    article = q20.get_article_from_gzip_json(file, "イギリス")
    template = q25.pick_basic_info_template(article)

    fixed = remove_markup_innerlink(template)

    result = (q25.to_dict_wiki_template(fixed))
    for k,v in result.items():
        print(k,":",v)