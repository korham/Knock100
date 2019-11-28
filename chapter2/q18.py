# 18. 各行を3コラム目の数値の降順にソート

# 各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
# 確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．

import os

def sort_reverse(file, col):
    with open(file, encoding="utf-8") as f:
        lines = [r.split("\t") for r in f]
    result = ["\t".join(row) for row in sorted(lines, key=lambda x: x[col], reverse=True)]
    return result

if __name__ == "__main__":
    file = os.path.join(os.path.dirname(__file__), "../DataSource/hightemp.txt")
    result = sort_reverse(file, 2)
    print("".join(result))