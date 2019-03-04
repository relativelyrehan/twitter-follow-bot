import tweepy
import time
print('this is my twitter bot')


CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACESS_KEY = ''
ACESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACESS_KEY, ACESS_SECRET)
api = tweepy.API(auth)
followers = api.followers()
file_name = 'follow_track.txt'

try:
    def retrieve_user_id(file_name):
        f_read = open(file_name, 'r')
        follow_track = int(f_read.read().strip())
        f_read.close()
        return follow_track

    def store_user_id(follow_track, file_name):
        f_write = open(file_name, 'w')
        f_write.write(str(follow_track))
        f_write.close()
        return

    def followback():
        print('retrieving and following...')
        follow_track = retrieve_user_id(FILE_NAME)  
        followers = api.create_friendship(follow_track, tweet_mode = 'extended')
        
    for element in range(len(followers)):
        follow_track = followers[element].id
        store_user_id(follow_track, file_name)
        api.create_friendship(followers[element].id)
        
    while True:
        followback()
        time.sleep(10)
except:
    print('no more followers')
    
    
    
    
    
    
    
    