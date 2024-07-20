# idea: create an array of shape = n_thread, putting processing time inside
# after each second, every processing time reduce by one
# whenver there is a free thread (which means processing time = 0 in that thread), add another task into it

import sys
import time


def parallel_processing(n_threads, n_tasks, task_times):
	times_arr = [0] * n_threads
	current_time = 0
	current_task = n_threads

	times_arr[:n_threads] = task_times[:n_threads]
	for i in range(n_threads):
		print (i, current_time)

	# TODO: optimize!!!!.
	while current_task < n_tasks:
		sorted_time_arr = sorted(times_arr)
		if sorted_time_arr[0] == 0:
			tmp_least = sorted_time_arr[1]
		else:
			tmp_least = sorted_time_arr[0]

		times_arr = [j - tmp_least for j in times_arr]
		current_time += tmp_least

		tmp_times_arr = times_arr.copy()
		for free_thread_idx, tmp_current_time in enumerate(tmp_times_arr):
			if tmp_current_time == 0:
				print (free_thread_idx, current_time)
				times_arr[free_thread_idx] = task_times[current_task]
				current_task += 1

	return


if __name__ == '__main__':
	input_n = sys.stdin.readlines()
	input_n = [list(map(int, i.split())) for i in input_n]
	n_threads, n_tasks = input_n[0]
	task_times = input_n[1]
	parallel_processing(n_threads, n_tasks, task_times)

