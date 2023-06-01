from datasets import load_dataset, ClassLabel, Dataset
from transformers import AutoTokenizer, DataCollatorWithPadding, \
    AutoModelForSequenceClassification, TrainingArguments, Trainer
import evaluate
import numpy as np
import pandas as pd

# Load dataset and labels
df = pd.read_csv("./BERT/datasets/dataset_twitter.csv", delimiter='|')
df = pd.DataFrame(df)
df = df.dropna() # Remove all None rows
dataset = Dataset.from_pandas(df)
dataset = dataset.train_test_split(test_size=0.2)
labels = ClassLabel(names_file='./BERT/labels.txt')

# Preprocess
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")


def preprocess_function(batch):
    """Preprocessing function to tokenize text and sequences."""
    tokenized_batch = tokenizer(batch['text'], truncation=True)
    tokenized_batch['label'] = labels.str2int(batch['label'])
    return tokenized_batch


tokenized_dataset = dataset.map(preprocess_function, batched=True)

data_collator = DataCollatorWithPadding(tokenizer=tokenizer, padding=True)

# Evaluate
accuracy = evaluate.load("accuracy")


def compute_metrics(eval_pred):
    """Function to calculate the accuracy."""
    predictions, labels = eval_pred
    predictions = np.argmax(predictions, axis=1)
    return accuracy.compute(predictions=predictions, references=labels)


# Train
id2label = {0: "INTJ", 1: "INTP", 2: "ENTJ", 3: "ENTP",
            4: "INFJ", 5: "INFP", 6: "ENFJ", 7: "ENFP",
            8: "ISTJ", 9: "ISFJ", 10: "ESTJ", 11: "ESFJ",
            12: "ISTP", 13: "ISFP", 14: "ESTP", 15: "ESFP"}

label2id = {"INTJ": 0, "INTP": 1, "ENTJ": 2, "ENTP": 3,
            "INFJ": 4, "INFP": 5, "ENFJ": 6, "ENFP": 7,
            "ISTJ": 8, "ISFJ": 9, "ESTJ": 10, "ESFJ": 11,
            "ISTP": 12, "ISFP": 13, "ESTP": 14, "ESFP": 15}

model = AutoModelForSequenceClassification.from_pretrained(
    "distilbert-base-uncased", num_labels=16, id2label=id2label, label2id=label2id
)

training_args = TrainingArguments(
    output_dir="./model",
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=2,
    weight_decay=0.01,
    evaluation_strategy="epoch",
    save_strategy="epoch",
    load_best_model_at_end=True,
    push_to_hub=False,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset["train"],
    eval_dataset=tokenized_dataset["test"],
    tokenizer=tokenizer,
    data_collator=data_collator,
    compute_metrics=compute_metrics,
)

trainer.train()
trainer.save_model("model")
