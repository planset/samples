from flask import Blueprint, render_template
from app.model.project import ProjectModel

project = Blueprint('admin', __name__)

@project.route('/')
def index():
    model = ProjectModel()
    return render_template('project.html', model=model)

