from flask import Flask, render_template
import cloudinary
import cloudinary.api

app = Flask(__name__)

# ------------------------------
# CLOUDINARY CONFIG
# ------------------------------
cloudinary.config(
   cloud_name="dimzggmbt",
    api_key="489628589741893",
    api_secret="JQobGgRo8AXD6qM35zogNgy0BfA"
)

# ------------------------------
# HOME PAGE
# ------------------------------
@app.route("/")
def home():
    return render_template("login.html")


# ------------------------------
# GALLERY PAGE
# ------------------------------
@app.route("/gallery")
def gallery():

    # Fetch all images stored in Cloudinary folder "snapshots/"
    result = cloudinary.api.resources(
        type="upload",
        prefix="snapshots/",
        max_results=500
    )

    # Extract only the secure image URLs
    images = [item["secure_url"] for item in result["resources"]]

    return render_template("gallery.html", images=images)


if __name__ == "__main__":
    app.run(debug=True)
