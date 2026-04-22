from fastapi import FastAPI
from app.api.routes import router as api_router
from app.api.health import router as health_router
from app.core.exceptions import global_exception_handler

app = FastAPI(
    title="AegisOps AI",
    version="1.0.0",
    description="Autonomous DevSecOps & Cyber Intelligence Platform"
)

# Routers
app.include_router(api_router)
app.include_router(health_router)

# Global Exception Handler
app.add_exception_handler(Exception, global_exception_handler)


@app.get("/")
def root():
    return {
        "status": "success",
        "service": "AegisOps AI Backend",
        "message": "Running successfully"
    }
