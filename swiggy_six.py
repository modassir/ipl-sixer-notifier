import time
import sys
import requests

def main():

	score = {}
	innings = {}
	over = "0.0"
	last_ball = "0"

	while (True):
		r = requests.get("https://www.cricbuzz.com/match-api/livematches.json")
		matches = r.json()["matches"]

		for match in matches:
			if matches[match]["series"]["name"] == "Indian Premier League 2019":
				score = matches[match]["score"]
				break

		innings = score["batting"]["innings"][0]

		print (innings)

		if innings["overs"] != over:
			over = innings["overs"]
			prev_overs = score["prev_overs"].strip()
			last_ball = prev_overs[-1]
			if last_ball == "6":
				print ("Hurray SIX! at " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
				print ('\a')

		time.sleep(20)

if __name__ == '__main__':
	main()