import requests
import json
import sys

# get data from json
data = json.load(open("data.json", "r"))

url = data["repost_url"]
api_key = data["prod_api_key"]
api_secret = data["prod_api_secret"]
use_type = "prod"

# validate command input
if len(sys.argv) <= 2:
		print("Missing arguments.\nUsage: python3 report.py from-date to-date\nDate format to use: YYYY-MM-DD")
		exit()

from_date = sys.argv[1] # YYYY-MM-DD
to_date = sys.argv[2] # YYYY-MM-DD

# post request
def send_post_request(url, api_key, secret_key, use_type, from_date, to_date):
	req_params = {
	"apikey":api_key,
	"secret":secret_key,
	"usetype":use_type,
	"fromdate": from_date,
	"todate":to_date
	}
	return requests.post(url, req_params)

# get response
response = send_post_request(url, api_key, api_secret, use_type, from_date, to_date)

# write data to a file
file = open("report.json", "w")
file.write(json.dumps(json.loads(response.text), indent=4, sort_keys=True))
file.close()