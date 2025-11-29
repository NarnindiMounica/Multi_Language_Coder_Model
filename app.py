import gradio as gr
import json
import requests

#Ollama has a REST API for running and managing models. Get details from github.com/ollama
#beow url is to generate response

url="http://localhost:11434/api/generate"

headers={
    'Content-Type':"application/json"
}

history=[]
def generate_response(prompt):
    history.append(prompt)
    final_prompt = "\n".join(history)
    data={
    
    "model": "Mouni_Mario",
    "prompt": final_prompt,
    "stream": False

    }

    response= requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code==200:
        response = response.text
        data= json.loads(response)
        actual_response=data['response']
        return actual_response
    
    else:
        print(f"Error: {response.text}")


#Gradio framework

interface = gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=4, placeholder="Enter your prompt"),
    outputs=gr.Textbox(lines=10)
)     

interface.launch()