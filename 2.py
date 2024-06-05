import torch
from transformers import CLIPProcessor, CLIPModel, AutoTokenizer, AutoModelForCausalLM
from PIL import Image

# 加载预训练的 CLIP 模型
clip_model = CLIPModel.from_pretrained("openai/clip-vit-large-patch14")
clip_processor = CLIPProcessor.from_pretrained("openai/clip-vit-large-patch14")

# 加载预训练的 Vicuna-7B-v1.5-16k 模型
model_path ="lmsys/vicuna-13b-v1.5"
tokenizer = AutoTokenizer.from_pretrained(model_path)
language_model = AutoModelForCausalLM.from_pretrained(model_path)

# 将模型移动到 GPU，如果可用的话
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
clip_model.to(device)
language_model.to(device)

# 设置模型为评估模式
clip_model.eval()
language_model.eval()

# 定义投影层
class ProjectionLayer(torch.nn.Module):
    def __init__(self, clip_dim, lm_dim):
        super(ProjectionLayer, self).__init__()
        self.projection = torch.nn.Linear(clip_dim, lm_dim)

    def forward(self, clip_features):
        return self.projection(clip_features)

# 获取 CLIP 模型的视觉模型隐藏层尺寸
clip_hidden_size = clip_model.vision_model.config.hidden_size

# 获取语言模型的隐藏层尺寸
lm_hidden_size = language_model.config.hidden_size

projection_layer = ProjectionLayer(clip_hidden_size, lm_hidden_size).to(device)

def project_image_features(image):
    inputs = clip_processor(images=image, return_tensors="pt").to(device)
    with torch.no_grad():
        clip_features = clip_model.get_image_features(**inputs)
    projected_features = projection_layer(clip_features)
    return projected_features

def generate_response(image_path, prompt, tokenizer, model, projection_layer, device, max_length=512):
    image = Image.open(image_path)
    image_features = project_image_features(image)
    
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    input_ids = inputs["input_ids"]
    
    # 将图像特征与文本输入结合
    input_ids = torch.cat([image_features, input_ids], dim=1)
    
    # 使用模型生成响应
    with torch.no_grad():
        outputs = model.generate(input_ids, max_length=max_length, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)
    
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

if __name__ == "__main__":
    print("与 Vicuna 模型对话。输入 'exit' 退出。")
    while True:
        user_input = input("你: ")
        if user_input.lower() == "exit":
            break
        
        response = generate_response("/home/cs2916_t1/b8bd61e5dd7c9f2290c2b3df273554dc.png", user_input, tokenizer, language_model, projection_layer, device)
        print(f"Vicuna: {response}")
