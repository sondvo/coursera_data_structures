## Used for quizz


def find(idx, parent_arr):
	while idx != parent_arr[idx-1]:
		idx = parent_arr[idx-1]
	return idx


def union(num1, num2, parent_arr, rank_arr):
	num1_id = find(num1, parent_arr)
	num2_id = find(num2, parent_arr)
	if num1_id == num2_id:
		return parent_arr, rank_arr

	if rank_arr[num1_id - 1] > rank_arr[num2_id - 1]:
		parent_arr[num2_id - 1] = num1_id
	else:
		parent_arr[num1_id - 1] = num2_id
		if rank_arr[num1_id - 1] == rank_arr[num2_id - 1]:
			rank_arr[num2_id - 1] = rank_arr[num2_id - 1] + 1

	return parent_arr, rank_arr



parent_arr = [i + 1 for i in range(12)]
rank_arr = [0] * 12
for i in range(0, 12 - 1):
	parent_arr, rank_arr = union(i, i+1, parent_arr, rank_arr)
print ([i + 1 for i in range(12)])
print (parent_arr)
print (rank_arr)


