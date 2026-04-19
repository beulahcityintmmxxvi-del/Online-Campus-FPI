from flask import Flask
from config import Config
from extensions import db, mail

from routes.public_routes import public_bp
from routes.report_routes import report_bp
from routes.track_routes import track_bp
from routes.admin_routes import admin_bp
from routes.officer_routes import officer_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    mail.init_app(app)

    # register blueprints
    app.register_blueprint(public_bp)
    app.register_blueprint(report_bp)
    app.register_blueprint(track_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(officer_bp)

    with app.app_context():
        db.create_all()

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
