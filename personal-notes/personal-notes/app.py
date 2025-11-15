#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Note
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "notes.db")

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_PATH}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = "dev-secret"
    db.init_app(app)

    # --- Add the filter here ---
    import markupsafe

    @app.template_filter("nl2br")
    def nl2br(text):
        if text is None:
            return ""
        escaped = markupsafe.escape(text)
        return markupsafe.Markup(escaped.replace("\n", "<br>"))
    # ----------------------------

    with app.app_context():
        db.create_all()


    @app.route("/")
    def index():
        notes = Note.query.order_by(Note.updated_at.desc()).all()
        return render_template("index.html", notes=notes)

    @app.route("/note/new", methods=["GET", "POST"])
    def new_note():
        if request.method == "POST":
            title = request.form.get("title", "").strip()
            body = request.form.get("body", "").strip()
            if not title:
                flash("Title is required.", "warning")
                return render_template("new.html", title=title, body=body)
            note = Note(title=title, body=body)
            db.session.add(note)
            db.session.commit()
            flash("Note created.", "success")
            return redirect(url_for("index"))
        return render_template("new.html")

    @app.route("/note/<int:note_id>")
    def view_note(note_id):
        note = Note.query.get_or_404(note_id)
        return render_template("view.html", note=note)

    @app.route("/note/<int:note_id>/edit", methods=["GET", "POST"])
    def edit_note(note_id):
        note = Note.query.get_or_404(note_id)
        if request.method == "POST":
            title = request.form.get("title", "").strip()
            body = request.form.get("body", "").strip()
            if not title:
                flash("Title is required.", "warning")
                return render_template("edit.html", note=note)
            note.title = title
            note.body = body
            db.session.commit()
            flash("Note updated.", "success")
            return redirect(url_for("view_note", note_id=note.id))
        return render_template("edit.html", note=note)

    @app.route("/note/<int:note_id>/delete", methods=["POST"])
    def delete_note(note_id):
        note = Note.query.get_or_404(note_id)
        db.session.delete(note)
        db.session.commit()
        flash("Note deleted.", "info")
        return redirect(url_for("index"))

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
