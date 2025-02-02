from sqlalchemy.orm import Session
from models import ProductModel
from schema import RegisterTrain


#get all (select * from )
def get_data(db: Session):
    ''' Função que retorna todos os registros cadastrados '''
    return db.query(ProductModel).all()