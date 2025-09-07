TaskFlow - To-Do Manager

TaskFlow is a simple web-based To-Do Manager built with Streamlit. It allows users to manage their daily tasks efficiently with full CRUD functionality (Create, Read, Update, Delete).

Features

1.Add tasks with title and date

2.Edit tasks inline

3.Delete tasks

4.Mark tasks as complete or active

5.Filter tasks by All / Active / Completed

6.Modern Streamlit-compatible UI

Folder Structure
taskflow/
│── app.py                # Main Streamlit app
│── task_manager.py       # Task manager class (CRUD)
│── requirements.txt      # Dependencies
│── README.md             # Project documentation

Installation

Clone the repository:

git clone https://github.com/Soundarya-Cyber/To-Do-Manager.git
cd taskflow


Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows


Install dependencies:

pip install -r requirements.txt

Usage

Run the Streamlit app:

streamlit run app.py


Add Task: Enter a task in the input box and click “Add Task”.

Edit Task: Click ✏️ next to a task to edit its text.

Delete Task: Click 🗑️ to remove a task.

Complete Task: Click ✅ to mark a task as completed.

Mark Active: Click ↩️ to revert a completed task back to active.

Filter Tasks: Use the sidebar to filter tasks by All / Active / Completed.

Dependencies

Python 3.10+

Streamlit

Install dependencies using:

pip install -r requirements.txt


License

This project is released under the MIT License.
