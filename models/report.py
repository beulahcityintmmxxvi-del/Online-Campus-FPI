from datetime import datetime
from extensions import db

class Report(db.Model):
    __tablename__ = "reports"

    id = db.Column(db.Integer, primary_key=True)
    tracking_code = db.Column(db.String(20), unique=True, nullable=False)

    incident_type = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)

    predicted_severity = db.Column(db.String(30))
    risk_score = db.Column(db.Integer, default=0)

    status = db.Column(db.String(30), default="Pending")
    progress_note = db.Column(db.Text)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
