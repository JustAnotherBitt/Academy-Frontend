import flet as ft
import requests

# URL base da API – ajuste conforme necessário
API_BASE_URL = "http://localhost:8000/api"

def main(page: ft.Page):
    page.title = "Academy"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    # Create student tab
    
    name_field = ft.TextField(label="Name")
    email_field = ft.TextField(label="Email")
    belt_field = ft.TextField(label="Belt")
    birth_date_field = ft.TextField(label="Birth Day (YYYY-MM-DD)") 
    create_result = ft.Text()
    
    def create_student_click(e):
        payload = {
		    "name": name_field.value,
		    "email": email_field.value,
		    "belt": belt_field.value,
		    "birth_date": birth_date_field.value,
		}
        
        try:
            response = requests.post(API_BASE_URL + "/", json=payload)
            if response.status_code == 200:
                student = response.json()
                create_result.value = f"Student created: {student}"
            else:
                create_result.value = f"Error: {response.text}"
        except Exception as ex:
            create_result.value = f"Exception: {ex}"
            page.update()
            print(response.json())


    create_button = ft.ElevatedButton(text="Create Student", on_click=create_student_click)


    create_student_tab = ft.Column(
        [
            name_field,
            email_field,
            belt_field,
            birth_date_field,
            create_button,
            create_result,
        ],
        scroll=True,
    )
    
    # List student tab
    students_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Name")),
            ft.DataColumn(ft.Text("Email")),
            ft.DataColumn(ft.Text("Belt")),
            ft.DataColumn(ft.Text("Birth date")),
        ],
        rows=[],
    )
    list_result = ft.Text()

    def list_students_click(e):
        try:
            response = requests.get(API_BASE_URL + "/students/")
            if response.status_code == 200:
                students = response.json()
                # Clear previous lines
                students_table.rows.clear()
                for student in students:
                    row = ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(student.get("name", ""))),
                            ft.DataCell(ft.Text(student.get("email", ""))),
                            ft.DataCell(ft.Text(student.get("belt", ""))),
                            ft.DataCell(ft.Text(student.get("birth_date", ""))),
                        ]
                    )
                    students_table.rows.append(row)
                list_result.value = f"{len(students)} students found."
            else:
                list_result.value = f"Error: {response.text}"
        except Exception as ex:
            list_result.value = f"Exception: {ex}"
        page.update()
        
        # print(response.json())

    list_button = ft.ElevatedButton(text="List students", on_click=list_students_click)
    list_students_tab = ft.Column([list_button, students_table, list_result], scroll=True)
        
    # Add lessons
    
    email_lesson_field = ft.TextField(label="Student Email")
    qtd_field = ft.TextField(label="Number of Classes", value="1")
    lesson_result = ft.Text()

    def check_lesson_click(e):
        try:
            qtd = int(qtd_field.value)
            payload = {
                "qtd": qtd,
                "email_student": email_lesson_field.value,
            }
            response = requests.post(API_BASE_URL + "/completed_lesson/", json=payload)
            if response.status_code == 200:
                # The API returns a success message 
                message = response.json()  # It can be a string or a object
                lesson_result.value = f"Sucsess: {message}"
            else:
                lesson_result.value = f"Error: {response.text}"
        except Exception as ex:
            lesson_result.value = f"Exception: {ex}"
        page.update()

    lesson_button = ft.ElevatedButton(text="Check Completed Lesson", on_click=check_lesson_click)
    lesson_tab = ft.Column([email_lesson_field, qtd_field, lesson_button, lesson_result], scroll=True)

    # Student Progress
    
    email_progress_field = ft.TextField(label="Student Email")
    progress_result = ft.Text()

    def consult_progress_click(e):
        try:
            email = email_progress_field.value
            response = requests.get(
                API_BASE_URL + "/student_progress/", params={"student_email": email}
            )
            if response.status_code == 200:
                progress = response.json()
                print(progress)
                progress_result.value = (
                    f"Name: {progress.get('name', '')}\n"
                    f"Email: {progress.get('email', '')}\n"
                    f"Current Belt: {progress.get('belt', '')}\n"
                    f"Total Lessons: {progress.get('total_lessons', '')}\n"
                    f"Lessons needed for next belt: {progress.get('required_classes_for_next_belt', '')}"
                )
            else:
                progress_result.value = f"Error: {response.text}"
        except Exception as ex:
            progress_result.value = f"Exception: {ex}"
        page.update()

    progress_button = ft.ElevatedButton(text="Consult Progress", on_click=consult_progress_click)
    progress_tab = ft.Column([email_progress_field, progress_button, progress_result], scroll=True)
    
    # Update Student
    
    id_student_field = ft.TextField(label="Student ID") #! create select field instead input!!!!!!!
    name_update_field = ft.TextField(label="New name")
    email_update_field = ft.TextField(label="New Email")
    belt_update_field = ft.TextField(label="New Belt")
    birth_date_update_field = ft.TextField(label="New Birth Date (YYYY-MM-DD)")
    update_result = ft.Text()

    def update_student_click(e):
        try:
            student_id = id_student_field.value
            if not student_id:
                update_result.value = "Student ID is required."
            else:
                payload = {}
                if name_update_field.value:
                    payload["name"] = name_update_field.value
                if email_update_field.value:
                    payload["email"] = email_update_field.value
                if belt_update_field.value:
                    payload["belt"] = belt_update_field.value
                if birth_date_update_field.value:
                    payload["birth_date"] = birth_date_update_field.value

                response = requests.put(API_BASE_URL + f"/students/{student_id}", json=payload)
                if response.status_code == 200:
                    student = response.json()
                    update_result.value = f"Updated student: {student}"
                else:
                    update_result.value = f"Error: {response.text}"
        except Exception as ex:
            update_result.value = f"Exception: {ex}"
        page.update()

    update_button = ft.ElevatedButton(text="Update student", on_click=update_student_click)
    update_tab = ft.Column(
        [
            id_student_field,
            name_update_field,
            email_update_field,
            belt_update_field,
            birth_date_update_field,
            update_button,
            update_result,
        ],
        scroll=True,
    )
    
    # Delete Student
    
    id_student_field = ft.TextField(label="Student ID")
    delete_result = ft.Text()
    
    def delete_student_click(e):
        student_id = id_student_field.value  # Student ID to be deleted
        if not student_id:
            delete_result.value = "Student ID is required."
        else:
            try:
                response = requests.delete(API_BASE_URL + f"/students/{student_id}")
                if response.status_code == 200:
                    delete_result.value = f"Student with ID {student_id} was deleted."
                else:
                    delete_result.value = f"Error: {response.text}"
            except Exception as ex:
                delete_result.value = f"Exception: {ex}"
        page.update()
    
    delete_button = ft.ElevatedButton(text="Delete student", on_click=delete_student_click)
    delete_tab = ft.Column(
        [
            id_student_field,
            delete_button,
            delete_result,
        ],
        scroll=True,
    )

    
    tabs = ft.Tabs(
        selected_index=0,
        tabs=[
            ft.Tab(text="Create Student", content=create_student_tab),
            ft.Tab(text="List Students", content=list_students_tab),
            ft.Tab(text="Lesson held", content=lesson_tab),
            ft.Tab(text="Consult Progress", content=progress_tab),
            ft.Tab(text="Update Student", content=update_tab),
            ft.Tab(text="Delete Student", content=delete_tab),
        ]
    )    
    
    page.add(tabs)

if __name__ == "__main__":
    ft.app(target=main)
