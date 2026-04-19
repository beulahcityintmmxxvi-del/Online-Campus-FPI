from flask import Blueprint, render_template, request, redirect, url_for, flash
from extensions import db
from models.report import Report
from ml.svm_classifier import classify_incident

import uuid

report_bp = Blueprint("report_bp", __name__, url_prefix="/report")

@report_bp.route("/", methods=["GET", "POST"])
def report():
    if request.method == "POST":
        description = request.form.get("description")

        # AI prediction
        predicted_severity, risk_score = classify_incident(description)

        report = Report(
            tracking_code=f"UNISAFE-{uuid.uuid4().hex[:6].upper()}",
            incident_type=request.form.get("incident_type"),
            description=description,
            predicted_severity=predicted_severity,
            risk_score=risk_score
        )

        db.session.add(report)
        db.session.commit()

        flash(
            f"Report submitted successfully. Tracking Code: {report.tracking_code}",
            "success"
        )
        return redirect(url_for("track_bp.track"))

    return render_template("report.html")
