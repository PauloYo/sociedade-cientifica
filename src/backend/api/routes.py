from fastapi import APIRouter
from src.backend.api.controller.DoadorController import DoadorController

doadorController = DoadorController()

router = APIRouter()

@router.get("/")
def read_root():
    return {"Hello": "World"}

@router.get("/doador")
def getDoador():
    return {'response': doadorController.findOne()}