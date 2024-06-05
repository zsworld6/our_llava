import os
conversation_dir = "/data2/cs2916_t1/ourllava/our_llava/data_gen/example/prompts/conversation"
# List to store fewshot samples
fewshot_samples = []

# Get all files in the directory
files = sorted(os.listdir(conversation_dir))

# Filter out only caps and conv files and ensure they are paired
caps_files = [f for f in files if '_caps.txt' in f]
conv_files = [f for f in files if '_conv.txt' in f]

# Ensure the lists are sorted in the same way
caps_files.sort()
conv_files.sort()

# Check if the number of caps and conv files are the same
if len(caps_files) != len(conv_files):
    raise ValueError("The number of _caps.txt and _conv.txt files do not match.")

# Iterate through the paired files and read the content
for caps_file, conv_file in zip(caps_files, conv_files):
    caps_file_path = os.path.join(conversation_dir, caps_file)
    conv_file_path = os.path.join(conversation_dir, conv_file)
    
    with open(caps_file_path, 'r', encoding='utf-8') as caps_file:
        context = caps_file.read().strip()
    with open(conv_file_path, 'r', encoding='utf-8') as conv_file:
        response = conv_file.read().strip()
    
    fewshot_samples.append({"context": context, "response": response})

# Display the fewshot samples to verify
fewshot_samples



