import torch
from transformers import CLIPProcessor, CLIPModel
from PIL import Image

# 加载预训练的CLIP模型
clip_model = CLIPModel.from_pretrained("openai/clip-vit-large-patch14-336")
clip_processor = CLIPProcessor.from_pretrained("openai/clip-vit-large-patch14-336")

# 设置模型为评估模式
clip_model.eval()

# 示例图像路径
image_path = "/home/cs2916_t1/b8bd61e5dd7c9f2290c2b3df273554dc.png"

# 加载并预处理图像
image = Image.open(image_path)
inputs = clip_processor(images=image, return_tensors="pt")

# 获取图像特征
with torch.no_grad():
    outputs = clip_model.get_image_features(**inputs)

print(outputs)
