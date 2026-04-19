from flask import Blueprint, render_template, request
from models.report import Report

track_bp = Blueprint("track_bp", __name__, url_prefix="/track")

@track_bp.route("/", methods=["GET", "POST"])
def track():
    report = None
    if request.method == "POST":
        code = request.form.get("tracking_code")
        report = Report.query.filter_by(tracking_code=code).first()

    return render_template("track.html", report=report)
