import requests
import json

input_path = "inference-input.json"

with open(input_path) as json_file:
	data = json.load(json_file)

r = requests.post(url="http://localhost:8080/v1/models/flower-sample:predict", data=json.dumps(data), headers={'Host': 'flower-sample.kubeflow.example.com'})
print(r.text)
