# idea: regarless (parent and children) pair, we'ss go with level of tree - parsing all childs in one level
# eg: 	-1
# 		[0, 1, 2]
#  		[4, 5]
#  		[]
#   	stop

import sys

def tree_height(num_seq):
	root_index = num_seq.index(-1)
	original_order = [i for i in range(0, len(num_seq))]
	tree_dict = {}
	for i in range(len(num_seq)):
		index_1 = num_seq[i]
		index_2 = original_order[i]
		if index_1 not in tree_dict:
			tree_dict[index_1] = []
		tree_dict[index_1].append(index_2)

	current_tree_height = 1
	current_level = tree_dict[root_index]
	while len(current_level) > 0:
		new_level = []
		for i in current_level:
			if i not in tree_dict:
				continue
			new_level.extend(tree_dict[i])
		current_level = new_level
		current_tree_height += 1

	return current_tree_height


if __name__ == '__main__':
	input_n = sys.stdin.readlines()
	input_n = [list(map(int, i.split())) for i in input_n]
	arr = input_n[0]
	num_seq = input_n[1]
	print (tree_height(num_seq))