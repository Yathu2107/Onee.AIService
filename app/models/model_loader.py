import os
import torch

from transformers import (
    DistilBertTokenizer,
    DistilBertForSequenceClassification
)

from app.config import MODEL_PATH, DEVICE

tokenizer = None
model = None


def load_model():

    global tokenizer
    global model

    print("Loading DistilBERT model...")

    tokenizer = DistilBertTokenizer.from_pretrained(MODEL_PATH)

    model = DistilBertForSequenceClassification.from_pretrained(
        MODEL_PATH
    )

    model.to(DEVICE)

    model.eval()

    print("Model loaded successfully.")


def get_model():
    return model


def get_tokenizer():
    return tokenizer