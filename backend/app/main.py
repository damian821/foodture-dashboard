from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.overview import router as overview_router
from app.api.admin import router as admin_router

app = FastAPI(title="Foodture Dashboard API", version="0.2.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://foodture-dashboard-frontend.onrender.com",
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(overview_router)
app.include_router(admin_router)

@app.get("/")
def root():
    return {"ok": True, "service": "Foodture Dashboard API", "docs": "/docs"}
