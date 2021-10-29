from pathlib import Path
from tokenizers import ByteLevelBPETokenizer

paths = ['../train/in_text_only.csv']

# Initialize a tokenizer
tokenizer = ByteLevelBPETokenizer()

# Customize training
tokenizer.train(files=paths, vocab_size=50265, min_frequency=2, special_tokens=[
    "<s>",
    "<pad>",
    "</s>",
    "<unk>",
    "<mask>",
])

tokenizer.save_model("./tokenizer_model")
