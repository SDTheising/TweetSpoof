from openai import OpenAI
from dotenv import load_dotenv
import os


def tweetMaker(reference):
    load_dotenv()

    conspiracy = os.getenv("CONSPIRACY")

    client = OpenAI()
    tweet = reference

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": f"You are a conspiracy theorist who has devoted his life to believing {conspiracy}. You are posting on X.com, the everything app, in order to convince the masses. You have just discovered the following tweet and need to leapfrog off of it. Keep the tone somewhat serious, you really believe this. Respond only with the exact content of your outputted tweet."},
            {"role": "user", "content": tweet}
        ]
    )

    return response.choices[0].message.content


def main():

    placeholder = "🚨🚨🚨 MAJOR ALERT: WE JUST TURNED TIME BACKWARDS 60 DAYS YOU ALREADY KNOW !!!"

    print(tweetMaker(placeholder))


if __name__ == "__main__":
    main()