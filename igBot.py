from makeBot import MakeBots
from instagram.activityBot import IgActivityBot
from instagram.commentBot import IgCommentBot
from instagram.directBot import IgDirectBot
from instagram.hashtagBot import IgHashtagBot
from instagram.localBot import IgLocalBot
from instagram.mediaBot import IgMediaBot
from instagram.userBot import IgUserBot


class IgBot(MakeBots, IgActivityBot, IgCommentBot, IgDirectBot, IgHashtagBot, IgLocalBot, IgMediaBot, IgUserBot):
	GRAPHQL_API_URL = 'https://www.instagram.com/graphql/query/'

	# def __init__(self):
	# def authenticate(self):
	# def logout():
	pass