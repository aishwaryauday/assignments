list1 = [1,1,2,4,5,6,88,99,78,4,3]
list2 = []
for num in list1:
	if num not in list2:
		list2.append(num)
print(list2)