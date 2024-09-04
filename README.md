**Run virtual environment**

`python3 -m venv .venv`

**Require package**

- flask
- flask-wtf
- email_validator
- flask-sqlalchemy
- flask-bcrypt
- flask-login
- pillow
- flask-mail

**Run**

`flask --app {project_name} run --debug`

**Manually set up context**

```
>>> from {project_name} import app, db
>>> app.app_context().push()
>>> db.create_all()
```
