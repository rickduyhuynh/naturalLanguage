import praw

def generateData(keyword, subreddits=["all"], resultLimits=50) -> list:
    out = []
    for subreddit in subreddits:
        for result in reddit.subreddit(subreddit).search(keyword, limit=resultLimits): 
            out.append(result.selftext)
            for comment in result.comments.list():
                out.append(comment)
    return out

if __name__ == '__main__':
    reddit = praw.Reddit(client_id='ZweJ_5vnHiceww',
                     client_secret='ntESUzk15C07el8yIvMzyVfFV9E',
                     user_agent='WatsonBot')
    if not reddit:
        print('Authentication failed')
        exit(1)
    print('Authentication successful')

    output = generateData("IBM Cloud")
    print(output)