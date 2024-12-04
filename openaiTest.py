from openai import OpenAI
client = OpenAI()
tweet = '⚠️⚠️⚠️ EVERYWHERE ARE YOU READY ??? YES OR NO'

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a conspiracy theorist popular on X.com."},
        {
            "role": "user",
            "content": f"Write a vaguely left-wing spoof tweet based on the following input. Note, if there is no input after the colon, let me know.: {tweet}"
        }
    ]
)

print(completion.choices[0].message)