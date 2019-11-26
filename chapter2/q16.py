# 16. ファイルをN分割する

# 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．
# 同様の処理をsplitコマンドで実現せよ．

import os
import string

def make_splitted_files(file, out_dir, line_num):
    suffix_list = [s1+s2 for s1 in string.ascii_lowercase for s2 in string.ascii_lowercase]
    suffix_index = 0
    basename = os.path.basename(file)
    name, ext = os.path.splitext(basename)
    with open(file, encoding="utf-8") as f:
        lines = f.readlines()
        # NOTE 接尾辞が不足するケース？
        if len(lines) // line_num + 1 > len(suffix_list):
            raise Exception('Too Many Rows')

        stock_rows = []
        for row in lines:
            if stock_rows and len(stock_rows) % line_num == 0:
                out_basename = name + suffix_list[suffix_index] + ext
                out_file = os.path.join(out_dir, out_basename)
                with open(out_file, mode="w", encoding="utf-8") as of:
                    of.write("".join(stock_rows))
                    stock_rows.clear()
                suffix_index += 1
            stock_rows.append(row)

        # 行数の割り切れなかった分の最終ファイル
        if stock_rows:
            out_basename = name + suffix_list[suffix_index] + ext
            out_file = os.path.join(out_dir, out_basename)
            with open(out_file, mode="w", encoding="utf-8") as of:
                    of.write("".join(stock_rows))

if __name__ == "__main__":
    n = int(input())
    file = os.path.join(os.path.dirname(__file__), '../DataSource/hightemp.txt')
    out_dir = os.path.join(os.path.dirname(__file__), '../Output/Chapter2/q16')
    make_splitted_files(file, out_dir, n)