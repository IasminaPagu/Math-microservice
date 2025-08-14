from fastapi import FastAPI, Depends
from prometheus_fastapi_instrumentator import Instrumentator
from app.controllers.math_operations import router as math_router
from app.db.db import Base, engine
from app.models.db_models import OperationRequest
from app.controllers.auth_controller import router as auth_router


Base.metadata.create_all(bind=engine)
app = FastAPI(title="Math Operations Microservice")
Instrumentator().instrument(app).expose(app)
app.include_router(math_router)
app.include_router(auth_router)
from app.db.db import SessionLocal
from app.services.seed_services import ensure_roles

@app.on_event("startup")
def _seed_roles():
    db = SessionLocal()
    try:
        ensure_roles(db)
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message":"Hello, World"}
