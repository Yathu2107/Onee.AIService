import torch

from app.config import MAX_LENGTH, DEVICE
from app.models.model_loader import (
    get_model,
    get_tokenizer
)
from app.models.label_encoder import (
    load_label_encoder
)
from app.utils.preprocessing import clean_text


def predict(text: str):

    text = clean_text(text)

    tokenizer = get_tokenizer()
    model = get_model()
    encoder = load_label_encoder()

    inputs = tokenizer(

        text,

        return_tensors="pt",

        truncation=True,

        padding=True,

        max_length=MAX_LENGTH

    )

    inputs = {
        key: value.to(DEVICE)
        for key, value in inputs.items()
    }

    with torch.no_grad():

        outputs = model(**inputs)

    logits = outputs.logits

    probabilities = torch.softmax(
        logits,
        dim=1
    )

    confidence, predicted = torch.max(
        probabilities,
        dim=1
    )

    label = encoder.inverse_transform(
        [predicted.item()]
    )[0]

    return {

        "category": label,

        "confidence": round(
            confidence.item(),
            4
        )

    }