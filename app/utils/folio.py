def generar_folio(ultimo_numero: int) -> str:
    return f"CCADPRC-{str(ultimo_numero + 1).zfill(4)}"
