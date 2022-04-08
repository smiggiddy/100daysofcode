from . import db 
from .models import ToDoList, Tasks
import secrets

class ToDos:
    """Helper class to hold notes until saved in database"""

    def __init__(self):
        self.todo_list = []


    def store_todo_id(self, todo_id):
        """Function takes todo id and creates dictionary and list for todolist"""
        todo_dict = {todo_id: []}
        self.todo_list.append(todo_dict)

        
    def return_todo_index(self, todo_id):
        """Function returns list index for todo_id"""
        for todo_list in self.todo_list:
            if todo_id in todo_list:
                index = self.todo_list.index(todo_list)            
                return index
        
        return None
    
    
    def note_id_exists(self, todo_id):
        """Bool function for returns true if url is valid"""

        for todo_list in self.todo_list:
            if todo_id in todo_list:
                return True
        
        return False


    def todo_in_db(self, hash):
        """Bool function to check if todo list exists in database"""

        in_db = ToDoList.query.filter_by(note_hash=hash).first()
        return in_db != None

    
    def get_todo(self, hash):
        """Function returns all the list items for note_hash"""

        # Grab ID from ToDoList Table
        todo_list = ToDoList.query.filter_by(note_hash=hash).first()

        # Pull all tasks with matching ToDo ID
        items_list = Tasks.query.filter_by(todo_id=todo_list.id).all()

        return items_list
    



def generate_note_hash():
    """Function returns a random hash as note ID"""

    # generate hash
    note_hash = secrets.token_urlsafe(8)

    # Verify hash not in database already
    in_db = ToDoList.query.filter_by(note_hash=note_hash).first()

    if not in_db:
        return note_hash
    else:
        return generate_note_hash()


def return_url_string(note_id):
    """Function returns url as string"""
    return str(note_id)