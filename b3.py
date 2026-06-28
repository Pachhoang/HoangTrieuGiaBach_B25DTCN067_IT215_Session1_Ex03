from fastapi import FastAPI

app = FastAPI()

students = [
    {"id": 1, "name": "An", "status": "active"},
    {"id": 2, "name": "Binh", "status": "inactive"},
    {"id": 3, "name": "Cuong", "status": "active"},
    {"id": 4, "name": "Dung", "status": "pending"}
]

@app.get("/students/active")
def get_active_students():
    # Lọc danh sách sinh viên có trạng thái "active"
    active_students = [
        student for student in students
        if student["status"] == "active"
    ]

    # Nếu không có sinh viên đang học
    if not active_students:
        return {
            "message": "Không có sinh viên đang học",
            "data": []
        }

    # Trả về danh sách sinh viên đang học
    return {
        "message": "Danh sách sinh viên đang học",
        "data": active_students
    }