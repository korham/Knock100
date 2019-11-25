# 08. 暗号文
# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
#     英小文字ならば(219 - 文字コード)の文字に置換
#     その他の文字はそのまま出力
# この関数を用い，英語のメッセージを暗号化・復号化せよ．

def cipher(string: str):
    CRITERIA = 219
    result = ""
    for c in string:
        if c.isalpha() and c.islower():
            code = int.from_bytes(str(c).encode("utf-8"), byteorder="big")
            converted_char = ((CRITERIA - code).to_bytes(1, byteorder="big")).decode("utf-8")
            result += converted_char
        else:
            result += c

    return result

if __name__ == "__main__":
    origin = "I Can't Get No Satisfaction!"
    result = cipher(origin)
    print(result)
    print(cipher(result))