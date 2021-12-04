file = open("day3input.txt", "r")
lines = file.readlines()

def part1(lines):
	gamma_rate = 0
	epsilon_rate = 0
	bitstring_size = len(lines[0])-1
	for i in range(bitstring_size):
		zeros = 0
		ones = 0
		for line in lines:
			if line[i] == "0":
				zeros += 1
			elif line[i] == "1":
				ones += 1
		if ones > zeros:
			gamma_rate += 2 ** (bitstring_size-1-i)
		else:
			epsilon_rate += 2 ** (bitstring_size-1-i)
	return gamma_rate * epsilon_rate


print(part1(lines))

def part2(lines):
	lines = list(map(lambda l: l.rstrip(), lines))
	o2_generator_rating = convert_to_decimal(find_most_common(lines))
	co2_scrubber_rating = convert_to_decimal(find_least_common(lines))
	print(o2_generator_rating)
	print(co2_scrubber_rating)
	return o2_generator_rating * co2_scrubber_rating

def find_most_common(bitstrings, i=0):
	if len(bitstrings) == 1:
		return bitstrings[0]
	else:
		zeros = 0
		ones = 0
		for bitstring in bitstrings:
			if bitstring[i] == "0":
				zeros += 1
			elif bitstring[i] == "1":
				ones += 1
		if ones >= zeros:
			return find_most_common(list(filter(lambda b: b[i] == "1", bitstrings)), i+1)
		else:
			return find_most_common(list(filter(lambda b: b[i] == "0", bitstrings)), i+1)

def find_least_common(bitstrings, i=0):
	if len(bitstrings) == 1:
		return bitstrings[0]
	else:
		zeros = 0
		ones = 0
		for bitstring in bitstrings:
			if bitstring[i] == "0":
				zeros += 1
			elif bitstring[i] == "1":
				ones += 1
		if ones < zeros:
			return find_least_common(list(filter(lambda b: b[i] == "1", bitstrings)), i+1)
		else:
			return find_least_common(list(filter(lambda b: b[i] == "0", bitstrings)), i+1)

def convert_to_decimal(bitstring):
	v = 0
	for i,b in enumerate(list(bitstring)):
		if b == "1":
			v += 2 ** (len(bitstring)-1-i)
	print(bitstring)
	return v
	
print(part2(lines))

