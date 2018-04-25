class IgMediaBot():
	@login_required
	def do_like(self, media_id):
		self.api.post_like(media_id)
		pass

	@login_required
	def do_unlike(self, media_id):
		self.api.delete_like(media_id)
		pass
	
	@login_required
	def do_delete(self, media_id):
		self.api.delete_media(media_id)
		pass
	
	def list_likers(self, media_id):
		self.api.media_likers(media_id)
		pass

	def list_commments(self, media_id):
		self.api.media_comments(media_id,{'max_id':50})
		pass