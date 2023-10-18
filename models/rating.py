from sqlalchemy import Table, Column,ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String,Numeric
from sqlalchemy.orm import relationship
from config.db import engine, meta_data

ratings = Table("ratings", meta_data,
                Column("id",Integer, primary_key=True),
                Column("rating", Numeric(precision=10,scale=2),nullable=False),
                Column("contador", Integer))

meta_data.create_all(engine)