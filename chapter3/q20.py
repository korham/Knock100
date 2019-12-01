# 20. JSONデータの読み込み

# Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．
# 問題21-29では，ここで抽出した記事本文に対して実行せよ．


import os, gzip, json


def get_article_from_gzip_json(file, title):
    with gzip.open(file, mode="rt", encoding="utf-8") as gz:
        contents = [json.loads(c) for c in gz.readlines()]
        result = [c for c in contents if c["title"] == title]

        if len(result) == 0:
            return None

    return result[0]["text"]

if __name__ == "__main__":
    file = os.path.join(os.path.dirname(__file__), r"..\DataSource\jawiki-country.json.gz")
    result = get_article_from_gzip_json(file, "イギリス")
    if result:
        print(result)
    else:
        print("該当記事なし。")
