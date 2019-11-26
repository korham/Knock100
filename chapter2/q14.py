# 14. 先頭からN行を出力

# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．
# 確認にはheadコマンドを用いよ．
import os

def get_head_rows(file, num):
    with open(file, encoding="utf-8") as f:
        result = [f.readline() for i in range(num)]

    return result

if __name__ == "__main__":
    n = int(input())
    file = os.path.join(os.path.dirname(__file__), '../DataSource/hightemp.txt')
    result = get_head_rows(file, n)
    print("".join(result))