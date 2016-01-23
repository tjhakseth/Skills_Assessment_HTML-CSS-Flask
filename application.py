from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""

    return render_template("index.html")

@app.route("/application_form")
def application_form_page():
    """Shows the application form"""

    return render_template("application-form.html")

@app.route("/application", methods=["POST"])
def submission_page():
    """Shows the submission page with message"""

    first = request.form.get("firstname")
    last = request.form.get("lastname")
    salary_req = request.form.get("salary")
    job_selection = request.form.get("job")

    return render_template("application-response.html",
                            firstname=first,
                            lastname=last,
                            salary=salary_req,
                            job=job_selection)



if __name__ == "__main__":
    app.run(debug=True)
