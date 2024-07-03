from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def show_msg():
    return "This is the fucking first message"
