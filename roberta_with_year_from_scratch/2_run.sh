#if [ -z ${CUDA_VISIBLE_DEVICES+x} ]; then echo "CUDA_VISIBLE_DEVICES NOT SET"; exit 1 ; else echo "using cuda devices '$CUDA_VISIBLE_DEVICES'"; fi

python run_mlm.py \
    --model_type roberta \
    --config_name roberta_small_config.json \
    --max_seq_length 64 \
    --output_dir ./robertamodel \
    --train_file ./train_in.csv \
    --validation_file ./dev-0_in.csv \
    --do_train \
    --do_eval \
    --per_device_train_batch_size=64 \
    --per_device_eval_batch_size=64  \
    --gradient_accumulation_steps=4 \
    --fp16 False \
    --save_steps 1000 \
    --eval_steps 1000 \
    --logging_steps 1000 \
    --evaluation_strategy steps \
    --num_train_epochs 200 \
    --warmup_steps 1000 \
    --tokenizer_name tokenizer_model \
    | tee --append logs_regular.txt
