function deleteNote(taskId, todoHash){
    fetch('/delete', {
      method: 'POST',
      body: JSON.stringify({ taskId: taskId })
    }).then((_res) => {
        url_string = `/${todoHash}/todo-list`;
        window.location.href = url_string;
    });
  }
