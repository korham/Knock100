# 10. 行数のカウント
# 行数をカウントせよ．確認にはwcコマンドを用いよ．

import os.path

def count_row(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return len(lines)

if __name__ == "__main__":
    file = os.path.join(os.path.dirname(__file__), '../DataSource/hightemp.txt')
    print(count_row(file))
    