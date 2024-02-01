import queue
from langchain.llms.ollama import Ollama
from motors import speak

def process(text):
    ollama = Ollama(model="mistral")
    output = ollama.invoke(text)
    print(output)
    speak(output)

