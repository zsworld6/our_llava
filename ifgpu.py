import torch

# 检查CUDA是否可用
if torch.cuda.is_available():
    num_gpus = torch.cuda.device_count()
    print(f"系统中有 {num_gpus} 张GPU。")
    for i in range(num_gpus):
        print(f"GPU {i}: {torch.cuda.get_device_name(i)}")
else:
    print("系统中没有可用的GPU。")
