# 19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる

# 各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．


import os
from collections import Counter
from operator import itemgetter

def count_sort(file, col=0, delimiter="\t"):
    with open(file, encoding="utf-8") as f:
        lines = f.readlines()
    counter = Counter(r.split(delimiter)[col] for r in lines)
    result = sorted(counter.items(), key=itemgetter(0))
    result = sorted(counter.items(), key=itemgetter(1), reverse=True)
    result = [str(count) + " " + val + "\n" for val,count in result]
    return result

if __name__ == "__main__":
    file = os.path.join(os.path.dirname(__file__), "../DataSource/hightemp.txt")
    result = count_sort(file)
    print("".join(result))
