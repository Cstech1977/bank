from fastapi import FastAPI


app = FastAPI(title="my app", description="banking")


app.get("/")


def home():
    return {"message": "Welcome to the NextGen Bank API"}
