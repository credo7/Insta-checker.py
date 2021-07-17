def make_nicks_db(old_nicks):
	nicks = []

	try:
		file = open(old_nicks, "r")
	except FileNotFoundError:
		return ([])
	for line in file:
		nicks.append(line.strip('\n'))
	return (nicks)

	