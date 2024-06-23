import json

data_path = "/data2/cs2916_t1/ReAlign/datasets/llava_train_QCM-LEA_converted.json"
output_path = "/data2/cs2916_t1/ReAlign/datasets/llava_train_QCM-LEA_converted.json"

with open(data_path, "r") as f:
    data = json.load(f)

for i in range(len(data)):    
    data[i]["id_str"] = data[i]["id"]
    data[i]["id"] = i

with open(output_path, "w") as f:
    json.dump(data, f)
    