import gradio as gr
from openai import AzureOpenAI
from dotenv import load_dotenv

import os

load_dotenv()
key = os.getenv("OPENAI_KEY")
endpoint = os.getenv("OPENAI_ENDPOINT")
key = os.getenv("GPT4_KEY")
endpoint = os.getenv("GPT4_ENDPOINT")
client = AzureOpenAI(
    api_key=key,  
    api_version="2024-02-01",
    azure_endpoint = endpoint
)

def greet(name, intensity):
    return "Hello, " + name + "!" * int(intensity)

def get_completion(prompt, model="gpt-4"):
    messages = [{"role": "user", "content": prompt}]
    print(f"Prompt: {prompt}")
    response = client.chat.completions.create(
        model=model,
        messages=messages
    )
    completion = response.choices[0].message.content
    print(f"Completion: {completion}")
    return completion

def repeat_after_me(text):
    prompt = "Repeat after me :" + text
    return prompt, get_completion(prompt)

demo = gr.Interface(
    title="Repeat after me",
    description="Prompt\nRepeat after me :{text}",
    fn=repeat_after_me,
    inputs=["text"],
    outputs=[
        gr.Textbox(label="Prompt"),
        gr.Textbox(label="Completion")
    ],
)

demo.launch()
