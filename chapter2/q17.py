# 17. １列目の文字列の異なり

# 1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．

import os

def sort_uniq(file):
    with open(file, encoding="utf-8") as f:
        col1_strings = [s.split()[0] for s in f]
    return set(col1_strings)

if __name__ == "__main__":
    file = os.path.join(os.path.dirname(__file__), "../DataSource/hightemp.txt")
    result_set = sort_uniq(file)
    print(sorted(list(result_set)))