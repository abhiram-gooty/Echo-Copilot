from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    return "Welcome to Echo"

@app.get('/upload')
def upload_transcript():
    return "Upload your transcript"