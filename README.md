# Turismo Perú 2026

## Descripción

Aplicación web desarrollada con Flask para listar y registrar personas, además de visualizar clientes desde una base de datos SQL Server.

## Funcionalidades

- Listado de personas.
- Listado de clientes.
- Registro de personas.
- Validación visual ante documentos duplicados.
- Conexión segura a SQL Server mediante variables de entorno.

## Tecnologías

- Python
- Flask
- PyODBC
- SQL Server
- Bootstrap 5
- Git y GitHub

## Estructura del proyecto

```text
TurismoPeru_2026/
├── controllers/
│   ├── listar_controller.py
│   └── persona_controller.py
├── database/
│   └── conexion.py
├── models/
│   ├── cliente.py
│   └── persona.py
├── procedures/
│   └── sp_personas.sql
├── scripts/
│   └── create_files.py
├── static/
├── templates/
│   ├── clientes.html
│   ├── index.html
│   └── insertar.html
├── .env
├── .gitignore
├── app.py
├── config.py
├── README.md
└── requirements.txt
```

## Instalación

1. Crear y activar el entorno virtual:

```bash
python -m venv myenv
source myenv/Scripts/activate
```

2. Instalar las dependencias:

```bash
python -m pip install -r requirements.txt
```

3. Crear el archivo `.env` con las credenciales de conexión.

4. Ejecutar la aplicación:

```bash
python app.py
```

5. Abrir en el navegador:

```text
http://127.0.0.1:5000
```

## Autor

Chefer  
Proyecto desarrollado para el curso de Base de Datos, 2026.