from constant import PROMPT_INPUT_FOR_TASK_CLS

from vllm import LLM, SamplingParams
import torch
import os
import json
os.environ["CUDA_VISIBLE_DEVICES"] = "6"


def init():
    num_gpus = torch.cuda.device_count()
    model_name_or_dir = "GAIR/ReAlign-Task-Classifier" # or the local directory to store the downloaded model
    llm = LLM(model=model_name_or_dir, tensor_parallel_size=1)
    return llm

def get_task(llm, query):
    input_ = PROMPT_INPUT_FOR_TASK_CLS.format(input=query)
    sampling_params = SamplingParams(temperature=0.0, top_p=1.0, max_tokens=50)
    outputs = llm.generate(input_, sampling_params)
    task = outputs[0].outputs[0].text
    return task

def convert(llm, input_path, output_path):
    with open(input_path, "r") as f:
        data = json.load(f)
    for i in range(10):
        data[i]["id"] = int(data[i]["id"])
        data[i]["items"] = data[i]["conversations"]
        data[i].pop("conversations", None)
        query = data[i]["items"][0]["value"]
        if "image" in data[i]:
            if data[i]["image"] != None and data[i]["image"] != "":
                query = "Please answer according to the image: " + query
        print(query)
        task = get_task(llm, query)
        data[i]["items"][0]["category"] = task.replace(" ", "")
    with open(output_path, "w") as f:
        json.dump(data, f)
    

def main():
    llm = init()
    # query = "Give three tips for staying healthy."
    # print(get_task(llm, query))
    input_path = "/data2/cs2916_t1/ScienceQA/data/scienceqa/llava_train_QCM-LEA.json"
    output_path = "/data2/cs2916_t1/ScienceQA/data/scienceqa/llava_train_QCM-LEA_converted_image.json"
    convert(llm, input_path, output_path)
    
if __name__ == "__main__":
    main()