import requests
import json
import pandas
import logging
import time
import sys

# get data from json
data = json.load(open("data.json", "r"))

url = data["send_message_url"]
stage_api_key = data["stage_api_key"]
stage_api_secret = data["stage_api_secret"]
prod_api_key = data["prod_api_key"]
prod_api_secret = data["prod_api_secret"]
use_type = "stage" # stage(for testing) and prod(for live)
sender_id = data["sender_id"]
text_message = data["text_message"]

# validate command input
if len(sys.argv) <= 1:
		print('Missing arguments.\nUsage: python3 report.py file-path\n\nFile path to the CSV file containing contacts.\nThe CSV file must contain the following columns:\n\tname: name of the contact\n\tcontact: containing 10 digit contact number or 12 digit contact number starting from 91.')
		exit()

file_path = sys.argv[1]

api_key = stage_api_key if use_type == "stage" else prod_api_key
api_secret = stage_api_secret if use_type == "stage" else prod_api_secret

# get request
def send_post_request(url, api_key, secret_key, use_type, phone_no, sender_id, text_message):
	req_params = {
	"apikey":api_key,
	"secret":secret_key,
	"usetype":use_type,
	"phone": phone_no,
	"message":text_message,
	"senderid":sender_id
	}
	return requests.post(url, req_params)

# get contact list
def contact_list(path):
	colnames = ["name", "contact"]
	data = pandas.read_csv(path, names=colnames, header=0)
	return data.contact.tolist()

# log file config
logging.basicConfig(filename="info.log",
					format="%(asctime)s: %(message)s",
					filemode="a",
					datefmt="%H:%M:%S",
					level=logging.DEBUG)
logger = logging.getLogger(__name__)

contacts = contact_list(file_path)

for i, contact in enumerate(contacts):
	print(f"{use_type}: Sending message {i} to {contact}")
	logger.info(f"{use_type}: Sending message {i} to {contact}")
	# response = send_post_request(url, api_key, api_secret, use_type, contact, sender_id, text_message)
	# print(f"Status code: {response.status_code}")
	# logger.info(f"Status code: {response.status_code}")
	time.sleep(0.5)
