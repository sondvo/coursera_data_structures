import sys


def find_parent(idx):
	return int(idx/2)


def find_left_child(idx):
	return 2*idx + 1


def find_right_child(idx):
	return 2*idx + 2


def swap(idx1, idx2, arr):
	tmp_value = arr[idx1]
	arr[idx1] = arr[idx2]
	arr[idx2] = tmp_value
	return arr


def sift_down(idx, arr, res=[]):
	r_child = find_right_child(idx)
	l_child = find_left_child(idx)

	chosen_child = idx
	if r_child < len(arr) and arr[r_child] <= arr[chosen_child]:
		chosen_child = r_child
	if l_child < len(arr) and arr[l_child] <= arr[chosen_child]:
		chosen_child = l_child

	if chosen_child == idx:
		return arr, res

	if arr[chosen_child] < arr[idx]:
		arr = swap(idx, chosen_child, arr)
		res.append([str(idx), str(chosen_child)])
		return sift_down(chosen_child, arr, res)

	return arr, res


def heap_sort(arr):
	n_num = len(arr)
	res=[]
	for idx in range(int(n_num/2) - 1, -1, -1):
		arr, res = sift_down(idx, arr, res)
	return arr, res


if __name__ == '__main__':
	input_n = sys.stdin.readlines()
	input_n = [list(map(int, i.split())) for i in input_n]
	arr = input_n[1]
	sorted_arr, res = heap_sort(arr)
	print (len(res))
	for i in res:
		print (' '.join(i))