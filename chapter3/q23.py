# 23. セクション構造

# 記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．

# wikipediaのセクションレベル？
# 行頭に等号。数が増えるごとに1階層下がる（等号一つは見出し）
# == セクションの見出し ==
# === サブセクションの見出し ===
# ==== サブサブセクションの見出し ====

import os, re
import q20

def pick_sections(article):
    result = []
    # 2つ以上の等号で囲まれた行
    pattern = r"^(?P<level>={2,})(?P<section>.*?)={2,}$"
    for m in re.finditer(pattern, article, flags=re.MULTILINE):
        section = m.group("section").strip()
        level = len(m.group("level")) - 1
        result.append((section, level))
    return result

if __name__ == "__main__":
    file = os.path.join(os.path.dirname(__file__), r"..\DataSource\jawiki-country.json.gz")
    article = q20.get_article_from_gzip_json(file, "日本")
    result = (pick_sections(article))
    for i in result:
        print(i)
