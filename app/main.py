from fastapi import FastAPI

# Create FastAPI app instance
app = FastAPI()

# Root endpoint
@app.get("/")
async def read_root():
    return {"message": "Hello, World"}
