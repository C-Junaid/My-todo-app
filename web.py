import streamlit as st
import Functions

todos = Functions.get_todos()


def add_todo():
    todo = st.session_state["New_Todo"] + '\n'
    todos.append(todo)
    Functions.write_todos(todos)


st.title("My To Do App")
st.subheader("This is my To-Do App")
st.write("This app can help improve your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        Functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="Enter a To-Do", placeholder="Add New To-Do",
              on_change=add_todo, key="New_Todo")







