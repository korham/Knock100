# 07. テンプレートによる文生成
# 引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．
# さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．

def inform_by_template(x:str, y:str, z:str):
    template = "{time}時の{name}は{value}"
    return template.format(time=x, name=y, value=z)

if __name__ == "__main__":
    print(inform_by_template(12, "気温", 22.4))