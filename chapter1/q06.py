# 06.集合
# "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，
# それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
# さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．

from q05 import get_n_gram

X = set(get_n_gram("paraparaparadise", 2))
Y = set(get_n_gram("paragraph", 2))

union = X | Y
intersection = X & Y
difference_xy = X - Y
difference_yx = Y - X

print('和集合 : ' + str(union))
print('積集合 : ' + str(intersection))
print('差集合 X-Y : ' + str(difference_xy))
print('差集合 Y-X : ' + str(difference_yx))

is_in_x = 'se' in X
is_in_y = 'se' in Y

print('Xに"se"は含まれるか : ' + str(is_in_x))
print('Yに"se"は含まれるか : ' + str(is_in_y))