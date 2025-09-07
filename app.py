import streamlit as st
from datetime import date
from task_manager import TaskManager

st.set_page_config(page_title="TaskFlow", layout="wide")

# Initialize TaskManager in session
if "task_manager" not in st.session_state:
    st.session_state.task_manager = TaskManager()
task_manager = st.session_state.task_manager

# --- Sidebar ---
st.sidebar.title("TaskFlow")
st.sidebar.subheader("ListTodo Overview")

# Always fetch tasks fresh
all_tasks = task_manager.get_tasks()
st.sidebar.write(f"Total ListTodo: {len(all_tasks)}")
st.sidebar.write(f"Completed: {sum(1 for t in all_tasks if t['completed'])}")

filter_choice = st.sidebar.radio("Filter ListTodo", ["All", "Active", "Completed"])

# --- Main ---
st.title("My Tasks")
st.write("Manage your daily tasks efficiently")

# Add new task
if "new_task_text" not in st.session_state:
    st.session_state.new_task_text = ""

st.session_state.new_task_text = st.text_input("Enter new task", st.session_state.new_task_text)

if st.button("Add Task") and st.session_state.new_task_text.strip():
    task_manager.add_task(st.session_state.new_task_text.strip(), str(date.today()))
    st.session_state.new_task_text = ""  # Clear input

# Filter tasks
filtered_tasks = []
for t in all_tasks:
    if filter_choice == "Active" and t["completed"]:
        continue
    if filter_choice == "Completed" and not t["completed"]:
        continue
    filtered_tasks.append(t)

# Display tasks
for t in filtered_tasks:
    i = all_tasks.index(t)
    cols = st.columns([5, 2, 2, 2])

    # Task text
    with cols[0]:
        st.write(f"- **{t['task']}** ({t['date']})")

    # Edit
    edit_key = f"edit_text_{i}"
    if edit_key not in st.session_state:
        st.session_state[edit_key] = t["task"]
    with cols[1]:
        if st.button("✏️ Edit", key=f"edit_{i}"):
            new_text = st.text_input("Edit task:", st.session_state[edit_key], key=edit_key)
            if new_text.strip() and new_text.strip() != t["task"]:
                task_manager.edit_task(i, new_text.strip())
                st.session_state[edit_key] = new_text.strip()

    # Delete
    with cols[2]:
        if st.button("🗑️ Delete", key=f"delete_{i}"):
            task_manager.delete_task(i)
            break  # Break to avoid iteration issues

    # Complete / Completed column
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



