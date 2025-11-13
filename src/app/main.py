# src/app/main.py
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from src.app.api import predict, health_check

# Create FastAPI instance
app = FastAPI()

# Add /predict endpoint
@app.post("/predict")
async def prediction(input_data: dict):
    """
    Endpoint for making predictions
    """
    try:
        # Call the predict function from api.py
        result = await predict(input_data)
        return JSONResponse(content=result, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)

# Add /health endpoint
@app.get("/health")
async def health():
    """
    Simple health check endpoint
    """
    return health_check()

