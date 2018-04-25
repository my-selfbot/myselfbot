
from functools import wraps

import json
import csv

def save_relationship_in_csv(type)
	# @TODO - Mudar Nome
	rel_type = if type == "followed": "edge_followed_by" else: "edge_XXXXXXXXXX_by"

	with open(r'followers.csv', 'a') as f:
		writer = csv.writer(f)
		with open('data.json') as data_file:    
		    data = json.load(data_file)
		    for node in data["data"]["user"][rel_type]["edges"]:
	writer.writerow([node["node"]["username"]])

def login_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if not args[0].is_authenticated:
            raise ClientError('Method requires authentication.', 403)
        return fn(*args, **kwargs)
	return wrapper