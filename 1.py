import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# 加载预训练的Vicuna-13B-v1.5-16k模型
model_path = "/data/ckpts/vicuna-13b-v1.5-16k"
tokenizer = AutoTokenizer.from_pretrained(model_path)
language_model = AutoModelForCausalLM.from_pretrained(model_path)

# 设置模型为评估模式
language_model.eval()

def generate_response(prompt, tokenizer, model, max_length=512):
    inputs = tokenizer(prompt, return_tensors="pt")
    input_ids = inputs["input_ids"]
    
    # 使用模型生成响应
    with torch.no_grad():
        outputs = model.generate(input_ids, max_length=max_length, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)
    
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

if __name__ == "__main__":
    print("与Vicuna模型对话。输入 'exit' 退出。")
    while True:
        user_input = input("你: ")
        if user_input.lower() == "exit":
            break
        
        response = generate_response(user_input, tokenizer, language_model)
        print(f"Vicuna: {response}")
