# 11. タブをスペースに置換

# タブ1文字につきスペース1文字に置換せよ．
# 確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

import os.path

def make_file_tab_replaced(in_file, out_file):
    with open(in_file, "r", encoding="utf-8") as in_f, \
     open(out_file, "w", encoding="utf-8") as out_f:
        for l in in_f.readlines():
            out_f.write(l.replace("\t", " "))

if __name__ == "__main__":
    in_file = os.path.join(os.path.dirname(__file__), '../DataSource/hightemp.txt')
    out_file = os.path.join(os.path.dirname(__file__), '../Output/q11.txt')
    make_file_tab_replaced(in_file, out_file)