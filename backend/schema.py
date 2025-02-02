from pydantic import BaseModel, PositiveFloat, PositiveInt, validators, StrictBool 
from datetime import datetime
from typing import Optional

class RegisterTrain(BaseModel):
    user_treino: str
    peso_user: Optional[PositiveFloat] = None
    fez_dieta: Optional[StrictBool] = False
    tipo_treino: str 
    exercicio_treino: str
    rpe: Optional[PositiveFloat] = None
    qtd_series: PositiveInt
    num_repeticoes: PositiveInt 
    num_kgs: PositiveFloat
    data_treino: datetime 

class TrainCreate(RegisterTrain):
    pass