import logging

import os

os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("OneeeAI")

logger.setLevel(logging.INFO)

formatter = logging.Formatter(

    "%(asctime)s | %(levelname)s | %(message)s"

)

file_handler = logging.FileHandler(

    "logs/ai_service.log"

)

file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

console = logging.StreamHandler()

console.setFormatter(formatter)

logger.addHandler(console)