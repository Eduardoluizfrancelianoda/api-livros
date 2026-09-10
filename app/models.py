from sqlalchemy import Column, Integer, String, Boolean

from app.database import BaseBanco


class Livro(BaseBanco):
    __tablename__ = "livros"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    titulo = Column(String(255), nullable=False)
    autor = Column(String(255), nullable=False)
    ano_publicacao = Column(Integer, nullable=False)
    disponivel = Column(Boolean, nullable=False, default=True)
