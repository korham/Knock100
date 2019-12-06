# 29. 国旗画像のURLを取得する

# テンプレートの内容を利用し，国旗画像のURLを取得せよ．
# （ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）

import os
import re, requests
import q20, q25

def get_national_flag(template):
    pattern = r"^\|国旗画像 = (?P<title>.+?)$"
    m = re.search(pattern, template, re.MULTILINE)
    return m.group("title")

def request_to_mediawiki_for_imageinfo_url(filename, api_url):
    s = requests.Session()
    params = {
        "action": "query",
        "format": "json",
        "prop": "imageinfo",
        "iiprop": "url",
        "titles": "file:" + filename
    }
    r = s.get(url=api_url, params=params)
    data = r.json()
    pages = list(data["query"]["pages"].values())
    url = pages[0]["imageinfo"][0]["url"]

    return url

if __name__ == "__main__":

    file = os.path.join(os.path.dirname(__file__), r"..\DataSource\jawiki-country.json.gz")
    article = q20.get_article_from_gzip_json(file, "ツバル")
    template = q25.pick_basic_info_template(article)

    API_URL = r"https://en.wikipedia.org/w/api.php"

    image_file = get_national_flag(template)
    result = request_to_mediawiki_for_imageinfo_url(image_file, API_URL)
    print(result)