import sys


def stack_with_max(n_orders, all_orders):
	lst = [0] * n_orders
	current_idx = 0
	current_max = 0
	for order in all_orders:
		if len(order) == 2:
			number = int(order[1])
		if order[0] == 'max':
			print (current_max)
		elif order[0] == 'push':
			if number > current_max:
				current_max = number
			lst[current_idx] += number
			current_idx += 1
		elif order[0] == 'pop':
			current_max = max(lst[:current_idx - 1])
			lst[current_idx - 1] = 0
			current_idx -= 1
	return


if __name__ == '__main__':
	input_n = sys.stdin.readlines()
	input_n = [i.split() for i in input_n]
	n_orders = int(input_n[0][0])
	all_orders = input_n[1:]
	stack_with_max(n_orders, all_orders)