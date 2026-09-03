from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


class Configuracoes(BaseSettings):
    db_user: str
    db_password: str = ""
    db_host: str = "localhost"
    db_port: int = 3306
    db_name: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    @field_validator("db_user", "db_password", "db_host", "db_name", mode="before")
    @classmethod
    def limpar_valores_ambiente(cls, valor):
        if isinstance(valor, str):
            return valor.strip().strip('"').strip("'")
        return valor


configuracoes = Configuracoes()

DATABASE_URL = (
    f"mysql+pymysql://{configuracoes.db_user}:{configuracoes.db_password}"
    f"@{configuracoes.db_host}:{configuracoes.db_port}/{configuracoes.db_name}"
)

mecanismo_banco = create_engine(DATABASE_URL, pool_pre_ping=True)
criar_sessao = sessionmaker(bind=mecanismo_banco, autoflush=False, autocommit=False)


class BaseBanco(DeclarativeBase):
    pass