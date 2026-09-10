from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import BaseBanco, mecanismo_banco, obter_sessao_banco
from app.models import Livro
from app.schemas import LivroCriacao, LivroResposta


BaseBanco.metadata.create_all(bind=mecanismo_banco)

app = FastAPI(
    title="API de Livros",
    version="1.0.0",
    description="API didática para gerenciamento de livros.",
)


@app.post("/livros", response_model=LivroResposta, status_code=201, tags=["Livros"])
def criar_livro(dados_livro: LivroCriacao, sessao_banco: Session = Depends(obter_sessao_banco)):
    novo_livro = Livro(
        titulo=dados_livro.titulo,
        autor=dados_livro.autor,
        ano_publicacao=dados_livro.ano_publicacao,
        disponivel=dados_livro.disponivel,
    )

    sessao_banco.add(novo_livro)
    sessao_banco.commit()
    sessao_banco.refresh(novo_livro)

    return novo_livro