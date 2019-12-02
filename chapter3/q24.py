# 24. ファイル参照の抽出

# 記事から参照されているメディアファイルをすべて抜き出せ．

# ファイル参照？
# https://ja.wikipedia.org/wiki/Help:%E6%97%A9%E8%A6%8B%E8%A1%A8
# マークアップ早見表：[[ファイル:Wikipedia-logo-v2-ja.png|thumb|説明文]] 

import os, re
import q20

def pick_media_refference(article):
    result = []
    pattern = r"\[\[:?(ファイル|File|Media):(?P<filename>.+?)(?P<thumb>\|.+?)?(?P<description>\|.+?)?\]\]"
    for m in re.finditer(pattern, article):
        result.append(m.group("filename"))
    return result

if __name__ == "__main__":
    file = os.path.join(os.path.dirname(__file__), r"..\DataSource\jawiki-country.json.gz")
    article = q20.get_article_from_gzip_json(file, "イギリス")
    result = (pick_media_refference(article))
    for i in result:
        print(i)
