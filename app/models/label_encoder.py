import os
import joblib

from app.config import MODEL_PATH

_encoder = None


def load_label_encoder():
    global _encoder

    if _encoder is None:

        path = os.path.join(
            MODEL_PATH,
            "label_encoder.pkl"
        )

        _encoder = joblib.load(path)

    return _encoder