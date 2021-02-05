from mergedeep import merge

a = {"keyA": 1}
b = {"keyB": {"sub1": 10}}
c = {"keyB": {"sub2": 20}}

merged = merge({}, a, b, c)

print(merged)
# {"keyA": 1, "keyB": {"sub1": 10, "sub2": 20}}
