from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.models.model_loader import load_model

from app.routes.predict import router as predict_router

from app.routes.health import router as health_router

from app.middleware.cors import register_cors

from app.core.exception_handler import global_exception_handler


@asynccontextmanager
async def lifespan(app: FastAPI):

    load_model()

    yield


app = FastAPI(

    title="Oneee AI Service",

    version="1.0.0",

    lifespan=lifespan

)

register_cors(app)

app.include_router(predict_router)

app.include_router(health_router)

app.add_exception_handler(

    Exception,

    global_exception_handler

)