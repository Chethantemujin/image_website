from flask import Flask, render_template, send_from_directory, request, redirect, session
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Required for login sessions

# Login credentials
USERNAME = "admin"
PASSWORD = "1234"

# Folder where images are stored
IMAGE_FOLDER = r"C:\Users\Chethan Kumar\Pictures\pen"


# ---------- LOGIN PAGE ----------
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["username"]
        pw = request.form["password"]

        if user == USERNAME and pw == PASSWORD:
            session["logged_in"] = True
            return redirect("/gallery")
        else:
            return render_template("login.html", error="Invalid username or password")

    return render_template("login.html")


# ---------- GALLERY PAGE ----------
@app.route("/gallery")
def gallery():
    if not session.get("logged_in"):
        return redirect("/")

    # List only image files
    images = [img for img in os.listdir(IMAGE_FOLDER)
              if img.lower().endswith((".jpg", ".jpeg", ".png"))]

    return render_template("gallery.html", images=images)


# ---------- SERVE IMAGES ----------
@app.route("/images/<filename>")
def send_image(filename):
    if not session.get("logged_in"):
        return redirect("/")
    return send_from_directory(IMAGE_FOLDER, filename)


# ---------- LOGOUT ----------
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
