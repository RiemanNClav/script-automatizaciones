import pyttsx3

def text_to_speech(file_path):
    # Inicializa el motor de texto a voz
    engine = pyttsx3.init()

    # Configura propiedades de voz (opcional)
    engine.setProperty('rate', 200)  # Velocidad del habla (default es 200)
    engine.setProperty('volume', 1)  # Volumen (rango entre 0.0 y 1.0)

    try:
        # Lee el archivo de texto
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        
        # Convertir el texto a voz
        engine.say(text)
        engine.runAndWait()

    except Exception as e:
        print(f"Error al leer el archivo: {e}")

# Especifica la ruta del archivo de texto
file_path = 'texto.txt'

# Llama a la función para convertir texto a voz
text_to_speech(file_path)

