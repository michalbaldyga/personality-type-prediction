from datasets import load_dataset
from transformers import AutoTokenizer, DataCollatorWithPadding

# Load dataset
dataset = load_dataset("json", data_files="dataset.json")

# Preprocess
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")


def preprocess_function(examples):
    """Preprocessing function to tokenize text and sequences"""
    return tokenizer(examples["text"], truncation=True)


tokenized_dataset = dataset.map(preprocess_function, batched=True)

data_collator = DataCollatorWithPadding(tokenizer=tokenizer)
