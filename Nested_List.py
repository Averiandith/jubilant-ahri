a_list = [['Harsh', 20], ['Beria', 20], ['Varun', 19], ['Kakunami', 19], ['Vikas', 21]]

first_lowest = a_list[0][1]

for item in a_list:
    if item[1] < first_lowest:
    	first_lowest = item[1]

print('first_lowest:', first_lowest)

second_lowest = a_list[0][1]
res = []

for item in a_list:
    if item[1] > first_lowest and item[1] <= second_lowest:
    	second_lowest = item[1]
    	res.append(item[0])

res.sort()

for i in res:
    print(i)

