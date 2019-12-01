# 21. カテゴリ名を含む行を抽出

# 記事中でカテゴリ名を宣言している行を抽出せよ．

import os, re

import q20

def pick_category_rows(article):
    results = re.findall(r"\[\[Category:.*?\]\]\n", article)
    return results

if __name__ == "__main__":
    file = os.path.join(os.path.dirname(__file__), r"..\DataSource\jawiki-country.json.gz")
    article = q20.get_article_from_gzip_json(file, "イギリス")
    result = (pick_category_rows(article))
    print("".join(result))
