# 13. col1.txtとcol2.txtをマージ

# 12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
# 確認にはpasteコマンドを用いよ．

import os
from itertools import zip_longest
import q12

def make_file_paste(left_file, right_file, out_file):
    with open(left_file, encoding="utf-8") as left, \
        open(right_file, encoding="utf-8") as right, \
        open(out_file, mode="w", encoding="utf-8") as out:

        for l,r in zip_longest(left.readlines(), right.readlines(), fillvalue=""):
            template = "{}\t{}\n"
            out.write(template.format(l.strip("\n"), r.strip("\n")))

if __name__ == "__main__":
    # 先にQ12
    in_file = os.path.join(os.path.dirname(__file__), '../DataSource/hightemp.txt')
    left_file = os.path.join(os.path.dirname(__file__), '../Output/Chapter2/col1.txt')
    q12.make_file_cut_col(in_file, left_file, 0)
    right_file = os.path.join(os.path.dirname(__file__), '../Output/Chapter2/col2.txt')
    q12.make_file_cut_col(in_file, right_file, 1)
    # Q13
    out_file = os.path.join(os.path.dirname(__file__), '../Output/Chapter2/q13.txt')
    make_file_paste(left_file, right_file, out_file)
    