# 22. カテゴリ名の抽出

# 記事のカテゴリ名を（行単位ではなく名前で）抽出せよ

import os, re

import q20

def pick_categories(article):
    result = []
    for r in re.finditer(r"\[\[Category:(?P<category>.*?)\]\]\n", article):
        result.append(r.group("category"))
    return result

if __name__ == "__main__":
    file = os.path.join(os.path.dirname(__file__), r"..\DataSource\jawiki-country.json.gz")
    article = q20.get_article_from_gzip_json(file, "イギリス")
    result = (pick_categories(article))
    print(result)