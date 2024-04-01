import json
import requests
# import nlt_for_railways.views as inputdata

API_URL = "https://api-inference.huggingface.co/models/facebook/mbart-large-50-many-to-many-mmt"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    output=json.dumps(payload)
    response = requests.post(API_URL, headers=headers, json=payload)
    return json.loads(response.content.decode("utf-8"))
	
# output = query({
# 	"inputs": "This is a tree", "parameters" : { "src_lang":"en_XX",
#     "tgt_lang":"ta_IN"}
   
# })
# temp = output[0].values()
# print(*temp)
