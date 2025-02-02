from database import Base
from sqlalchemy import Column, Integer, Float, String, DateTime, Boolean
from sqlalchemy.sql import func

# O que eu desejo cadastrar?
    # Dados do treino 
    # Dados pessoas (Peso, se treinei ou não treinei, se fiz dieta ou não fiz)

class ProductModel(Base):
    __tablename__ = "treino"
    id:Integer = Column(Integer, primary_key=True)
    user_treino:String = Column(String)
    peso_user: Float = Column(Float)
    fez_dieta: bool = Column(Boolean)
    tipo_treino:String = Column(String)
    exercicio_treino:String = Column(String)
    rpe:float = Column(Float)
    qtd_series:int = Column(Integer)
    num_repeticoes:int = Column(Integer)
    num_kgs:float = Column(Float)
    data_treino: DateTime = Column(DateTime)
    created_at:DateTime = Column(DateTime(timezone=True), 
                                 default=func.now())
