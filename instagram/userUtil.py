def get_userID(self, user):
	try:
		r = self.s.get('https://www.instagram.com/' + self.user_login + '/?__a=1')
		user_data = json.loads(r.text)["graphql"]["user"]
	except BaseException as e:
		print("unable to get user information\n", str(e))
	user_id = json.loads(requests.get("https://www.instagram.com/%s?__a=1" % username).text)['user']['id']

def get_username(self, user):
	pass