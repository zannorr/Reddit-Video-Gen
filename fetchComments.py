import praw
import random

def fetch_comment_text(reddit_url):
    with open('clientid.txt', 'r') as file:
        client_id = file.read().strip()
    with open('clientsecret.txt', 'r') as file:
        client_secret = file.read().strip()
    with open('useragent.txt', 'r') as file:
        user_agent = file.read().strip()
    reddit = praw.Reddit(client_id=client_id, # 'RMEptsuiFAIls7O8NfhbxA' 
                         client_secret=client_secret, #'XpBAWCtNW5-y-fLfhxx6tGNdcNHp2w'
                         user_agent=user_agent) #'Test/0.1 by Internal_Ocelot_181'
    submission = reddit.submission(url=reddit_url)
    comments = [comment.body for comment in submission.comments if isinstance(comment, praw.models.Comment)]
    selected_comments = random.sample(comments, min(8, len(comments)))
    selected_comments.insert(0, submission.title)
    print('Successfully fetched comments')
    return selected_comments

if __name__ == '__main__':
    print(fetch_comment_text('https://www.reddit.com/r/AskReddit/comments/1hegsgk/whats_a_secret_life_hack_that_everyone_should_know/')) #Test URL