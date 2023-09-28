from model.project_model import Project
import string
import random


def random_name(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + "".join(random.choice(symbols) for i in range(random.randrange(maxlen)))


def test_add(app):
    project = Project(name=random_name("Project_", 10))
    old_projects = app.soap.get_project_list()
    app.project.create(project)
    new_projects = app.soap.get_project_list()
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
