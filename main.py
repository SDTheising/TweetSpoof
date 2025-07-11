import tweetMaker
import pandas as pd
from datetime import datetime

# Loads the current date, and finds the CSV of tweets collected from today. 
today_str = datetime.now().strftime("%d%m%y")
filename = f"collected_tweets_{today_str}.csv"

def main():

    df = pd.read_csv(filename)

    # Turns the output of the CSV to a list
    tweet_list = df['tweet'].tolist()

    output = []

    # Makes and saves each output tweet.
    for tweet in tweet_list:
        output.append(tweetMaker(tweet))



if __name__ == "__main__":
    main()