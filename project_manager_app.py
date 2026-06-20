from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# 1. Custom Initial Project Board Data
team_tasks = [
    {"id": 1, "title": "Design App UI", "assigned_to": "Chaitra", "status": "In Progress", "comments": ["Finalize ad banners."]},
    {"id": 2, "title": "Mobile Documentation", "assigned_to": "Sibbu", "status": "To Do", "comments": []}
]

# 2. Frontend Layout Interface (HTML/CSS)
BOARD_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>TaskBoard - Project Planner</title>
    <style>
        body { font-family: system-ui, sans-serif; margin: 15px; background-color: #f4f6f9; color: #333; }
        .board { display: flex; flex-direction: column; gap: 15px; }
        .card { background: white; padding: 15px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
        .badge { background: #007bff; color: white; padding: 3px 8px; border-radius: 4px; font-size: 0.85em; }
        .notes-section { margin-top: 10px; background: #f8f9fa; padding: 10px; border-radius: 6px; }
        .btn { background-color: #28a745; color: white; border: none; padding: 6px 12px; border-radius: 4px; cursor: pointer; }
        .box { width: 80%; padding: 6px; margin: 5px 0; border: 1px solid #ccc; border-radius: 4px; }
    </style>
</head>
<body>

    <h2>📋 Workspace Project Board</h2>
    <p>Track team tasks, assignees, and active conversation feeds below.</p>

    <div class="board">
        {% for task in cards %}
        <div class="card">
            <h3>📌 {{ task.title }}</h3>
            <p><strong>Assigned To:</strong> {{ task.assigned_to }} | <span class="badge">{{ task.status }}</span></p>
            
            <div class="notes-section">
                <h4>Task Notes & Comments:</h4>
                {% if task.comments|length == 0 %}
                    <p style="color:#777;">No messages logged yet.</p>
                {% else %}
                    <ul>
                    {% for note in task.comments %}
                        <li>{{ note }}</li>
                    {% endfor %}
                    </ul>
                {% endif %}
                
                <form action="/comment/{{ task.id }}" method="POST">
                    <input type="text" name="user_note" class="box" placeholder="Add a comment..." required>
                    <button type="submit" class="btn">Post</button>
                </form>
            </div>
        </div>
        {% endfor %}
    </div>

</body>
</html>
"""

# 3. Routing Logic
@app.route('/')
def workspace():
    return render_template_string(BOARD_HTML, cards=team_tasks)

@app.route('/comment/<int:id_num>', methods=['POST'])
def add_comment(id_num):
    text_note = request.form.get('user_note')
    for task in team_tasks:
        if task['id'] == id_num:
            task['comments'].append(text_note)
            break
    return redirect(url_for('workspace'))

if __name__ == '__main__':
    # Run server on port 9000 to keep it separate from other projects
    app.run(debug=True, port=9000)
