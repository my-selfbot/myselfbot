# @TODO - Criar Mescanismo de Log

import relationship as rel

class IgUserBot():

	@login_required
	def list_media_by_user(self):
		pass

	@login_required
	def list_feed_media(self):
		pass

	@login_required
	def list_popular_media(self):
		pass

	@login_required
	def list_my_posted_media(self):
		pass

	@login_required
	def list_my_saved_media(self):
		pass

	@login_required
	def list_my_liked_media(self):
		pass

	@login_required
	def do_follow_user(self, user_id):
		self.api.friendships_create(user_id)
		pass

	@login_required
	def do_unfollow_user(self, user_id):
		self.api.friendships_destroy(user_id)
		pass
	
	def list_follower_user(self, user):
		# users = rel.extract_relationship(self, user, 'follower')
		pass

	def list_following_user(self, user):
		# users = rel.extract_relationship(self, user, 'following')
		pass