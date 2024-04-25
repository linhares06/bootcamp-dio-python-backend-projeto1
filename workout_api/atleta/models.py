from workout_api.contrib.models import BaseModel

from sqlalchemy import Float, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, mapped_column, Mapped
from datetime import datetime


class AtletaModel(BaseModel):
    __tablename__ = "atletas"

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    cpf: Mapped[str] = mapped_column(String(11), unique=True, nullable=False)
    idade: Mapped[int] = mapped_column(Integer, nullable=False)
    peso: Mapped[float] = mapped_column(Float, nullable=False)
    altura: Mapped[float] = mapped_column(Float, nullable=False)
    sexo: Mapped[str] = mapped_column(String(1), nullable=False)
    data_criacao: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    categoria_id: Mapped[int] = mapped_column(ForeignKey("categorias.pk_id"))
    categoria: Mapped["CategoriaModel"] = relationship(back_populates="atleta", lazy="selectin")  # type: ignore

    centro_treinamento_id: Mapped[int] = mapped_column(ForeignKey("centros_treinamento.pk_id"))
    centro_treinamento: Mapped["CentroTreinamentoModel"] = relationship(back_populates="atleta", lazy="selectin")  # type: ignore
