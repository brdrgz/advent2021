file = open("day2input.txt", "r")
lines = file.readlines()

def part1(lines):
	depth = 0
	distance = 0
	for line in lines:
		direction, value = line.split()
		if direction == "forward":
			distance += int(value)
		elif direction == "up":
			depth -= int(value)
		elif direction == "down":
			depth += int(value)
	return depth * distance

print(part1(lines))

def part2(lines):
	depth = 0
	distance = 0
	aim = 0
	for line in lines:
		direction, value = line.split()
		if direction == "forward":
			distance += int(value)
			depth += aim * int(value)
		elif direction == "up":
			aim -= int(value)
		elif direction == "down":
			aim += int(value)
	return depth * distance
	
print(part2(lines))