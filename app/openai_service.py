import openai
import os


openai.api_key = os.getenv("OPENAI_API_KEY")

async def get_openai_response(email: str) -> str:
    messages = [
        {"role": "system", "content": "You are an assistant that provides basic information based on the domain of an email ID."},
        {"role": "user", "content": f"Extract the organization name and possible names of individuals associated with the email domain: {email}"}
    ]


    try:
        completion = openai.chat.completions.create(
            model="gpt-4o-mini", 
            messages=messages,
            temperature=0.7,
            max_tokens=150,
        )
        return completion.choices[0].message['content'].strip()
    except openai.OpenAIError as e:
        raise Exception(f"OpenAI API error: {e}")
