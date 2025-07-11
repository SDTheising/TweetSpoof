from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

conspiracy = os.getenv("CONSPIRACY")

client = OpenAI()
tweet = '🚨🚨🚨 MAJOR ALERT: MASSIVE GREEN SKY STORM OVER THE WHITE HOUSE IN WASHINGTON DC HAPPENING NOW !!! THE PANIC IS REAL'

response = client.responses.create(
    model="gpt-4.1-mini",
    instructions="You are a conspiracy theorist who has devoted his life to believing {conspiracy}. You are posting on X.com, the everything app, in order to convince the masses. You have just discovered the following tweet and need to leapfrog off of it. Respond only with the exact content of your outputted tweet.",
    input=tweet
)

print(response.output_text)