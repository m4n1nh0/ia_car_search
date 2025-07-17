from app.utils.brand_aliases import BRAND_ALIASES


def normalizar_marca(marca_usuario: str) -> str:
    marca_lower = marca_usuario.lower()
    return BRAND_ALIASES.get(marca_lower, marca_usuario)