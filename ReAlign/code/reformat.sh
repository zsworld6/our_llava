# export OPENAI_API_KEY=YOUR_OPENAI_KEY

python reformat.py \
    --input_data_path /data2/cs2916_t1/ReAlign/datasets/dataset_retrieval_clean_evidence.json \
    --output_directory reformat_results \
    --tokenizer_path /data2/ckpts/llama3 \
    --dataset_batch_id 0 \
    --dataset_batch_num 1 \
    --openai_key YOUR_OPENAI_KEY \
    --top_k 2 \
    --model gpt-4o \
    --temperature 0.3 \
    --top_p 1 \
    --target_length 4096