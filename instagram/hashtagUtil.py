def extract_hashtags(caption):
	"""
	Simple hashtag extractor to return the hastags in the post
	:return:
	"""
	hashtags = []
	if caption is None:
		return hashtags
	else:
		for tag in re.findall("#[a-zA-Z0-9]+", caption):
			hashtags.append(tag)
	return hashtags