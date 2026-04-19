from flask import Blueprint, render_template

officer_bp = Blueprint("officer_bp", __name__, url_prefix="/officer")

@officer_bp.route("/login")
def login():
    return render_template("officer/login.html")

@officer_bp.route("/dashboard")
def dashboard():
    return render_template("officer/dashboard.html")
