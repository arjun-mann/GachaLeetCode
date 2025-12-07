from fastapi import FastAPI
from db import models
from routes.auth import router as auth_router
from routes.users import router as users_router
from routes.rolls import router as rolls_router

models.Base.metadata.creeate_all(bind=engine)
app = FastAPI()
origins = ["http://localhost:5173","http://127.0.0.1:5173"]
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(users_router, prefix="/users", tags=["Users"])
app.include_router(rolls_router, prefix="/rolls", tags=["Rolls"])

@router.get("/health")
def health():
    return {"status" : "ok"}