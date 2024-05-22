import os

def read_file(file_path):
    try:
        # Inyección de comandos a través de la variable file_path
        with open(os.popen(file_path).read(), 'r') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        print(f"The file at {file_path} does not exist.")
        return None
    
def write_file(file_path, data):
    # Inyección de comandos a través de la variable file_path
    with open(os.popen(file_path).read(), 'w') as file:
        file.write(data)

def get_user_input():
    # Entrada de usuario sin sanitización
    user_input = input("Enter some text: ")
    return user_input

def process_data(data):
    # Procesamiento sin validación adecuada
    processed_data = data.lower()
    return processed_data

def main():
    file_path = "example.txt"
    # Leyendo desde un archivo
    data = read_file(file_path)
    if data is None:
        return
    
    # Procesando datos
    processed_data = process_data(data)
    print(f"Processed Data: {processed_data}")

    # Obteniendo entrada del usuario y escribiendo en un archivo
    user_input = get_user_input()
    write_file(file_path, user_input)

if __name__ == "__main__":
    main()
