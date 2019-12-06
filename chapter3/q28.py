# 28. MediaWikiマークアップの除去

# 27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，
# 国の基本情報を整形せよ．

import os, re
import q20, q25


def replace_markup(template, pattern, val="", disp="", re_flag=0):
    """
    templateのうち、patternに一致するマークアップを取り除く。
    マークアップはpattern中の<val>または<disp>の文字列に置き換えられる。
    <val>と<disp>の双方がある場合は<disp>が優先される。
    """
    if not disp:
        disp = val

    rec = re.compile(pattern, re_flag)
    pre = ""
    result = template
    # disp：表示名が指定されていれば優先する。
    while pre != result:
        pre = result
        match = rec.search(result)
        if match and disp in match.groupdict().keys() and match.group(disp):
            repl = r"\g<{}>".format(disp)
        else:
            if not val:
                repl = ""
            else:
                repl = r"\g<{}>".format(val)
        result = rec.sub(repl, result, count=1)

    return result

# 強調、内部リンク、外部リンク、カテゴリ、ファイル参照、リダイレクト　を除去
if __name__ == "__main__":
    file = os.path.join(os.path.dirname(__file__), r"..\DataSource\jawiki-country.json.gz")
    article = q20.get_article_from_gzip_json(file, "イギリス")
    template = q25.pick_basic_info_template(article)

    # 強調
    pattern = r"('{5}|'{2,3})(?P<val>.+?)('{5}|'{2,3})"
    result = replace_markup(template, pattern, "val")

    # 内部リンク
    pattern = r"""
                \[\[(?!(ファイル|File|Media|Category):)   #ファイルでもカテゴリーでもない[[ ]]
                (?P<val>.+?)
                (\|(?P<disp>.+?))?
                \]\]
                """
    result = replace_markup(result, pattern, "val", "disp", re.VERBOSE)

    # 外部リンク
    pattern = r"""
            (?<!\[)\[               # OK "[http...]" NG "[[http...]]"
            (?P<val>http.+?)
            ([ ](?P<disp>.+?))?
            \]
            """
    result = replace_markup(result, pattern, "val", "disp", re.VERBOSE)

    # カテゴリ
    pattern = r"""
                    \[\[
                    Category:(?P<val>.+?)
                    (\|.+?)
                    \]\]
                """
    result = replace_markup(result, pattern, "val", re_flag=re.VERBOSE)

    # ファイル
    pattern = r"""
                \[\[
                (ファイル|File|Media):(?P<val>.+?)
                (\|(?P<disp>[^\|]+?))?              # 最後の"|"以降（説明文）を表示
                \]\]
                """
    result = replace_markup(result, pattern, "val", "disp", re.VERBOSE)

    # リダイレクト
    result = result.replace("#REDIRECT", "↳")

    origin = os.path.join(os.path.dirname(__file__), r"..\Output\Chapter3\origin.txt")
    with open(origin, mode="w", encoding="utf-8") as f:
        f.write(template)

    output = os.path.join(os.path.dirname(__file__), r"..\Output\Chapter3\fixed.txt")
    with open(output, mode="w", encoding="utf-8") as f:
        f.write(result)