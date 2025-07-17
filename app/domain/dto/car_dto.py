from pydantic import BaseModel, Field


class CarDTO(BaseModel):
    marca: str
    modelo: str
    ano: int = Field(..., gt=1900, lt=2100)
    combustivel: str
    motorizacao: str
    quilometragem: int = Field(..., ge=0)
    portas: int = Field(..., ge=2, le=5)
    transmissao: str
    cor: str
    preco: float = Field(..., ge=0)
    tipo_carroceria: str
    placa: str
    revisao: str

    class Config:
        from_attributes = True
