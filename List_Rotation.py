a_list = [1, 2, 3, 4, 5]
N = 3
rotation_list = [0 for i in range(len(a_list))]

for i in range(len(a_list)):
    item = a_list[i]
    idx = i - N
    rotation_list[idx] = item

res = ""

for i in rotation_list:
    res += str(i) + ' '

print(res)
