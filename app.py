from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

def connect_to_database():
    try:
        connection = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='password',
            database='postgres'
        )
        return connection
    except Exception as ex:
        print(ex)
        return None

def close_connection(connection):
    if connection:
        connection.close()

@app.route('/')
def index():
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()

            # Consulta para obtener los nombres de los clientes y los resultados de la pregunta1
            query = """
                SELECT cliente, pregunta1 , pregunta2, pregunta3,  pregunta4, pregunta5,pregunta6,pregunta7,pregunta8,pregunta9,pregunta10,
           (pregunta1 + pregunta2 + pregunta3 + pregunta4 + pregunta5 + pregunta6 + pregunta7 + pregunta8 + pregunta9 + pregunta10) as suma_preguntas
                FROM clienteencu
            """

            cursor.execute(query)
            data = cursor.fetchall()   
            
             # Calcular la suma de las preguntas para cada cliente
            
           

             # Calcular la suma de pregunta1 y pregunta2
             # Calcular la suma de pregunta1 y pregunta2 
            

            # Calcular la suma de pregunta1 y pregunta2
            suma_pregunta1 = sum(row[1] for row in data)
            suma_pregunta2 = sum(row[2] for row in data)
            suma_pregunta3 = sum(row[3] for row in data)
            suma_pregunta4 = sum(row[4] for row in data)
            suma_pregunta5 = sum(row[5] for row in data)
            suma_pregunta6 = sum(row[6] for row in data)
            suma_pregunta7 = sum(row[7] for row in data)
            suma_pregunta8 = sum(row[8] for row in data)
            suma_pregunta9 = sum(row[9] for row in data)
            suma_pregunta10 = sum(row[10] for row in data)
            # Calcular la cantidad de clientes
            cantidad_clientes = len(data)

            

            # Calcular el resultado final y redondearlo
            resultado_final = round((suma_pregunta1 / cantidad_clientes) * (100 / 10), 2)
            resultado_final_pregunta2 = round((suma_pregunta2 / cantidad_clientes) * (100 / 10), 2)
            resultado_final_pregunta3 = round((suma_pregunta3 / cantidad_clientes) * (100 / 10), 2)
            resultado_final_pregunta4 = round((suma_pregunta4 / cantidad_clientes) * (100 / 10), 2)
            resultado_final_pregunta5 = round((suma_pregunta5 / cantidad_clientes) * (100 / 10), 2)
            resultado_final_pregunta6 = round((suma_pregunta6 / cantidad_clientes) * (100 / 10), 2)
            resultado_final_pregunta7 = round((suma_pregunta7 / cantidad_clientes) * (100 / 10), 2)
            resultado_final_pregunta8 = round((suma_pregunta8 / cantidad_clientes) * (100 / 10), 2)
            resultado_final_pregunta9 = round((suma_pregunta9 / cantidad_clientes) * (100 / 10), 2)
            resultado_final_pregunta10 = round((suma_pregunta10 / cantidad_clientes) * (100 / 10), 2)
            

            

            
            return render_template('index.html', data=data, resultado_final=resultado_final, resultado_final_pregunta2=resultado_final_pregunta2,resultado_final_pregunta3=resultado_final_pregunta3,resultado_final_pregunta4=resultado_final_pregunta4,resultado_final_pregunta5=resultado_final_pregunta5,
                                   resultado_final_pregunta6=resultado_final_pregunta6 ,resultado_final_pregunta7=resultado_final_pregunta7,resultado_final_pregunta8=resultado_final_pregunta8,
                                    resultado_final_pregunta9=resultado_final_pregunta9,resultado_final_pregunta10=resultado_final_pregunta10
                       )
        

        except Exception as ex:
            print(ex)
            return f"Error en la base de datos: {ex}"
        finally:
            close_connection(connection)

    return "Error de conexión a la base de datos."

if __name__ == '__main__':
    app.run(debug=True)