import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

from resume_parser import extract_text_from_pdf
from jd_matcher import analyze_resume

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"pdf"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Create uploads folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET", "POST"])
def index():

    result = None
    error = None

    if request.method == "POST":

        # Check file
        if "resume" not in request.files:
            error = "Please upload a resume."
            return render_template("index.html", error=error)

        file = request.files["resume"]
        job_description = request.form.get("job_description", "").strip()

        if file.filename == "":
            error = "Please select a PDF resume."
            return render_template("index.html", error=error)

        if not allowed_file(file.filename):
            error = "Only PDF files are allowed."
            return render_template("index.html", error=error)

        if job_description == "":
            error = "Please enter the Job Description."
            return render_template("index.html", error=error)

        try:
            # Save uploaded resume
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(filepath)

            # Extract resume text
            resume_text = extract_text_from_pdf(filepath)

            if not resume_text.strip():
                error = "Unable to extract text from the resume."
                return render_template("index.html", error=error)

            # AI Analysis
            result = analyze_resume(resume_text, job_description)

            # Optional: Delete uploaded file after processing
            if os.path.exists(filepath):
                os.remove(filepath)

        except Exception as e:
            error = f"Error: {str(e)}"

    return render_template(
        "index.html",
        result=result,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)