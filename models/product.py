from sqlalchemy import Table, Column,ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String,Numeric
from sqlalchemy.orm import relationship
from config.db import engine, meta_data
from .rating import ratings

products = Table("products", meta_data,
                Column("id",Integer, primary_key=True),
                Column("titulo", String(255),nullable=False),
                Column("precio_compra", Numeric(precision=10,scale=2),nullable=False),
                Column("descripcion", String(255)),
                Column("categoria", String(255)),
                Column("url_imagen", String(255)),
                Column("rating_id",Integer,ForeignKey("ratings.id")))

products_ratings = relationship("ratings",back_populates="products")

meta_data.create_all(engine)