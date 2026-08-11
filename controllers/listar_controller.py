from database.conexion import conectar


def listarpersonas():
    conexion = conectar()
    cursor = conexion.cursor()

    try:
        cursor.execute("EXEC CNPV.sp_ListarPersonas")
        return cursor.fetchall()
    finally:
        cursor.close()
        conexion.close()


def listarclientes():
    conexion = conectar()
    cursor = conexion.cursor()

    try:
        cursor.execute("EXEC CNPV.sp_ListarClientes")
        return cursor.fetchall()
    finally:
        cursor.close()
        conexion.close()