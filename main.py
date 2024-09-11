import sys
import os

print("Python version:", sys.version)
print("Current working directory:", os.getcwd())
print("Contents of current directory:", os.listdir())

try:
    from fastapi import FastAPI, File, UploadFile
    print("FastAPI imported successfully")
except ImportError as e:
    print("Error importing FastAPI:", str(e))
    print("Python path:", sys.path)

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

