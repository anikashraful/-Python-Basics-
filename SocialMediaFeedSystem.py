# Social media data structures

users = {} # Dictionary: user_id -> user_info
posts = [] # List: chronological posts
hashtags = set() #Set: unique hashtag
connections = {} # Dictionary: user_id -> set of friends


#create user
def create_user(user_id, name, email):
	users[user_id] = {
		'name': name,
		'email': email,
		'followers': set(),
		'following': set()
	}
	connections[user_id] = set()

# create post
def create_post(user_id, content, tags):
	post = {
		'user_id': user_id,
		'content': content,
		'timestamp': '2025-09-17',
		'tags': tags,
		'likes': set() # set of user_ids who liked
	}
	posts.append(post)
	hashtags.update(tags) #add new hashtags to global set

#example
create_user(1, 'Anik','anik@anik.com')
create_post(1,'learning Python!',['python','coding'])

#output
print(f'All hashtags: {hashtags}')