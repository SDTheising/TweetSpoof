import asyncio
from twikit import Client
from dotenv import load_dotenv
import os


load_dotenv()

USERNAME = os.getenv("USERNAME")
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")


tweet_text='They can reverse time because the true thinking cell—the Messiah—controls the entire network of cells across beings, bending reality as a single synchronised mind. #CellControl #MessiahNetwork #OneMindOneBody'

# Initialize client
client = Client('en-US')

async def main():
    await client.login(
        auth_info_1=USERNAME,
        auth_info_2=EMAIL,
        password=PASSWORD,
        cookies_file='cookies.json'
    )

    await client.create_tweet(tweet_text)

asyncio.run(main())