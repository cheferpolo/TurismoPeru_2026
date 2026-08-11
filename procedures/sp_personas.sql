CREATE OR ALTER PROCEDURE CNPV.sp_ListarPersonas
AS
BEGIN
    SET NOCOUNT ON;

    SELECT
        id_persona,
        tipo_persona,
        nombres,
        apaterno,
        amaterno,
        estado
    FROM CNPV.persona;
END;
GO


CREATE OR ALTER PROCEDURE CNPV.sp_ListarClientes
AS
BEGIN
    SET NOCOUNT ON;

    SELECT
        p.id_persona,
        p.tipo_persona,
        p.nombres,
        p.apaterno,
        p.amaterno,
        p.estado
    FROM CNPV.persona AS p
    INNER JOIN CNPV.cliente AS c
        ON p.id_persona = c.id_persona;
END;
GO


CREATE OR ALTER PROCEDURE CNPV.sp_insertarPersona
    @tipo_persona VARCHAR(1),
    @nombres VARCHAR(100),
    @apaterno VARCHAR(100),
    @amaterno VARCHAR(100),
    @razon_social VARCHAR(150),
    @nombre_comercial VARCHAR(150),
    @id_tipo_documento INT,
    @numero_documento VARCHAR(20),
    @telefono VARCHAR(15),
    @email VARCHAR(100),
    @id_nacionalidad INT,
    @estado VARCHAR(20)
AS
BEGIN
    SET NOCOUNT ON;

    BEGIN TRY
        INSERT INTO CNPV.persona (
            tipo_persona,
            nombres,
            apaterno,
            amaterno,
            razon_social,
            nombre_comercial,
            id_tipo_documento,
            numero_documento,
            telefono,
            email,
            id_nacionalidad,
            estado
        )
        VALUES (
            @tipo_persona,
            @nombres,
            @apaterno,
            @amaterno,
            @razon_social,
            @nombre_comercial,
            @id_tipo_documento,
            @numero_documento,
            @telefono,
            @email,
            @id_nacionalidad,
            @estado
        );

        PRINT 'Persona registrada correctamente';
    END TRY
    BEGIN CATCH
        THROW;
    END CATCH
END;
GO