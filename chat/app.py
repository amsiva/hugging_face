from groq import Groq
from dotenv import load_dotenv
load_dotenv()
import os 
import requests
import gradio as gr
import spaces

client = Groq(api_key= os.getenv("GROQ_API_KEY"))

@spaces.GPU
def chat_response(message, history):
    response = client.chat.completions.create(
        model= os.getenv("MODEL_NAME"),
        messages = [{"role":"user", "content": message}]
    )
    return response.choices[0].message.content

with gr.Blocks() as another_demo:
    gr.ChatInterface(title="Groq Chat",
                     fn=chat_response,
                     description="Ask me anything!",
                     examples = ['How are you?', 'MS Dhoni', 'CM Vijay']
                     )
    
if __name__ == "__main__":
    another_demo.launch()


