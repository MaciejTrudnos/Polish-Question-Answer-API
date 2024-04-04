# Polish-Question-Answer-API
Simple Web API Extractive Question-Answer model for polish language

## Model Card
Extractive Question-Answer model for polish. Extractive means, that the most relevant chunk of the text is returned as answer from the context for the given question.

## Model Details
- Model name: [radlab/polish-qa-v2](https://huggingface.co/radlab/polish-qa-v2) 
- Developed by: [radlab.dev](https://radlab.dev)  
- Shared by: radlab.dev
- Model type: QA
- Language(s) (NLP): PL
- License: CC-BY-4.0
- Finetuned from model: [sdadas/polish-roberta-large-v2 ](https://huggingface.co/sdadas/polish-roberta-large-v2) 
- Maxiumum context size: 512 tokens

# Getting start via docker compose
Build image and run container
```sh
docker-compose up -d
```

# Usage
Simple usage via curl
```sh
curl -X POST \
http://127.0.0.1:5000 \
-H 'Content-Type: application/json' \
-d '{"Question":"Jakie silniki posiadał okręt?"}'
```

with the sample output:
```sh
{
  "score": 0.6079185009002686,
  "start": 25,
  "end": 84,
  "answer": "trzy trzycylindrowe maszyny parowe potrójnego rozprężania"
}
```