from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///fakeapi.db")

# Definir SessionLocal para el manejo de sesiones de SQLAlchemy
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

conn = engine.connect()

meta_data = MetaData()
