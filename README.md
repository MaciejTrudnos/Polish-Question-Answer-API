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
Context from answer.txt file
```sh
Okręt był napędzany przez trzy trzycylindrowe maszyny parowe potrójnego rozprężania, które
napędzały poprzez wały napędowe trzy śruby napędowe (dwie trójskrzydłowe
zewnętrzne o średnicy 4,5 metra i czteroskrzydłową o średnicy 4,2 metra).
Para była dostarczana przez cztery kotły wodnorurkowe typu Marine,
wyposażone łącznie w osiem palenisk i osiem kotłów cylindrycznych,
które miały łącznie 32 paleniska. Ciśnienie robocze kotłów wynosiło 12 at,
a ich łączna powierzchnia grzewcza 3560 m². Wszystkie kotły były opalane węglem,
którego normalny zapas wynosił 650, a maksymalny 1070 ton.
Nominalna moc siłowni wynosiła 13 000 KM (maksymalnie 13 922 KM przy 108 obr./min),
co pozwalało na osiągnięcie prędkości maksymalnej od 17,5 do 17,6 węzła.
Zasięg wynosił 3420 mil morskich przy prędkości 10 węzłów. Zużycie węgla przy mocy 10 000 KM
wynosiło około 11 ton na godzinę, a przy mocy maksymalnej 16 ton na godzinę.
```

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