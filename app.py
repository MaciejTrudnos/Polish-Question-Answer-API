import json
from flask import Flask, request
from transformers import pipeline
from waitress import serve

model_path = "radlab/polish-qa-v2"

question_answerer = pipeline("question-answering", model=model_path)

with open('answers.txt', 'r', encoding='utf-8') as file:
    context = file.read().rstrip()
    
app = Flask(__name__)

@app.route("/", methods = ['POST'])
def answer():    
    request_data = request.json
    result = question_answerer(question=request_data["Question"], context=context.replace("\n", " "))
    data_result = {
        "score": result["score"],
        "start": result["start"],
        "end": result["end"],
        "answer": result["answer"].strip()
    }
    json_result = json.dumps(data_result, ensure_ascii=False)
    return json_result
    
if __name__ == "__main__":
    serve(app, listen='*:5000')