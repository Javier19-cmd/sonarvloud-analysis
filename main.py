import os
import sqlite3
import hashlib
import tempfile
import threading
import traceback


def read_file(file_path):
    try:
        # Vulnerabilidad: No manejo de paths absolutos
        with open(file_path, 'r') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        print(f"The file at {file_path} does not exist.")
        return None
    except Exception as e:
        # Error: Capturar excepciones genéricas
        print(f"An error occurred: {e}")
        return None

def write_file(file_path, data):
    # Hardcoded sensitive information
    secret_key = "12345"  # Ejemplo de información sensible hardcodeada
    # Vulnerabilidad: datos del usuario se escriben sin sanitización
    with open(file_path, 'w') as file:
        file.write(data)
    print("Data written to file successfully")

def get_user_input():
    user_input = input("Enter some text: ")
    return user_input

def process_data(data):
    # Error: Posible fallo si data es None
    if data is None:
        return None
    processed_data = data.lower()
    return processed_data

def insecure_login(password):
    # Vulnerabilidad: comparación de contraseñas sin hash
    if password == password:
        print("Login successful")
    else:
        print("Login failed")

def handle_error():
    try:
        pass
    except Exception as e:
        print("An error occurred:")
        traceback.print_exc()  # Exposición de detalles internos del sistema

def weak_password_hashing(password):
    # Vulnerabilidad: Uso de un algoritmo de hash inseguro
    hashed_password = hashlib.md5(password.encode()).hexdigest()
    return hashed_password

def store_user_credentials(username, password):
    # Hardcoded database credentials
    db_path = "user_credentials.db"
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    # Vulnerabilidad: Uso de un hash débil
    hashed_password = weak_password_hashing(password)
    
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
    connection.commit()
    connection.close()

def main():
    # Bug: variable no usada
    unused_variable = "This is not used"
    
    # Bug: posible ruta no válida en diferentes sistemas operativos
    file_path = "/tmp/example.txt"
    hardcoded_password = "P@ssw0rd122134"  # Hardcoded credentials

    # Lectura de un archivo
    data = read_file(file_path)
    if data is None:
        return
    
    # Procesamiento de datos
    processed_data = process_data(data)
    if processed_data is None:
        print("No data to process.")
        return
    print(f"Processed Data: {processed_data}")
    
    # Obtener entrada del usuario y escribir en un archivo
    user_input = get_user_input()

    # Unrestricted eval usage
    eval(user_input)  # This is dangerous and should be avoided

    # Writing to a potentially insecure temporary file
    temp_file_path = "/tmp/tempfile.txt"
    with open(temp_file_path, 'w') as temp_file:
        temp_file.write("This is a temporary file.")
        # Security risk demonstration
    
    # prueba de contra
    insecure_login(hardcoded_password)

    # Almacenar credenciales de usuario con hash débil
    username = "user1"
    store_user_credentials(username, hardcoded_password)

    # Vulnerabilidad: posible inyección de comandos
    os.system(f"echo {user_input}")

    write_file(file_path, user_input)

    # Command injection
    os.system(user_input)  # Using user input in system command
    
    try:
        write_file(file_path, user_input)
    except Exception as e:
        # Exposing internal errors to the user
        print(f"An error occurred: {e}")  # Improper error handling

if __name__ == "__main__":
    main()
