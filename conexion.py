import psycopg2

try:
    connection = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='password',
        database='postgres'
    )
    print("Conexion exitosa")
    cursor = connection.cursor()
    cursor.execute("SELECT version()")
    row = cursor.fetchone()
    print(row)
except Exception as ex:
    print(ex)
finally:
    if connection:
        connection.close()
        print("Conexión cerrada")