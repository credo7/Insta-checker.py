def get_last_nick_index(nicks):
	try:
		file = open("last_nick.txt", "r")
	except FileNotFoundError:
		return (0)
	last_nick = file.readline().strip('\n')
	if (last_nick == ""):
		return (0)
	print("last: " + last_nick)
	index = 0
	for i in nicks:
		index += 1
		if (i == last_nick):
			break
	return (index)