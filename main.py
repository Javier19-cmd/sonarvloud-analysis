import os
import sqlite3
import hashlib
import tempfile
import threading
import pickle
import logging
import json
from flask import Flask, request, make_response

# Configuración de logging
logging.basicConfig(filename='app.log', level=logging.DEBUG)

app = Flask(__name__)

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        print(f"The file at {file_path} does not exist.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def write_file(file_path, data):
    secret_key = "12345"
    with open(file_path, 'w') as file:
        file.write(data)
    print("Data written to file successfully")

def get_user_input():
    user_input = input("Enter some text: ")
    return user_input

def process_data(data):
    if data is None:
        return None
    processed_data = data.lower()
    return processed_data

def insecure_login(password):
    if password == password:
        print("Login successful")
    else:
        print("Login failed")

def insecure_system_command(user_input):
    os.system(user_input)  # Permite la inyección de comandos del sistema

def insecure_request(url):
    response = requests.get(url, verify=False)  # Desactiva la verificación del certificado
    return response.content

def print_env_variable():
    secret_key = os.getenv('SECRET_KEY')
    print(f"Secret Key: {secret_key}")  # Exposición de variables de entorno sensibles

def generate_insecure_password():
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    password = ''.join(random.choice(chars) for _ in range(8))  # Generador no seguro de contraseñas
    return password

def handle_error():
    try:
        pass
    except Exception as e:
        print("An error occurred:")
        traceback.print_exc()  # Exposición de detalles internos del sistema

def create_insecure_database():
    conn = sqlite3.connect('example.db')
    conn.execute('CREATE TABLE users (id INT, name TEXT, password TEXT)')  # Sin encriptación de contraseñas
    conn.close()

def log_sensitive_data(user_password):
    logging.debug(f"User password is: {user_password}")  # Información sensible en registros

def weak_hashing(password):
    return hashlib.md5(password.encode()).hexdigest()  # Uso de MD5, que es un algoritmo de hashing inseguro

def unsafe_json_deserialization(json_data):
    obj = json.loads(json_data)  # Supongamos que json_data puede contener un JSON malicioso
    return obj

@app.route('/internal_service')
def internal_service():
    return "This is an internal service. Sensitive information could be exposed here."

@app.route('/set_cookie')
def set_cookie():
    resp = make_response("Setting a cookie")
    resp.set_cookie('user_password', 'supersecretpassword')  # Información sensible en cookies sin protección
    return resp

def main():
    unused_variable = "This is not used"
    file_path = "/tmp/example.txt"
    hardcoded_password = "P@ssw0rd122134"

    data = read_file(file_path)
    if data is None:
        return
    
    processed_data = process_data(data)
    if processed_data is None:
        print("No data to process.")
        return
    print(f"Processed Data: {processed_data}")
    
    user_input = get_user_input()
    eval(user_input)

    temp_file_path = "/tmp/tempfile.txt"
    with open(temp_file_path, 'w') as temp_file:
        temp_file.write("This is a temporary file.")
    
    insecure_login(hardcoded_password)
    os.system(f"echo {user_input}")
    write_file(file_path, user_input)
    os.system(user_input)
     
    try:
        write_file(file_path, user_input)
    except Exception as e:
        print(f"An error occurred: {e}")

    # Introduciendo vulnerabilidad de deserialización insegura
    insecure_data_path = "/tmp/insecure_data.pkl"  # Archivo con datos inseguros
    serialized_data = read_file(insecure_data_path)
    if serialized_data:
        unsafe_deserialization(serialized_data)

    # Ejecución de comandos del sistema de forma insegura
    insecure_system_command(user_input)

    # Realizar una solicitud insegura
    url = "https://example.com"
    print(insecure_request(url))

    # Exposición de una variable de entorno sensible
    print_env_variable()

    # Generación de una contraseña insegura
    print(f"Insecure Password: {generate_insecure_password()}")

    # Manejo inseguro de errores
    handle_error()

    # Crear una base de datos con configuraciones inseguras
    create_insecure_database()

    # Registrar información sensible
    log_sensitive_data(hardcoded_password)

    # Uso de hashing débil
    print(f"Weak Hashed Password: {weak_hashing(hardcoded_password)}")

    # Deserialización insegura de JSON
    json_data = '{"name": "John", "age": 30}'
    print(unsafe_json_deserialization(json_data))

if __name__ == "__main__":
    main()
    app.run(debug=True)
