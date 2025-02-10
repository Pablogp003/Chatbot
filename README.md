# Chatbot Asistente de Desarrollo de Software

## Descripción
Este es un chatbot diseñado para asistir en el desarrollo de software. Utiliza el modelo GPT-2 para la generación de texto y permite a los usuarios hacer preguntas relacionadas con desarrollo de software. Además, tiene la capacidad de extraer texto de archivos PDF para proporcionar respuestas basadas en documentos subidos por el usuario.

## Tecnologías utilizadas
- **Python**
- **Streamlit** (Interfaz web)
- **Transformers (Hugging Face)** (Generación de texto con GPT-2)
- **PyMuPDF (Fitz)** (Extracción de texto de PDF)
- **Logging** (Registro de interacciones)

## Funcionalidades
- **Interfaz web sencilla con Streamlit**.
- **Capacidad para cargar archivos PDF y extraer su contenido**.
- **Generación de respuestas utilizando un modelo de lenguaje preentrenado**.
- **Registro de interacciones en un archivo de log para monitoreo**.

## Instalación y ejecución
```bash
# Clona este repositorio
git clone https://github.com/Pablogp003/Chatbot.git
cd Chatbot

# Instala las dependencias necesarias
pip install streamlit transformers pymupdf
```
# Ejecuta la aplicación
streamlit run ChatbotAsistente.py
