#### Django Project - Assignment for library data clear, import & export

##### Steps to build and run the assignment

##### 1. Create virtual environment

```bash
mkvirtualenv assignment
```

##### 2. Create project folder

```bash
django-admin startproject assign .
```

##### 3. Run the server Visit http://127.0.0.1:8000 to confirm the server is running

```bash
python manage.py runserver
```

##### 4. Goto vs code to do import and export data

```bash
code .
```

Import Data:
Run the script at import_data.py using the 'Run Python File'
Export Data:
Check the output file at exported_data.json
Reference file:
sample_data.json

##### 5. Clear Data in Admin panel

**Bold text**, _italic text_, and [links](http://127.0.0.1:8000/admin/login/?next=/admin/)

- Username : Admin
- Password : 1234

Ckear Data:
=> Select LIBRARY => Authors => tick all NAME
=> Goto ACTION Dropdown => Select delete selected authors
=> Press buttons Go then Yes
