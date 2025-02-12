from flask import Flask  

# Crear instancia
app = Flask(__name__)   

# Ruta raíz
@app.route('/')
def hola_mundo():
    return 'Hola Mundo'

if __name__ == '__main__':
    app.run(debug=True)