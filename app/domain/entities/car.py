from app.domain.dto.car_dto import CarDTO

class Car:
    """
    Entidade de domínio que representa um automóvel no sistema.
    Contém métodos utilitários para conversão entre entidade e DTO.
    """

    def __init__(
        self,
        marca: str,
        modelo: str,
        ano: int,
        combustivel: str,
        motorizacao: str,
        quilometragem: int,
        portas: int,
        transmissao: str,
        cor: str,
        preco: float,
        tipo_carroceria: str,
        placa: str,
        revisao: str,
    ):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.combustivel = combustivel
        self.motorizacao = motorizacao
        self.quilometragem = quilometragem
        self.portas = portas
        self.transmissao = transmissao
        self.cor = cor
        self.preco = preco
        self.tipo_carroceria = tipo_carroceria
        self.placa = placa
        self.revisao = revisao

    def to_dto(self) -> CarDTO:
        """
        Converte esta entidade para um DTO (Data Transfer Object) CarDTO.
        """
        return CarDTO(
            marca=self.marca,
            modelo=self.modelo,
            ano=self.ano,
            combustivel=self.combustivel,
            motorizacao=self.motorizacao,
            quilometragem=self.quilometragem,
            portas=self.portas,
            transmissao=self.transmissao,
            cor=self.cor,
            preco=self.preco,
            tipo_carroceria=self.tipo_carroceria,
            placa=self.placa,
            revisao=self.revisao,
        )

    @classmethod
    def from_dto(cls, dto: CarDTO) -> "Car":
        """
        Cria uma instância da entidade Car a partir de um DTO.
        """
        return cls(**dto.dict())

    def to_dict(self) -> dict:
        """
        Converte esta entidade para um dicionário simples.
        Útil para debug ou serialização.
        """
        return self.__dict__
