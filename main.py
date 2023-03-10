from modules.functions import get_todos, write_todos
import streamlit as st

todos = get_todos()


def add_todo():
    td = st.session_state["new_todo"] + "\n"
    todos.append(td)
    write_todos(todos)



st.title("Todo App")

for todo in todos:
    st.checkbox(todo)

st.text_input(key="new_todo", label="", placeholder="Enter todo Item",
              on_change=add_todo)

st.session_state
