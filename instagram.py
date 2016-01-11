import urllib
import urllib2

class Instagram:
	def __init__ (self, access_token):
		self.values = {
			"access_token": access_token
		}
		self.base_url = "https://api.instagram.com/v1"

	"""

		Calls Instagram API

	"""

	def call_api (self, url, values, method = "GET"):
		"""
			Send request
		"""

		result = ""
		data = urllib.urlencode (values)
		if method == "GET":
			print url + "?" + data
			response = urllib2.urlopen (url + "?" + data)
			result = response.read()
		elif method == "POST":
			req = urllib2.Request (url, data)
			response = urllib2.urlopen (req)
			result = response.read()
		elif method == "PUT":
			opener = urllib2.build_opener (urllib2.HTTPHandler)
			request = urllib2.Request (url, data)
			request.get_method = lambda: 'PUT'
			response = urllib2.urlopen (request)
			result = response.read()
		elif method == "DELETE":
			opener = urllib2.build_opener (urllib2.HTTPHandler)
			request = urllib2.Request (url, data)
			request.get_method = lambda: 'DELETE'
			response = urllib2.urlopen (request)
			result = response.read()
		return result




	"""

		Users API
		
		self_info() - get information about the owner of the access_token
		user_info (string) - get information about a user; this endpoint requires the public_content scope if the user_id is not the owner of the access_token
		self_recent (count = integer, min_id = string, max_id = string) - get the most recent media published by the owner of the access_token
			count - count of media to return
			min_id - return media later than this min_id
			max_id - return media earlier than this max_id
		user_recent (string, count = integer, min_id = string, max_id = string) - get the most recent media published by a user; this endpoint requires the public_content scope if the user_id is not the owner of the access_token
			count - count of media to return
			min_id - return media later than this min_id
			max_id - return media earlier than this max_id
		self_liked (count = integer, max_like_id = string) - get the list of recent media liked by the owner of the access_token
			count - count of media to return
			max_like_id - return media liked before this id
		search_users (q = string, count = integer) - get a list of users matching the query
			q - a query string
			count - number of users to return

	"""

	def self_info (self):
		url = "%s/users/self" % (self.base_url)
		result = self.call_api (url, self.values, "GET")
		return result

	def user_info (self, user_id):
		url = "%s/users/%s" % (self.base_url, user_id)
		result = self.call_api (url, self.values, "GET")
		return result

	def self_recent (self, **kwargs):
		url = "%s/users/self/media/recent" % (self.base_url)
		values = self.values
		for k, v in kwargs.iteritems():
			values[k] = v
		result = self.call_api (url, values, "GET")
		return result

	def user_recent (self, user_id, **kwargs):
		url = "%s/users/%s/media/recent" % (self.base_url, user_id)
		values = self.values
		for k, v in kwargs.iteritems():
			values[k] = v
		result = self.call_api (url, values, "GET")
		return result

	def self_liked (self, **kwargs):
		url = "%s/users/self/media/liked" % (self.base_url)
		values = self.values
		for k, v in kwargs.iteritems():
			values[k] = v
		result = self.call_api (url, values, "GET")
		return result


	def search_users (self, **kwargs):
		url = "%s/users/search" % (self.base_url)
		values = self.values
		for k, v in kwargs.iteritems():
			values[k] = v
		result = self.call_api (url, values, "GET")
		return result




	"""

		Relationships API

		self_follows() - get the list of users this user follows
		self_followed_by() - get the list of users this user is followed by
		self_requested_by() - list the users who have requested this user's permission to follow
		get_user_relationship (string) - get information about a relationship to another user; relationships are expressed using the following terms in the response:
			* outgoing_status: your relationship to the user; can be "follows", "requested", "none"
			* incoming_status: a user's relationship to you; can be "followed_by", "requested_by", "blocked_by_you", "none"
		post_user_relationship (string, string) - modify the relationship between the current user and the target user; you need to include an action parameter to specify the relationship action you want to perform; relationships are expressed as in get_user_relationship()
			action - follow | unfollow | approve | ignore

	"""

	def self_follows (self):
		url = "%s/users/self/follows" % (self.base_url)
		result = self.call_api (url, self.values, "GET")
		return result

	def self_followed_by (self):
		url = "%s/users/self/followed-by" % (self.base_url)
		result = self.call_api (url, self.values, "GET")
		return result

	def self_requested_by (self):
		url = "%s/users/self/requested-by" % (self.base_url)
		result = self.call_api (url, self.values, "GET")
		return result

	def get_user_relationship (self, user_id):
		url = "%s/users/%s/relationship" % (self.base_url, user_id)
		result = self.call_api (url, self.values, "GET")
		return result

	def post_user_relationship (self, user_id, action):
		url = "%s/users/%s" % (self.base_url, user_id)
		values = self.values
		values["action"] = action
		result = self.call_api (url, values, "POST")
		return result



	"""

		Media API

		media_by_id (string) - get information about a media object; use the type field to differentiate between image and video media in the response; you will also receive the user_has_liked field which tells you whether the owner of the access_token has liked this media; the public_content permission scope is required to get a media that does not belong to the owner of the access_token
		media_by_shortcode (string) - this endpoint returns the same response as GET /media/media-id; a media object's shortcode can be found in its shortlink URL; an example shortlink is http://instagram.com/p/tsxp1hhQTG/ - its corresponding shortcode is tsxp1hhQTG
		media_search (lat = float, lng = float, distance = integer) - search for recent media in a given area
			lat - latitude of the center search coordinate; if used, lng is required
			lng - longitude of the center search coordinate; if used, lat is required
			distance - default is 1km (distance=1000), max distance is 5km

	"""

	def media_by_id (self, media_id):
		url = "%s/media/%s" % (self.base_url, media_id)
		result = self.call_api (url, self.values, "GET")
		return result

	def media_by_shortcode (self, shortcode):
		url = "%s/media/shortcode/%s" % (self.base_url, shortcode)
		result = self.call_api (url, self.values, "GET")
		return result

	def media_search (self, **kwargs):
		url = "%s/media/search" % (self.base_url)
		values = self.values
		cd = False
		first = ""
		for k,v in kwargs.iteritems():
			if (k == "lat" or k == "lng") and not cd:
				cd = True
				first = k
			elif (k == "lat" or k == "lng") and cd:
				if k == first:
					raise ValueError ("One of coordinates were mentioned twice")
				cd = False
			values[k] = v
		if not cd:
			result = self.call_api (url, values, "GET")
		else:
			raise ValueError ("One of coordinates missing")
		return result


	"""

		Comments API

		get_comments (string) - get a list of recent comments on a media object; the public_content permission scope is required to get comments for a media that does not belong to the owner of the access_token
		post_comment (string, string) - create a comment on a media object with the following rules:
			* the total length of the comment cannot exceed 300 characters
			* the comment cannot contain more than 4 hashtags
			* the comment cannot contain more than 1 URL
			* the comment cannot consist of all capital letters
		delete_comment (string, string) - remove a comment either on the authenticated user's media object or authored by the authenticated user

	"""

	def get_comments (self, media_id):
		url = "%s/media/%s/comments" % (self.base_url, media_id)
		result = self.call_api (url, self.values, "GET")
		return result

	def post_comment (self, media_id, text):
		url = "%s/media/%s/comments" % (self.base_url, media_id)
		values = self.values
		values["text"] = text
		result = self.call_api (url, values, "POST")
		return result

	def delete_comment (self, media_id, comment_id):
		url = "%s/media/%s/comments/%s" % (self.base_url, media_id, comment_id)
		result = self.call_api (url, self.values, "DELETE")
		return result



	"""

		Likes API

		get_likes (string) - get a list of users who have liked this media
		like (string) - set a like on this media by the currently authenticated user; the public_content permission scope is required to create likes on a media that does not belong to the owner of the access_token
		unlike (string) - remove a like on this media by the currently authenticated user; The public_content permission scope is required to delete likes on a media that does not belong to the owner of the access_token

	"""

	def get_likes (self, media_id):
		url = "%s/media/%s/likes" % (self.base_url, media_id)
		result = self.call_api (url, self.values, "GET")
		return result

	def like (self, media_id):
		url = "%s/media/%s/likes" % (self.base_url, media_id)
		result = self.call_api (url, self.values, "POST")
		return result

	def unlike (self, media_id):
		url = "%s/media/%s/likes" % (self.base_url, media_id)
		result = self.call_api (url, self.values, "DELETE")
		return result



	"""

		Tags API

		tag_info (string) - get information about a tag object
		recent_tagged_media (string) - get a list of recently tagged media
		search_tags (string) - search for tags by name

	"""

	def tag_info (self, name):
		url = "%s/tags/%s" % (self.base_url, name)
		result = self.call_api (url, self.values, "GET")
		return result

	def recent_tagged_media (self, name, **kwargs):
		url = "%s/tags/%s/media/recent" % (self.base_url, name)
		values = self.values
		for k, v in kwargs.iteritems():
			values[k] = v
		result = self.call_api (url, values, "GET")
		return result

	def search_tags (self, query):
		url = "%s/tags/search" % (self.base_url)
		values = self.values
		values["q"] = query
		result = self.call_api (url, values, "GET")
		return result


	"""

		Locations API
		
		location_info (string) - get information about a location
		recent_media_from_location (string, min_id = string, max_id = string) - get a list of recent media objects from a given location
		search_location () - search for a location by geographic coordinate
			distance - default is 1000m (distance=1000), max distance is 5000
			facebook_places_id - returns a location mapped off of a Facebook places id; if used, a Foursquare id and lat, lng are not required
			foursquare_id - returns a location mapped off of a foursquare v1 api location id; if used, you are not required to use lat and lng; note that this method is deprecated; you should use the new foursquare IDs with V2 of their API
			lat - latitude of the center search coordinate; if used, lng is required
			lng - longitude of the center search coordinates; If used, lat is required.
			foursquare_v2_id - returns a location mapped off of a foursquare v2 api location id; if used, you are not required to use lat and lng
	"""

	def location_info (self, location_id):
		url = "%s/locations/%s" % (self.base_url, location_id)
		result = self.call_api (url, self.values, "GET")
		return result

	def recent_media_from_location (self, location_id, **kwargs):
		url = "%s/locations/%s/media/recent" % (self.base_url, name)
		values = self.values
		for k, v in kwargs.iteritems():
			values[k] = v
		result = self.call_api (url, values, "GET")
		return result

	def search_location (self, **kwargs):
		url = "%s/locations/%s/media/recent" % (self.base_url, name)
		values = self.values
		unique = False
		cd = False
		for k, v in kwargs.iteritems():
			if (k == "facebook_places_id" or k == "foursquare_id" or k == "foursquare_v2_id") and not unique:
				unique = True
			elif unique:
				raise ValueError ("Excess data")
			elif (k == "lat" or k == "lng") and not cd:
				cd = True
				first = k
			elif (k == "lat" or k == "lng") and cd:
				if k == first:
					raise ValueError ("One of coordinates were mentioned twice")
				cd = False
			values[k] = v
		if not cd:
			result = self.call_api (url, values, "GET")
		else:
			raise ValueError ("One of coordinates missing")
		return result
