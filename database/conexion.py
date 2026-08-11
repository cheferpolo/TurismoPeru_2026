import pyodbc
from config import SERVER, DATABASE, USERNAME, PASSWORD, DRIVER


def conectar():
    cadena_conexion = (
        f"DRIVER={{{DRIVER}}};"
        f"SERVER={SERVER};"
        f"DATABASE={DATABASE};"
        f"UID={USERNAME};"
        f"PWD={PASSWORD};"
        "Encrypt=yes;"
        "TrustServerCertificate=yes;"
    )

    return pyodbc.connect(cadena_conexion)