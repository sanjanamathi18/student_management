from flask import Flask, render_template, request, make_response  # abort

app = Flask(__name__)


@app.route("/students")
def students():
    # code to retrive and display all students
    return render_template("students.html", students=student_list)


@app.route("/student/<int:id>")
def specific_student(id):
    # code to show details of a specific student
    return render_template("student_detail.html", student=student)


@app.route("/studentlist")
def student_list():
    return """
        <ul>
        <li>San</li>
        <li>Sanjana</li>
        </ul>
    """


@app.route("/students", methods=["GET"])
def read_students():
    print("Incoming response:", request.headers)
    print("Method:", request.method)
    print("Path:", request.path)
    response = make_response()
    response.headers["X-students-app-headers"] = "I like my students"
    response.set_data("""
        <ul>
            <li>Sanjana</li> 
            <li>San</li>
            <li>Sanju</li>          
        </ul>
    """)
    return response


@app.route("/students", methods=["POST"])
def create_student():
    name = request.form["name"]
    grade = request.form["grade"]
    id = request.form["id"]
    subject = request.form["subject"]
    print("Create student:", name, grade, id, subject)
    return "Created student"


@app.route("/students/<int:id>/edit", methods=["PUT"])
def edit_student(id):
    name = request.form["name"]
    grade = request.form["grade"]
    id = request.form["id"]
    subject = request.form["subject"]
    print(f"/students/{id}")
    print("Update student:", name, grade, id, subject)
    return "Updated student"


@app.route("/student/<int:id>")
def specifik_student(id):
    print("Method:", request.method)
    print("Path:", request.path)
    # data = lookup_in_database(id)
    return f"""
        <h3>Student {id}</h3>
        <p> Sanjana </p>
    """


@app.route("/students/<int:id>/delete", methods=["DELETE"])
def delete_student(id):
    print(f"/students/{id}")
    print("Delete student")
    return "Deleted student"
