#### Django Project - Assignment for library data clear, import & export

##### ERB L.. ..G ..E (14) submit on 3 Nov 2025

##### Steps to build and run the assignment

##### 1. Create virtual environment

```bash
mkvirtualenv assignment
```

##### 2. Create project folder

```bash
django-admin startproject assign .
```

##### 3. Run the server

```bash
python manage.py runserver
```

##### 4. Goto vs code to do import and export data => code .

```py
IMPORT DATA: Script at import_data.py =>  press button Run Python File
EXPORT DATA: Check data file at exported_data.json
Refer to data file => sample_data.json
```

##### 5. Goto Admin Panel to clear data

##### Login at http://127.0.0.1:8000/admin/login/?next=/admin/

##### Username : Admin

##### Password : 1234

##### CLEAR DATA: Select LIBRARY => Authors => tick all NAME => Goto ACTION Box => Select delete selected authors => Press button Go => Press button Yes
