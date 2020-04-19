import math

a_string = 'have aniceday'
a_string = a_string.replace(' ', '')

row = int(math.sqrt(len(a_string)))

res = []
tick = 0
short_string = ""
for i in range(len(a_string)):
    short_string += a_string[i]
    if tick < row:
	    tick += 1
    else:
    	res.append(short_string)
    	short_string = ""
    	tick = 0	


for i in res:
    print(i)
