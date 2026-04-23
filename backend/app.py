from flask import Flask, request, jsonify, session
from flask_cors import CORS
import pymysql
import os
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

app = Flask(__name__)
app.secret_key = "num_secret_123"
CORS(app, supports_credentials=True)

def get_db():
    return pymysql.connect(
        host=os.environ.get("DB_HOST", "localhost"),
        user=os.environ.get("DB_USER", "num_user"),
        password=os.environ.get("DB_PASSWORD", "num_pass"),
        database=os.environ.get("DB_NAME", "num_db"),
        cursorclass=pymysql.cursors.DictCursor
    )

def init_db():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS admin (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS introduction (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255),
            content TEXT,
            image_url VARCHAR(500)
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS teachers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            title VARCHAR(100),
            department VARCHAR(100),
            email VARCHAR(150),
            image_url VARCHAR(500)
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS programs (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            degree VARCHAR(50),
            duration VARCHAR(50),
            description TEXT
        )
    """)

    cur.execute("SELECT * FROM admin WHERE username='admin'")
    if not cur.fetchone():
        cur.execute("INSERT INTO admin (username, password) VALUES (%s, %s)",
            ("admin", generate_password_hash("admin123")))

    conn.commit()
    conn.close()

# ── AUTH ──
def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if "admin_id" not in session:
            return jsonify({"error": "Нэвтрэх шаардлагатай"}), 401
        return f(*args, **kwargs)
    return decorated

@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM admin WHERE username=%s", (data["username"],))
    user = cur.fetchone()
    conn.close()
    if user and check_password_hash(user["password"], data["password"]):
        session["admin_id"] = user["id"]
        return jsonify({"message": "ok"})
    return jsonify({"error": "Буруу нэвтрэх мэдээлэл"}), 401

@app.route("/api/logout", methods=["POST"])
def logout():
    session.clear()
    return jsonify({"message": "ok"})

# ── INTRODUCTION ──
@app.route("/api/introduction", methods=["GET"])
def get_intro():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM introduction")
    rows = cur.fetchall()
    conn.close()
    return jsonify(rows)

@app.route("/api/introduction", methods=["POST"])
@login_required
def add_intro():
    data = request.get_json()
    conn = get_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO introduction (title, content, image_url) VALUES (%s, %s, %s)",
        (data["title"], data["content"], data.get("image_url", "")))
    conn.commit()
    conn.close()
    return jsonify({"message": "ok"}), 201

@app.route("/api/introduction/<int:id>", methods=["PUT"])
@login_required
def update_intro(id):
    data = request.get_json()
    conn = get_db()
    cur = conn.cursor()
    cur.execute("UPDATE introduction SET title=%s, content=%s, image_url=%s WHERE id=%s",
        (data["title"], data["content"], data.get("image_url", ""), id))
    conn.commit()
    conn.close()
    return jsonify({"message": "ok"})

@app.route("/api/introduction/<int:id>", methods=["DELETE"])
@login_required
def delete_intro(id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM introduction WHERE id=%s", (id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "ok"})

# ── TEACHERS ──
@app.route("/api/teachers", methods=["GET"])
def get_teachers():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM teachers")
    rows = cur.fetchall()
    conn.close()
    return jsonify(rows)

@app.route("/api/teachers", methods=["POST"])
@login_required
def add_teacher():
    data = request.get_json()
    conn = get_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO teachers (name, title, department, email, image_url) VALUES (%s,%s,%s,%s,%s)",
        (data["name"], data["title"], data["department"], data["email"], data.get("image_url", "")))
    conn.commit()
    conn.close()
    return jsonify({"message": "ok"}), 201

@app.route("/api/teachers/<int:id>", methods=["PUT"])
@login_required
def update_teacher(id):
    data = request.get_json()
    conn = get_db()
    cur = conn.cursor()
    cur.execute("UPDATE teachers SET name=%s, title=%s, department=%s, email=%s, image_url=%s WHERE id=%s",
        (data["name"], data["title"], data["department"], data["email"], data.get("image_url", ""), id))
    conn.commit()
    conn.close()
    return jsonify({"message": "ok"})

@app.route("/api/teachers/<int:id>", methods=["DELETE"])
@login_required
def delete_teacher(id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM teachers WHERE id=%s", (id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "ok"})

# ── PROGRAMS ──
@app.route("/api/programs", methods=["GET"])
def get_programs():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM programs")
    rows = cur.fetchall()
    conn.close()
    return jsonify(rows)

@app.route("/api/programs", methods=["POST"])
@login_required
def add_program():
    data = request.get_json()
    conn = get_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO programs (name, degree, duration, description) VALUES (%s,%s,%s,%s)",
        (data["name"], data["degree"], data["duration"], data["description"]))
    conn.commit()
    conn.close()
    return jsonify({"message": "ok"}), 201

@app.route("/api/programs/<int:id>", methods=["PUT"])
@login_required
def update_program(id):
    data = request.get_json()
    conn = get_db()
    cur = conn.cursor()
    cur.execute("UPDATE programs SET name=%s, degree=%s, duration=%s, description=%s WHERE id=%s",
        (data["name"], data["degree"], data["duration"], data["description"], id))
    conn.commit()
    conn.close()
    return jsonify({"message": "ok"})

@app.route("/api/programs/<int:id>", methods=["DELETE"])
@login_required
def delete_program(id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM programs WHERE id=%s", (id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "ok"})

if __name__ == "__main__":
    import time
    for i in range(10):
        try:
            init_db()
            print("DB ready!")
            break
        except Exception as e:
            print(f"Wait DB... {i+1}/10")
            time.sleep(5)
    app.run(host="0.0.0.0", port=5000, debug=True)
