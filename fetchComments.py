import praw
import random

def fetch_comment_text(reddit_url):
    reddit = praw.Reddit(client_id='RMEptsuiFAIls7O8NfhbxA', 
                         client_secret='XpBAWCtNW5-y-fLfhxx6tGNdcNHp2w', 
                         user_agent='Test/0.1 by Internal_Ocelot_181')
    submission = reddit.submission(url=reddit_url)
    comments = [comment.body for comment in submission.comments if isinstance(comment, praw.models.Comment)]
    selected_comments = random.sample(comments, min(5, len(comments)))
    selected_comments.insert(0, submission.title)
    print('Successfully fetched comments')
    return selected_comments
