# 15. 末尾のN行を出力

# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．
# 確認にはtailコマンドを用いよ．
import os

def get_tail_rows(file, num):
    with open(file, encoding="utf-8") as f:
        lines = f.readlines()
    result = lines[:-num-1:-1]
    result.reverse()
    return result

if __name__ == "__main__":
    n = int(input())
    file = os.path.join(os.path.dirname(__file__), '../DataSource/hightemp.txt')
    result = get_tail_rows(file, n)
    print("".join(result))