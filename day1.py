file = open("day1input.txt", "r")
lines = file.readlines()

def part1(lines):
	num_increases = 0
	for line_number in range(1,len(lines)):
		previous_depth = int(lines[line_number-1])
		current_depth = int(lines[line_number])
		if previous_depth < current_depth:
			num_increases += 1
	return num_increases

print(part1(lines))

def part2(lines):
	num_increases = 0
	previous_sum = None
	for line_number in range(2,len(lines)):
		a = int(lines[line_number-2])
		b = int(lines[line_number-1])
		c = int(lines[line_number])
		if previous_sum is not None and a + b + c > previous_sum:
			num_increases += 1
		previous_sum = a + b + c
	return num_increases

print(part2(lines))