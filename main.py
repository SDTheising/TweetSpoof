import tweetMaker
import pandas as pd
from datetime import datetime

today_str = datetime.now().strftime("%d%m%y")
filename = f"collected_tweets_{today_str}.csv"

def main():

    df = pd.read_csv(filename)

    tweet_list = df['tweet'].tolist()

    output = []
    for tweet in tweet_list:
        output.append(tweetMaker(tweet))



if __name__ == "__main__":
    main()