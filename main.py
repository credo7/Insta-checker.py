import requests
import sys
from nick_db import make_nicks_db
from last_nick import get_last_nick_index

if (len(sys.argv) != 3):
	print("Usage: " + sys.argv[0] + " old_db.txt new_db.txt")
	exit()
nicks = make_nicks_db(sys.argv[1])
index = get_last_nick_index(nicks)
while (index < len(nicks)):
	response = requests.get("https://instagram.com/" + nicks[index])
	if (response.status_code == 200):
		file = open(sys.argv[2], "a")
		file.write(nicks[index] + "\n")
		file.close()
	elif (response.status_code == 404):
		print("404: " + nicks[index])
	else:
		print("(" + nicks[index] + ") Error: " + str(response))
		exit()
	last_nick = open("last_nick.txt", "w")
	last_nick.write(nicks[index] + "\n")
	last_nick.close()
	index += 1
print("Database " + sys.argv[2] + " is ready")
last_nick = open("last_nick.txt", "w")
last_nick.close()