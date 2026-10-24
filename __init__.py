from blueprints.alumnos.routes import alumnos_bp
from blueprints.maestros.routes import maestro_bp

def registrar_blueprints(app):
    app.registrar_blueprints(alumnos.bp)
    app.registrar_blueprints(maestros.bp)