from workout_api.contrib.models import BaseModel

from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship, mapped_column, Mapped


class CentroTreinamentoModel(BaseModel):
    __tablename__ = "centros_treinamento"

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    endereco: Mapped[str] = mapped_column(String(60), nullable=False)
    proprietario: Mapped[int] = mapped_column(String(30), nullable=False)

    atleta: Mapped["AtletaModel"] = relationship(back_populates="centro_treinamento")  # type: ignore
