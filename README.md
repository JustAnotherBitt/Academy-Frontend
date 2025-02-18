# Academy Frontend

## Overview

The **Academy Frontend** project provides a user-friendly interface for interacting with the <a href="https://github.com/JustAnotherBitt/Academy-Backend">**Academy Backend**</a>API<. It allows users to perform various operations such as creating students, updating student details, deleting students, listing all students, marking lessons as completed, and checking student progress. This frontend is built using **Flet**, a framework for creating cross-platform apps with Python.

## First look

<p align="center">
<img src="https://github.com/user-attachments/assets/0ba17f04-e535-42d4-80af-e46b41953ccf" alt="" width="850">
</p>


## Features

- **Create Student**: Allows you to create a new student profile by providing necessary details such as name, email, belt, and birth date.
- **List Students**: Displays a list of all students with their details.
- **Mark Lesson as Completed**: Allows you to mark lessons as completed for a student by specifying the student’s email and the number of lessons completed.
- **Consult Student Progress**: Retrieves a student’s progress by email, showing their current belt, total lessons, and lessons required for the next belt.
- **Update Student**: Lets you update an existing student’s information, such as name, email, belt, and birth date.
- **Delete Student**: Allows you to delete a student by their ID.

## Technologies Used

- **Flet**: A framework for building cross-platform apps with Python. Used to create the frontend UI and interact with the backend API.
- **Requests**: A simple HTTP library for making requests to the backend API.

## Installation

To run this project locally, follow the steps below:

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/academy-frontend.git
   cd academy-frontend
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install the required dependencies:

   ```bash
   pip install flet
   pip install requests
   ```

4. Ensure that the **Academy Backend** is running locally. If it’s not, refer to the backend repository for instructions on setting it up.

5. Run the frontend:

   ```bash
   python app.py      
   ```

6. The frontend will open in a window and interact with the **Academy Backend** API.

## API Interaction

This frontend interacts with the backend API, which must be running concurrently for proper functionality. The key endpoints are:

- **Create a Student** (`POST /api/`): Creates a new student profile.
- **List Students** (`GET /api/students/`): Lists all students.
- **Mark Lesson as Completed** (`POST /api/completed_lesson/`): Marks lessons as completed for a student.
- **Student Progress** (`GET /api/student_progress/`): Retrieves a student’s progress, including current belt, total lessons, and required lessons for the next belt.
- **Update a Student** (`PUT /api/students/{student_id}`): Updates a student's information.
- **Delete a Student** (`DELETE /api/students/{student_id}`): Deletes a student by ID.

## Usage

- **Tabs**: The application consists of several tabs:
    - **Create Student**: Allows creating a new student.
    - **List Students**: Displays a table with all students.
    - **Lesson Held**: Marks lessons as completed for a student.
    - **Consult Progress**: Displays a student's progress.
    - **Update Student**: Updates an existing student’s details.
    - **Delete Student**: Deletes a student from the system.

Each tab corresponds to a different functionality in the system, providing a seamless and easy-to-use experience.

## Observations

- IDE used: <a href="https://code.visualstudio.com/download">Visual Studio Code</a>.
- Backend API must be running for the frontend to work properly.

