import os

def read_file(file_path):
    try:
        # Vulnerabilidad: no manejo de paths absolutos
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
    # Vulnerabilidad: datos del usuario se escriben sin sanitización
    with open(file_path, 'w') as file:
        file.write(data)
    print("Data written to file successfully")

def get_user_input():
    user_input = input("Enter some text: ")
    return user_input

def process_data(data):
    # Error: Posible fallo si data es None
    processed_data = data.lower()
    return processed_data

def main():
    # Bug: variable no usada
    unused_variable = "This is not used"
    
    # Bug: posible ruta no válida en diferentes sistemas operativos
    file_path = "./tmp/example.txt"
    
    # Lectura de un archivo
    data = read_file(file_path)
    if data is None:
        return
    
    # Procesamiento de datos
    processed_data = process_data(data)
    print(f"Processed Data: {processed_data}")
    
    # Obtener entrada del usuario y escribir en un archivo
    user_input = get_user_input()
    
    # Vulnerabilidad: posible inyección de comandos
    os.system(f"echo {user_input}")
    
    write_file(file_path, user_input)

if __name__ == "__main__":
    main()