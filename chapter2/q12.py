# 12. 1列目をcol1.txtに，2列目をcol2.txtに保存

# 各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
# 確認にはcutコマンドを用いよ．

import os

def make_file_cut_col(in_file, out_file, col):
    with open(in_file, encoding="utf-8") as in_f, \
    open(out_file, mode="w", encoding="utf-8") as out_f:
        rows = [r.rstrip("\n").split("\t") for r in in_f.readlines()]
        for row in rows:
            out_f.write(row[col] + "\n")


if __name__ == "__main__":
    in_file = os.path.join(os.path.dirname(__file__), '../DataSource/hightemp.txt')
    out_file = os.path.join(os.path.dirname(__file__), '../Output/Chapter2/col1.txt')
    make_file_cut_col(in_file, out_file, 0)
    out_file = os.path.join(os.path.dirname(__file__), '../Output/Chapter2/col2.txt')
    make_file_cut_col(in_file, out_file, 1)
