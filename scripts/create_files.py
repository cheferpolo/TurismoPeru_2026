from pathlib import Path

# Carpetas principales del proyecto
carpetas = [
    "database",
    "models",
    "controllers",
    "templates",
    "static",
    "procedures",
]

for carpeta in carpetas:
    ruta = Path.cwd() / carpeta
    ruta.mkdir(parents=True, exist_ok=True)
    print(f"Carpeta '{carpeta}' lista en: {ruta}")