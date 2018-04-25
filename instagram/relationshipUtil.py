import json

def extract_relationship(self, user, rel_type):

	if rel_type == 'follower':
		rel = 'edge_followed_by'
	else if rel_type == 'following':
		rel = 'edge_follows'

	resp = self.query_relationship(user,rel_type)['data']['user']
	rel_list = resp[rel]['edges']

	while resp[rel]['page_info']['has_next_page']:
		resp = self.query_relationship(user, rel_type, resp[rel]['page_info']['end_cursor'])
		rel_list += resp[rel]['edges']

	return relList


def query_relationship(self, user, rel_type, end_cursor=None):
	headers = self.get_headers("https://www.instagram.com/%s" % user.username)

	variables = "id:" + user.id+ ",first:" + 100

	if end_cursor is not None:
		variables = variables + "last:" + end_cursor
	
	if rel_type == 'follower':
		query_id = 17874545323001329
	else if rel_type == 'following':
		query_id = 17851374694183129

	url = 'https://www.instagram.com/graphql/query/?query_id='+query_id+'&variables={'+variables+'}'
	req = requests.post(url, data=post_data, headers=headers)

	return json.loads(req.text)
