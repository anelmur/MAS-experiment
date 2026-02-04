import os
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")
base_url = os.getenv("OPENAI_BASE_URL")  # new

client = OpenAI(
    api_key=api_key,
    base_url=base_url,  # will be None if not set, which is fine
)

def call_agent(system_prompt, messages):
    full_messages = [{"role": "system", "content": system_prompt}] + messages
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=full_messages,
    )
    return response.choices[0].message.content

def manager(query):
    system_prompt = "You are a manager agent. Break the user request into 2-3 short tasks."
    messages = [{"role": "user", "content": query}]
    return call_agent(system_prompt, messages)

def researcher(task):
    system_prompt = "You are a research agent. Give concise bullet-point notes for the task."
    messages = [{"role": "user", "content": task}]
    return call_agent(system_prompt, messages)

def writer(summary_notes):
    system_prompt = "You are a writer agent. Turn notes into a clear, friendly answer."
    messages = [{"role": "user", "content": summary_notes}]
    return call_agent(system_prompt, messages)
