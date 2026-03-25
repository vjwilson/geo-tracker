"""Main FastAPI application"""

from fastapi import FastAPI

from app.api.routes import countries, divisions

app = FastAPI(
    title="Geo Tracker API",
    description="API for tracking geographic information including countries and administrative divisions",
    version="1.0.0"
)

# Include routers
app.include_router(countries.router)
app.include_router(divisions.router)


@app.get("/")
def root():
    """Root endpoint that returns a greeting"""
    return "Hello"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
