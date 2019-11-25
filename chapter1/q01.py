# 「パタトクカシーー」
# 「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．

STRING = 'パタトクカシーー'
result = ''.join([chr for i,chr in enumerate(STRING) if i % 2 == 0])

print(result)