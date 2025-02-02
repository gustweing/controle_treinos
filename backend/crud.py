from sqlalchemy.orm import Session
from models import ProductModel, ProdutcUser

#get all (select * from )
def get_data(db: Session):
    return db.query(ProductModel).all()