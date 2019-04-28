'''
MIT License

Copyright (c) 2019 Modassir Akhtar

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

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

		if innings["overs"] != over:
			print (innings)
			over = innings["overs"]
			prev_overs = score["prev_overs"].strip()
			last_ball = prev_overs[-1]
			if last_ball == "6":
				print ("Hurray SIX! at " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
				print ('\a')

		time.sleep(10)

if __name__ == '__main__':
	main()
