from . import db

class Ciudadano(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # otros campos...

# Definir otras clases (Empresa, Gobierno, etc.) aquí
