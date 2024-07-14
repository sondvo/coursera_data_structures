close_and_open = {
    '}': '{',
    ']': '[',
    ')': '(',
}
open_char = list(close_and_open.values())
close_char = list(close_and_open.keys())

def brackets_in_code(input_seq):
	is_opening = [None]
	current_index = [None]

	for i in range(len(input_seq)):
		char = input_seq[i]
		if char in close_char and close_and_open[char] != is_opening[-1]:
			return i + 1

		if char in close_char and close_and_open[char] == is_opening[-1]:
			is_opening = is_opening[:-1]
			current_index = current_index[:-1]
			continue

		if char in open_char:
			is_opening.append(char)
			current_index.append(i)

	if len(is_opening) == 1 and is_opening[0] is None:
		return 'Success'

	return current_index[1] + 1


if __name__ == '__main__':
    input_seq = input()
    print (brackets_in_code(input_seq))