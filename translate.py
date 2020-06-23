import json
from googletrans import Translator

translator = Translator(service_urls=[
      'translate.google.com'
])


with open('data.json', 'r') as f:
    data = json.load(f)

for d in data:
    d['Name_Pt'] = translator.translate(d['Name'], src='en', dest='pt').text
    print(d['Name'], '->', d['Name_Pt'])

with open('data_transformed.json', 'w') as f:
    f.write(json.dumps(data, ensure_ascii=False))
