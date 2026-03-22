from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase, Session
import os

app = FastAPI()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://usuario:password@db:5432/tareas_db")
engine = create_engine(DATABASE_URL)

class Base(DeclarativeBase):
    pass

class Tarea(Base):
    __tablename__ = "tareas"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)

Base.metadata.create_all(bind=engine)

@app.get("/")
def inicio():
    return {"mensaje": "API de tareas funcionando 🚀"}

@app.get("/tareas")
def listar_tareas():
    with Session(engine) as session:
        tareas = session.query(Tarea).all()
        return {"tareas": [{"id": t.id, "titulo": t.titulo} for t in tareas]}

@app.post("/tareas")
def crear_tarea(titulo: str):
    with Session(engine) as session:
        tarea = Tarea(titulo=titulo)
        session.add(tarea)
        session.commit()
        session.refresh(tarea)
        return {"mensaje": f"Tarea '{titulo}' creada", "id": tarea.id}