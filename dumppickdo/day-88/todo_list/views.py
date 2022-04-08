from crypt import methods
from distutils.log import error
from logging import exception
from sqlite3 import IntegrityError
from tkinter import E
from flask import Blueprint, jsonify, redirect, url_for, render_template, request, flash
from .models import ToDoList, Tasks
from . import db 
from .utils import generate_note_hash, ToDos
from datetime import datetime
import json



views = Blueprint('views', __name__)
todo = ToDos()


@views.route("/")
def home():
    """Returns the homepage"""

    # Generate random note ID on each visit to home page
    note_id = generate_note_hash()
    todo.store_todo_id(note_id)

    return render_template('base.html', note_id=note_id)


@views.route("/<note_id>/dump-tasks", methods=['GET', 'POST'])
def note(note_id):
    """Function used to render dumped tasks"""

    # redirct home if invalid note_id
    if not todo.note_id_exists(note_id):
        return redirect(url_for('views.home'))


    # Grab index / pass note_id dictionary key 
    index_todo = todo.return_todo_index(note_id)

    if request.method == 'POST':
        items = request.form.get('todo')

        # get todo_list index to append todo into list
        # LIST[INDEX][DICTIONARY / NOTE ID ]        
        todo.todo_list[index_todo][note_id].append(items)


    return render_template('todolist.html', note_id=note_id, todo_list=todo.todo_list[index_todo][note_id])


@views.route("/<note_id>/todo-list", methods=['POST', 'GET'])
def pick(note_id):
    """Method used to narrow down todo list"""

    # Grab index / pass note_id dictionary key 
    index_todo = todo.return_todo_index(note_id)

    if request.method == 'POST' and index_todo != None:
        
        dump_list = todo.todo_list[index_todo][note_id]
        picked_tasks_list = request.form.getlist('item')

        if len(picked_tasks_list) >= 1:
            todo.todo_list[index_todo][note_id] = picked_tasks_list
            save_note(note_id, picked_tasks_list)
            # print(f"Checking if in database: {todo.todo_in_db(note_id)}")

            picked_list = todo.get_todo(note_id)
            return render_template(
                'pick.html', 
                note_id=note_id, 
                picked_tasks=picked_list
                )
        
        else:
            flash('Please select or enter a task', 'error')
            return redirect(url_for('views.note', note_id=note_id))                   

        flash('Please select a task or enter a task', 'error')

    elif request.method == 'GET':
        if todo.todo_in_db(note_id):
            picked_list = todo.get_todo(note_id)

            return render_template('pick.html', note_id=note_id, picked_tasks=picked_list)
    
    return redirect(url_for('views.note', note_id=note_id) )



@views.route("/<note_id>/save", methods=['POST'])
def save_note(note_id, picked_tasks):
    """ Function saves note to database"""


    try:
        new_list = ToDoList(
            note_hash = note_id,
            name = 'todo_list',
            date = datetime.now(),
        )

        db.session.add(new_list)
        db.session.commit()

        save_list_items(picked_tasks, note_id)


    except Exception as E:
        if E:
            print(E)
            print(type(E))


@views.route('/delete', methods=['POST'])
def delete_item():
    """Function deletes the requested task"""

    task = json.loads(request.data)
    task_id = task['taskId']
    task = Tasks.query.get(task_id)
    if task:
        # delete task from list
        db.session.delete(task)
        db.session.commit()
    return jsonify({}) #returns empty funtion
    

@views.route('/<note_id>/complete/<task_id>', methods=['POST'])
def completed_task(note_id, task_id):
    """Function is used to mark item as complete"""

    task_id = request.form.get('todo')
    
    task = Tasks.query.get(task_id)
    task.completed = 1
    db.session.commit()


    return redirect(url_for('views.pick', note_id=note_id) )


def save_list_items(todo_list_items, note_id):
    """Function returns the todo_list id"""

    # Get ID
    list_id = ToDoList.query.filter_by(note_hash=note_id).first()    
    todo_id =  list_id.id

    for item in todo_list_items:
        add_to_db = Tasks(
            todo_id=todo_id,
            list_item_name=item
        )
        db.session.add(add_to_db)
        db.session.commit()


