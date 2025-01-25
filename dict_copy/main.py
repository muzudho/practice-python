import copy

a_dict = {
    "a": 10,
    "b": {
        "b1": 20,
        "b2": {
            "b2a": 30
        }
    }
}

b_dict = dict(a_dict)

print('シャローコピー')
print(f'{a_dict}')
print(f'{b_dict}')

# b_dict の方だけ変わる
b_dict['b2a'] = 3099

print(f'{a_dict}')
print(f'{b_dict}')

# a_dict の方も変わる。シャローコピーだから。
b_dict['b']['b1'] = 2099

print(f'{a_dict}')
print(f'{b_dict}')


a_dict = {
    "a": 10,
    "b": {
        "b1": 20,
        "b2": {
            "b2a": 30
        }
    }
}

# ディープコピー
b_dict = copy.deepcopy(a_dict)

# b_dict の方だけ変わる。ディープコピーだから
b_dict['b']['b1'] = 2099

print('ディープコピー')
print(f'{a_dict}')
print(f'{b_dict}')
