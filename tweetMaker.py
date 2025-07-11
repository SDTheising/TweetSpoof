from openai import OpenAI
from dotenv import load_dotenv
import os

# ---- SETUP ----
load_dotenv()
conspiracy = os.getenv("CONSPIRACY")
client = OpenAI()


def truncate_at_last_period(text):
    last_period = text.rfind(".")
    if last_period != -1:
        return text[:last_period + 1]
    return text  # fallback: no period found

def clean_for_tweet(text, max_len=280):
    truncated = text[:max_len]
    return truncate_at_last_period(truncated)




# Sends in tweet for response, and returns response.
def tweetMaker(reference, conspiracy):

    tweet = reference
    curr_conspiracy = conspiracy

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        #System prompt and message, conspiracy itself is hidden in .env so my account won't be so obvious.
        messages=[
            {"role": "system", "content": f"You are a conspiracy theorist who has devoted his life to believing {curr_conspiracy}. You are posting on X.com, the everything app, in order to convince the masses. You have just discovered the following tweet and need to leapfrog off of it. Keep the tone somewhat serious, you really believe this. Respond only with the exact content of your outputted tweet."},
            {"role": "user", "content": tweet}
        ],
        max_tokens=70
    )

    output = response.choices[0].message.content
    output = clean_for_tweet(output)
    return output

# Main module for individual testing.
def main():

    placeholder = "🚨🚨🚨 MAJOR ALERT: WE JUST TURNED TIME BACKWARDS 60 DAYS YOU ALREADY KNOW !!!"

    print(tweetMaker(placeholder, conspiracy))


if __name__ == "__main__":
    main()