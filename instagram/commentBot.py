class IgCommentBot():
	@login_required
	def do_like(self):
		self.api.comment_like(comment_id)
		pass
	
	@login_required
	def do_unlike(self, comment_id):
		self.api.comment_unlike(comment_id)
		pass
	
	@login_required
	def do_delete(self, media_id, comment_id):
		self.api.delete_comment(media_id, comment_id)
		pass
	
	@login_required
	def do_replay(self):
		pass
	
	def list_likers(self,comment_id):
		self.api.comment_likers(comment_id):
		# @TODO - Salvar Usuario que curtiu um comentario
		pass