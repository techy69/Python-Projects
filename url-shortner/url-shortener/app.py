#!/usr/bin/env python3
import string, random
from urllib.parse import urlparse
from flask import Flask, render_template, request, redirect, url_for, flash, abort
from models import db, Link, Click
import validators
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "db.sqlite3")

def generate_code(length=6):
    alphabet = string.ascii_letters + string.digits
    return ''.join(random.choices(alphabet, k=length))

def create_unique_code():
    for _ in range(5):
        code = generate_code()
        if not Link.query.filter_by(short_code=code).first():
            return code
    # fallback to a longer code if collisions happen
    while True:
        code = generate_code(length=8)
        if not Link.query.filter_by(short_code=code).first():
            return code

def create_app():
    app = Flask(__name__, static_folder="static", template_folder="templates")
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_PATH}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "dev-secret"
    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.route("/", methods=["GET", "POST"])
    def index():
        if request.method == "POST":
            original = request.form.get("url", "").strip()
            if not original:
                flash("Please provide a URL.", "warning")
                return render_template("index.html", short=None)
            # add scheme if missing
            parsed = urlparse(original)
            if not parsed.scheme:
                original = "http://" + original

            if not validators.url(original):
                flash("That doesn't look like a valid URL.", "danger")
                return render_template("index.html", short=None)

            # Optional: let user suggest custom code
            custom = request.form.get("custom", "").strip()
            if custom:
                if Link.query.filter_by(short_code=custom).first():
                    flash("Custom code already taken.", "danger")
                    return render_template("index.html", short=None)
                code = custom
            else:
                code = create_unique_code()

            link = Link(original_url=original, short_code=code)
            db.session.add(link)
            db.session.commit()
            short_url = url_for("redirect_short", code=code, _external=True)
            return render_template("created.html", short=short_url, original=original)
        return render_template("index.html", short=None)

    @app.route("/<code>")
    def redirect_short(code):
        link = Link.query.filter_by(short_code=code).first_or_404()
        # Log click
        click = Click(
            link_id=link.id,
            referrer=request.referrer,
            user_agent=request.headers.get("User-Agent")
        )
        db.session.add(click)
        db.session.commit()
        return redirect(link.original_url)

    @app.route("/stats/<code>")
    def stats(code):
        link = Link.query.filter_by(short_code=code).first_or_404()
        clicks = link.clicks.order_by(Click.timestamp.desc()).limit(100).all()
        total = link.clicks.count()
        return render_template("stats.html", link=link, clicks=clicks, total=total)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
