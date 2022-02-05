import praw
import os
import time
from dotenv import load_dotenv

#--------------------------------------------------#
# Loading all environment variables from .env file #
#--------------------------------------------------#

load_dotenv()


client_id = os.environ['CLIENT_ID']
client_secret = os.environ['CLIENT_SECRET']
user_agent = os.environ['USER_AGENT']
username = os.environ['USERNAME']
password = os.environ['PASSWORD']
post_message = os.environ['POST_MESSAGE']
post_title = os.environ['POST_TITLE']
subredditName = os.environ['SUBREDDIT']
frequency = os.environ['FREQUENCY']

#----------------------------#
# Initializing reddit client #
#----------------------------#

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent,
    username=username,
    password=password
)

#----------------------------------------------#
# Getting subreddit object from subreddit name #
#----------------------------------------------#

subreddit = reddit.subreddit(subredditName)

#----------------------------------------------#
# Creating a submission draft that we can post #
#----------------------------------------------#

draft = reddit.drafts.create(selftext=post_message, subreddit=subreddit, title=post_title)

#-----------------------------------------------------------------------------#
# Infinite loop that posts the draft ever x seconds as specified in frequency #
#-----------------------------------------------------------------------------#

while True:
    draft.submit()
    time.sleep(float(frequency))