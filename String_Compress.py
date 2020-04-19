# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

# a_list = [line for line in sys.stdin]
# a_string = str(a_list[0])
a_string = '1222311'

res = []
ctr = 1
for i in range(len(a_string)):
    if i == len(a_string) - 1:
        res.append((ctr, int(a_string[i])))
    else:
        if a_string[i] == a_string[i+1]:
            ctr += 1
        else:
            res.append((ctr, int(a_string[i])))
            ctr = 1

for i in res:
    print(str(i), end = " ")
