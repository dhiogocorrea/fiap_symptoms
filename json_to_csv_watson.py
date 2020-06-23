import json

with open('data_transformed.json', 'r') as f:
    data = json.load(f)


result = []
for d in data:
    id_ = d['ID']
    name = d['Name']
    name_pt = d['Name_Pt']
    result.append(f'symptoms,{id_},{name},{name_pt}')

result_str = '\n'.join(result)

with open('symptoms_entities.csv', 'w') as f:
    f.write(result_str)