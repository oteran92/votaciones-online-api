from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/ciudadano', methods=['POST'])
def add_ciudadano():
    # Lógica para añadir ciudadano
    pass

# Define otras rutas aquí
