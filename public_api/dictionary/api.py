from matplotlib.font_manager import json_dump, json_load
import requests
import os
import dotenv
import json

URL = "https://owlbot.info/api/v4/dictionary/"

dotenv.load_dotenv()
API_KEY = os.getenv('apikey')

def get_definition(word):
	"""Get request to API with word and returns the data"""

	request_header = {
		'Authorization': f'Token {API_KEY}'
	}

	r = requests.get(url=f'{URL}{word}', headers=request_header)
	json_data = json.loads(r.text) 

	return json_data



