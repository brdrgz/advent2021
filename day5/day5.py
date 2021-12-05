file = open("day5input.txt", "r")
lines = file.readlines()

def part1(lines):
	vents = {}
	for line in lines:
		x1y1_x2y2 = line.rstrip().split(" -> ")
		x1y1,x2y2 = map(lambda pair: pair.split(","), x1y1_x2y2)
		x1,y1,x2,y2 = int(x1y1[0]), int(x1y1[1]), int(x2y2[0]), int(x2y2[1])
		if x1 == x2:
			for yi in range(min(y1,y2), max(y1,y2)+1):
				vents[(x1,yi)] = vents.get((x1,yi), 0) + 1
		elif y1 == y2:
			for xi in range(min(x1,x2), max(x1,x2)+1):
				vents[(xi,y1)] = vents.get((xi,y1), 0) + 1
	return len(list(filter(lambda count: count >= 2, vents.values())))

def part2(lines):
	vents = {}
	for line in lines:
		x1y1_x2y2 = line.rstrip().split(" -> ")
		x1y1,x2y2 = map(lambda pair: pair.split(","), x1y1_x2y2)
		x1,y1,x2,y2 = int(x1y1[0]), int(x1y1[1]), int(x2y2[0]), int(x2y2[1])
		if x1 == x2:
			for yi in range(min(y1,y2), max(y1,y2)+1):
				vents[(x1,yi)] = vents.get((x1,yi), 0) + 1
		elif y1 == y2:
			for xi in range(min(x1,x2), max(x1,x2)+1):
				vents[(xi,y1)] = vents.get((xi,y1), 0) + 1
		else:
			xr = range(x1,x2-1,-1) if x1 > x2 else range(x1,x2+1)
			yr = range(y1,y2-1,-1) if y1 > y2 else range(y1,y2+1)
			for key in zip(xr,yr):
				vents[key] = vents.get(key, 0) + 1
	return len(list(filter(lambda count: count >= 2, vents.values())))


print(part1(lines))
print(part2(lines))

# >>> list(zip(range(7,10),range(9,6,-1)))
# [(7, 9), (8, 8), (9, 7)]

# >>> list(zip(range(9,6,-1),range(7,10)))
# [(9, 7), (8, 8), (7, 9)]

# >>> list(zip(range(1,4),range(1,4)))
# [(1, 1), (2, 2), (3, 3)]
