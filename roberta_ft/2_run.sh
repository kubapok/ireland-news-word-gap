#if [ -z ${CUDA_VISIBLE_DEVICES+x} ]; then echo "CUDA_VISIBLE_DEVICES NOT SET"; exit 1 ; else echo "using cuda devices '$CUDA_VISIBLE_DEVICES'"; fi

python run_mlm.py \
    --model_name_or_path roberta-base \
    --max_seq_length 64 \
    --output_dir ./robertamodel \
    --train_file ./train_in.csv \
    --validation_file ./dev-0_in.csv \
    --do_train \
    --do_eval \
    --per_device_train_batch_size=32 \
    --per_device_eval_batch_size=32  \
    --gradient_accumulation_steps=8 \
    --fp16 False \
    --save_steps 1000 \
    --eval_steps 1000 \
    --logging_steps 1000 \
    --evaluation_strategy steps \
    --num_train_epochs 200 \
    --warmup_steps 1000 \
    | tee --append logs_regular.txt
