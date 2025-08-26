import gradio as gr
from openai import AzureOpenAI
from dotenv import load_dotenv
import os



def get_completion(prompt):
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


load_dotenv()
model = "gpt-4"
if model == "gpt-4":
    key = os.getenv("GPT4_KEY")
    endpoint = os.getenv("GPT4_ENDPOINT")
elif model == "gpt-3":
    key = os.getenv("GPT3_KEY")
    endpoint = os.getenv("GPT3_ENDPOINT")
else:
    raise ValueError("Invalid model")

client = AzureOpenAI(
    api_key=key,  
    api_version="2024-02-01",
    azure_endpoint = endpoint
)

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
