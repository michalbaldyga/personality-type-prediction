from transformers import pipeline

classifier = pipeline("text-classification", model="../model", tokenizer="distilbert-base-uncased", framework="pt")

text = "Feeling sensitivity of disposition is the sign of a good heart."

print(classifier(text))

