from flask import Flask, render_template
import psycopg2
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
from io import BytesIO
import base64

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

@app.route('/grafico')
def grafico():
    connection = connect_to_database()

    if connection:
        try:
            cursor = connection.cursor()

            # Consulta para obtener los nombres de los clientes y los resultados de las preguntas
            # Consulta para obtener los nombres de los clientes y los resultados de las preguntas
            # Consulta para obtener los nombres de los clientes y los resultados de las preguntas
            # Consulta para obtener los nombres de los clientes y los resultados de las preguntas
            # Consulta para obtener los nombres de los clientes y los resultados de las preguntas
            # Consulta para obtener los nombres de los clientes y los resultados de las preguntas
            query = """
                SELECT cliente, pregunta1, pregunta2, pregunta3, pregunta4, pregunta5, pregunta6, pregunta7, pregunta8, pregunta9, pregunta10
                FROM clienteencu
            """

            cursor.execute(query)
            data = cursor.fetchall()

            # Convertir los valores de las preguntas a enteros
            data_numeric = [[row[0]] + [int(value) for value in row[1:]] for row in data]

            # Calcular la cantidad total de respuestas
            cantidad_respuestas = len(data_numeric)
            # Calcular la suma de cada pregunta
            sumas_preguntas = [sum(row[i] for row in data_numeric) for i in range(1, 11)]


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
             # Calcular la cantidad de clientes
             # Calcular la cantidad de clientes
            
            cantidad_clientes = len(data)
            # Calcular la cantidad total de respuestas
            cantidad_respuestas = len(data)
            
            porcentajes_preguntas = [(suma / cantidad_respuestas) * (100 / 10) for suma in sumas_preguntas]
            # Crear el gráfico
            preguntas = [f'Pregunta {i+1}' for i in range(10)]
            plt.figure(figsize=(10, 6))
            bars = plt.bar(preguntas, porcentajes_preguntas, color='tomato')
            # Agregar etiquetas con los porcentajes
            for bar, porcentaje in zip(bars, porcentajes_preguntas):
                plt.text(bar.get_x() + bar.get_width() / 2 - 0.15, bar.get_height() + 0.5,
                        f'{porcentaje:.2f}%', ha='center', color='black')
                
            plt.title('Porcentaje de Acuerdo a Todas las Preguntas')
            plt.xlabel('Preguntas')
            plt.ylabel('Porcentaje')
            plt.xticks(rotation=45, ha='right')
            plt.yticks(range(0, 101, 20))
            plt.ylim(0, 100)

            # Convertir el gráfico a una imagen base64
            buffer = BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            imagen_base64 = base64.b64encode(buffer.getvalue()).decode()

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

            # Obtener los valores reales de las preguntas por cliente
            valores_pregunta1 = [max(1, min(10, row[1])) for row in data]
            valores_pregunta2 = [max(1, min(10, row[2])) for row in data]
            valores_pregunta3 = [max(1, min(10, row[3])) for row in data]
            valores_pregunta4 = [max(1, min(10, row[4])) for row in data]
            valores_pregunta5 = [max(1, min(10, row[5])) for row in data]
            valores_pregunta6 = [max(1, min(10, row[6])) for row in data]
            valores_pregunta7 = [max(1, min(10, row[7])) for row in data]
            valores_pregunta8 = [max(1, min(10, row[8])) for row in data]
            valores_pregunta9 = [max(1, min(10, row[9])) for row in data]
            valores_pregunta10= [max(1, min(10, row[10])) for row in data]


            

            # Crear el gráfico para la pregunta 1
            clientes = [row[0] for row in data]
            porcentajes_pregunta1 = [(valor / 10) * 100 for valor in valores_pregunta1]

            plt.figure(figsize=(8, 6))
            plt.bar(clientes, porcentajes_pregunta1, color='lightcoral')
            plt.title('Porcentaje de Acuerdo a Pregunta 1 por Cliente')
            plt.xlabel('Clientes')
            plt.ylabel('Porcentaje')
            plt.xticks(rotation=45, ha='right')
            plt.yticks(range(0, 101, 20))
            plt.ylim(0, 100)

            # Convertir el gráfico a una imagen base64
            buffer_pregunta1 = BytesIO()
            plt.savefig(buffer_pregunta1, format='png')
            buffer_pregunta1.seek(0)
            imagen_base64_pregunta1 = base64.b64encode(buffer_pregunta1.getvalue()).decode()

            # Crear el gráfico para la pregunta 2
            porcentajes_pregunta2 = [(valor / 10) * 100 for valor in valores_pregunta2]

            plt.figure(figsize=(8, 6))
            plt.bar(clientes, porcentajes_pregunta2, color='skyblue')
            plt.title('Porcentaje de Acuerdo a Pregunta 2 por Cliente')
            plt.xlabel('Clientes')
            plt.ylabel('Porcentaje')
            plt.xticks(rotation=45, ha='right')
            plt.yticks(range(0, 101, 20))
            plt.ylim(0, 100)

            # Convertir el gráfico a una imagen base64
            buffer_pregunta2 = BytesIO()
            plt.savefig(buffer_pregunta2, format='png')
            buffer_pregunta2.seek(0)
            imagen_base64_pregunta2 = base64.b64encode(buffer_pregunta2.getvalue()).decode()

            # Crear el gráfico para la pregunta 3
            porcentajes_pregunta3 = [(valor / 10) * 100 for valor in valores_pregunta3]

            plt.figure(figsize=(8, 6))
            plt.bar(clientes, porcentajes_pregunta3, color='lightgreen')
            plt.title('Porcentaje de Acuerdo a Pregunta 3 por Cliente')
            plt.xlabel('Clientes')
            plt.ylabel('Porcentaje')
            plt.xticks(rotation=45, ha='right')
            plt.yticks(range(0, 101, 20))
            plt.ylim(0, 100)

            # Convertir el gráfico a una imagen base64
            buffer_pregunta3 = BytesIO()
            plt.savefig(buffer_pregunta3, format='png')
            buffer_pregunta3.seek(0)
            imagen_base64_pregunta3 = base64.b64encode(buffer_pregunta3.getvalue()).decode()

            # Crear el gráfico para la pregunta 4
            porcentajes_pregunta4 = [(valor / 10) * 100 for valor in valores_pregunta4]

            plt.figure(figsize=(8, 6))
            plt.bar(clientes, porcentajes_pregunta4, color='orange')
            plt.title('Porcentaje de Acuerdo a Pregunta 4 por Cliente')
            plt.xlabel('Clientes')
            plt.ylabel('Porcentaje')
            plt.xticks(rotation=45, ha='right')
            plt.yticks(range(0, 101, 20))
            plt.ylim(0, 100)

            # Convertir el gráfico a una imagen base64
            buffer_pregunta4 = BytesIO()
            plt.savefig(buffer_pregunta4, format='png')
            buffer_pregunta4.seek(0)
            imagen_base64_pregunta4 = base64.b64encode(buffer_pregunta4.getvalue()).decode()

            # Crear el gráfico para la pregunta 5
            porcentajes_pregunta5 = [(valor / 10) * 100 for valor in valores_pregunta5]

            plt.figure(figsize=(8, 6))
            plt.bar(clientes, porcentajes_pregunta5, color='purple')
            plt.title('Porcentaje de Acuerdo a Pregunta 5 por Cliente')
            plt.xlabel('Clientes')
            plt.ylabel('Porcentaje')
            plt.xticks(rotation=45, ha='right')
            plt.yticks(range(0, 101, 20))
            plt.ylim(0, 100)

            # Convertir el gráfico a una imagen base64
            buffer_pregunta5 = BytesIO()
            plt.savefig(buffer_pregunta5, format='png')
            buffer_pregunta5.seek(0)
            imagen_base64_pregunta5 = base64.b64encode(buffer_pregunta5.getvalue()).decode()


            # Crear el gráfico para la pregunta 6
            porcentajes_pregunta6 = [(valor / 10) * 100 for valor in valores_pregunta6]

            plt.figure(figsize=(8, 6))
            plt.bar(clientes, porcentajes_pregunta6, color='tomato')
            plt.title('Porcentaje de Acuerdo a Pregunta 6 por Cliente')
            plt.xlabel('Clientes')
            plt.ylabel('Porcentaje')
            plt.xticks(rotation=45, ha='right')
            plt.yticks(range(0, 101, 20))
            plt.ylim(0, 100)

            # Convertir el gráfico a una imagen base64
            buffer_pregunta6 = BytesIO()
            plt.savefig(buffer_pregunta6, format='png')
            buffer_pregunta6.seek(0)
            imagen_base64_pregunta6 = base64.b64encode(buffer_pregunta6.getvalue()).decode()

            # Crear el gráfico para la pregunta 7
            porcentajes_pregunta7 = [(valor / 10) * 100 for valor in valores_pregunta7]

            plt.figure(figsize=(8, 6))
            plt.bar(clientes, porcentajes_pregunta7, color='mediumpurple')
            plt.title('Porcentaje de Acuerdo a Pregunta 7 por Cliente')
            plt.xlabel('Clientes')
            plt.ylabel('Porcentaje')
            plt.xticks(rotation=45, ha='right')
            plt.yticks(range(0, 101, 20))
            plt.ylim(0, 100)

            # Convertir el gráfico a una imagen base64
            buffer_pregunta7 = BytesIO()
            plt.savefig(buffer_pregunta7, format='png')
            buffer_pregunta7.seek(0)
            imagen_base64_pregunta7 = base64.b64encode(buffer_pregunta7.getvalue()).decode()

            # Crear el gráfico para la pregunta 8
            porcentajes_pregunta8 = [(valor / 10) * 100 for valor in valores_pregunta8]

            plt.figure(figsize=(8, 6))
            plt.bar(clientes, porcentajes_pregunta8, color='mediumseagreen')
            plt.title('Porcentaje de Acuerdo a Pregunta 8 por Cliente')
            plt.xlabel('Clientes')
            plt.ylabel('Porcentaje')
            plt.xticks(rotation=45, ha='right')
            plt.yticks(range(0, 101, 20))
            plt.ylim(0, 100)

            # Convertir el gráfico a una imagen base64
            buffer_pregunta8 = BytesIO()
            plt.savefig(buffer_pregunta8, format='png')
            buffer_pregunta8.seek(0)
            imagen_base64_pregunta8 = base64.b64encode(buffer_pregunta8.getvalue()).decode()

            # Crear el gráfico para la pregunta 9
            porcentajes_pregunta9 = [(valor / 10) * 100 for valor in valores_pregunta9]

            plt.figure(figsize=(8, 6))
            plt.bar(clientes, porcentajes_pregunta9, color='darkorange')
            plt.title('Porcentaje de Acuerdo a Pregunta 9 por Cliente')
            plt.xlabel('Clientes')
            plt.ylabel('Porcentaje')
            plt.xticks(rotation=45, ha='right')
            plt.yticks(range(0, 101, 20))
            plt.ylim(0, 100)

            # Convertir el gráfico a una imagen base64
            buffer_pregunta9 = BytesIO()
            plt.savefig(buffer_pregunta9, format='png')
            buffer_pregunta9.seek(0)
            imagen_base64_pregunta9 = base64.b64encode(buffer_pregunta9.getvalue()).decode()

             # Crear el gráfico para la pregunta 10
            porcentajes_pregunta10 = [(valor / 10) * 100 for valor in valores_pregunta10]

            plt.figure(figsize=(8, 6))
            plt.bar(clientes, porcentajes_pregunta10, color='slateblue')
            plt.title('Porcentaje de Acuerdo a Pregunta 10 por Cliente')
            plt.xlabel('Clientes')
            plt.ylabel('Porcentaje')
            plt.xticks(rotation=45, ha='right')
            plt.yticks(range(0, 101, 20))
            plt.ylim(0, 100)

            # Convertir el gráfico a una imagen base64
            buffer_pregunta10 = BytesIO()
            plt.savefig(buffer_pregunta10, format='png')
            buffer_pregunta10.seek(0)
            imagen_base64_pregunta10 = base64.b64encode(buffer_pregunta10.getvalue()).decode()

            return render_template('grafico.html', 
                                   imagen_base64_pregunta1=imagen_base64_pregunta1,
                                   imagen_base64_pregunta2=imagen_base64_pregunta2,
                                   imagen_base64_pregunta3=imagen_base64_pregunta3,
                                   imagen_base64_pregunta4=imagen_base64_pregunta4,
                                   imagen_base64_pregunta5=imagen_base64_pregunta5,
                                   imagen_base64_pregunta6=imagen_base64_pregunta6,
                                   imagen_base64_pregunta7=imagen_base64_pregunta7,
                                   imagen_base64_pregunta8=imagen_base64_pregunta8,
                                   imagen_base64_pregunta9=imagen_base64_pregunta9,
                                   imagen_base64_pregunta10=imagen_base64_pregunta10,
                                   resultado_final=resultado_final,
                                   resultado_final_pregunta2=resultado_final_pregunta2,
                                   resultado_final_pregunta3=resultado_final_pregunta3,
                                   resultado_final_pregunta4=resultado_final_pregunta4,
                                   resultado_final_pregunta5=resultado_final_pregunta5,
                                   resultado_final_pregunta6=resultado_final_pregunta6,
                                   resultado_final_pregunta7=resultado_final_pregunta7,
                                   resultado_final_pregunta8=resultado_final_pregunta8,
                                   resultado_final_pregunta9=resultado_final_pregunta9,
                                   resultado_final_pregunta10=resultado_final_pregunta10,
                                   imagen_base64=imagen_base64)
                                   

        except Exception as ex:
            print(ex)
            return f"Error en la base de datos: {ex}"
        finally:
            close_connection(connection)

    return "Error de conexión a la base de datos."

if __name__ == '__main__':
    app.run(debug=True)