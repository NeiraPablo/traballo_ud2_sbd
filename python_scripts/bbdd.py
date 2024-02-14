def destino(nombre):

    import pymysql

    conexion = pymysql.connect(
        host='193.144.42.124',
        port=33306,
        user='Pablo',
        password='1Super-Password',
        database='inferno'
    )

    with conexion.cursor() as cursor:
        cursor.execute(f"SELECT nivel, nome_nivel FROM admision WHERE nome LIKE '{nombre}'")
        nivel, nome_nivel = cursor.fetchone()
        conexion.close()
    return f'Estás no {nivel}º nivel, o/a {nome_nivel}'
    