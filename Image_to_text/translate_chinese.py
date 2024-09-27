from openai import OpenAI
client = OpenAI(api_key = "")

def gpt(message):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "translate english to Traditional Chinese"},
            {"role": "user", "content": message}
        ]
    )
    reply = completion.choices[0].message.content
    return reply
