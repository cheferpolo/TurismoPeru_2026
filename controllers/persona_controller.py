from database.conexion import conectar


def insertar_persona(persona):
    conexion = conectar()
    cursor = conexion.cursor()

    sql = "{CALL CNPV.sp_insertarPersona (?,?,?,?,?,?,?,?,?,?,?,?)}"

    parametros = (
        persona.tipo_persona,
        persona.nombres,
        persona.apaterno,
        persona.amaterno,
        persona.razon_social,
        persona.nombre_comercial,
        persona.id_tipo_documento,
        persona.numero_documento,
        persona.telefono,
        persona.email,
        persona.id_nacionalidad,
        persona.estado,
    )

    try:
        cursor.execute(sql, *parametros)
        conexion.commit()
        print("Inserción exitosa")
    finally:
        cursor.close()
        conexion.close()