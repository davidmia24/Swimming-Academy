from datetime import date

from sqlmodel import Field, SQLModel, UniqueConstraint


class Categoria(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nombre: str = Field(unique=True)
    edad_min: int
    edad_max: int | None = None  # None = sin límite (adultos)
    cupo_maximo: int


class Nivel(SQLModel, table=True):
    __table_args__ = (UniqueConstraint("categoria_id", "numero"),)

    id: int | None = Field(default=None, primary_key=True)
    categoria_id: int = Field(foreign_key="categoria.id")
    numero: int
    nombre: str


class AcudienteBase(SQLModel):
    nombre: str
    documento: str = Field(unique=True, index=True)
    telefono: str
    email: str | None = None
    parentesco: str


class Acudiente(AcudienteBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class AcudienteCreate(AcudienteBase):
    pass


class AcudientePublic(AcudienteBase):
    id: int


class AcudienteUpdate(SQLModel):
    nombre: str | None = None
    telefono: str | None = None
    email: str | None = None
    parentesco: str | None = None


class Instructor(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nombre: str
    documento: str = Field(unique=True, index=True)
    telefono: str
    email: str | None = None


class Alumno(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nombre: str
    documento: str = Field(unique=True, index=True)
    fecha_nacimiento: date
    telefono: str | None = None
    acudiente_id: int | None = Field(default=None, foreign_key="acudiente.id")
    nivel_actual_id: int = Field(foreign_key="nivel.id")
