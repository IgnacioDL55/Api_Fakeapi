from fastapi import APIRouter,Depends
from schema.products_schema import schema_products
from config.db import conn,engine,SessionLocal
from models.product import products
from sqlalchemy.orm import sessionmaker


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


user = APIRouter()

@user.get("/")
def main():
    return {"message":"Hola mundito"}


@user.post("/api/productos")
def create_persona(data_producto: schema_products, db: SessionLocal = Depends(get_db)):
    try:
        new_producto = data_producto.dict()
        db.execute(products.insert().values(new_producto))
        db.commit()
        return {"message": "Producto creado exitosamente"}
    except Exception as e:
        db.rollback()  # Deshacer la transacción en caso de error
    finally:
        db.close()  # Asegurarse de cerrar la sesión después de usarla
