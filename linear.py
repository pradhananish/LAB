def linear_search(values, target):
	n = len(values)
	for i in range(n):
		if values[i] == target:
			return i

	return -1