# Use a pipeline as a high-level helper
from transformers import pipeline
import gradio as gr 
pipe = pipeline("summarization", model="ayoubkirouane/T5-4-Summarization")
def summarization(text) :
  return pipe(text)[0]["summary_text"]
# Create a Gradio interface
iface = gr.Interface(
    fn=summarization,
    inputs=gr.Textbox(prompt="Input Text"),
    outputs=gr.Textbox(prompt="Generated Summary") , 
    allow_flagging=False , 
    title="T5-4-Summarization" , 
    description="This app generates a summary of the input text using T5 fine-tuned model.",
)
# Launch the Gradio app
iface.launch(debug=True)