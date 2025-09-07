import streamlit as st
from datetime import date
from task_manager import TaskManager

st.set_page_config(page_title="TaskFlow", layout="wide")

# Initialize TaskManager
if "task_manager" not in st.session_state:
    st.session_state.task_manager = TaskManager()
task_manager = st.session_state.task_manager

# --- Sidebar ---
st.sidebar.title("TaskFlow")
st.sidebar.subheader("Overview")

all_tasks = task_manager.get_tasks()
st.sidebar.write(f"Total tasks: {len(all_tasks)}")
st.sidebar.write(f"Completed: {sum(t['completed'] for t in all_tasks)}")

filter_choice = st.sidebar.radio("Filter", ["All", "Active", "Completed"])

# --- Main ---
st.title("My Tasks")
st.write("Manage your daily tasks efficiently")

# Add Task
if "new_task_text" not in st.session_state:
    st.session_state.new_task_text = ""

st.session_state.new_task_text = st.text_input("Enter new task", st.session_state.new_task_text)

if st.button("Add Task") and st.session_state.new_task_text.strip():
    task_manager.add_task(st.session_state.new_task_text.strip(), str(date.today()))
    st.session_state.new_task_text = ""  # Clear input after adding

# Filter tasks
filtered_tasks = [
    t for t in all_tasks
    if (filter_choice == "All") or
       (filter_choice == "Active" and not t["completed"]) or
       (filter_choice == "Completed" and t["completed"])
]

# Display tasks
for t in filtered_tasks:
    i = all_tasks.index(t)
    cols = st.columns([5, 2, 2, 2])

    # Task text
    with cols[0]:
        status = "✅" if t["completed"] else ""
        st.write(f"- **{t['task']}** ({t['date']}) {status}")

    # Edit
    edit_key = f"edit_text_{i}"
    if edit_key not in st.session_state:
        st.session_state[edit_key] = t["task"]

    with cols[1]:
        # Let text_input handle session_state automatically
        new_text = st.text_input("Edit task:", key=edit_key)
        if new_text.strip() != t["task"]:
            task_manager.edit_task(i, new_text.strip())

    # Delete
    with cols[2]:
        if st.button("🗑️ Delete", key=f"delete_{i}"):
            task_manager.delete_task(i)
            break  # Stop loop to avoid session_state issues

    # Complete
    with cols[3]:
        if t["completed"]:
            st.write("✅ Completed")
            if st.button("↩️ Mark Active", key=f"undo_{i}"):
                task_manager.toggle_task(i)
                break
        else:
            if st.button("✅ Complete", key=f"complete_{i}"):
                task_manager.toggle_task(i)
                break




