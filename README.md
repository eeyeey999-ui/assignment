### Django Project - Assignment for library data clear, import & export

#### **_ERB assignment submitted by L.. ..G ..E (14) on 3 Nov 2025_**

### Steps to build and run the assignment

### 1. Create virtual environment

```bash
mkvirtualenv assignment
```

### 2. Create project folder

```bash
django-admin startproject assign .
```

### 3. Run the server

```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000 to confirm the server is running

#### 4. Goto Visual Studio Code (VS code)

```bash
code .
```

#### 5. Import Data

Run the script at import_data.py by using the 'Run Python File' (Sample data file refer to sample_data.json)

#### 6. Export Data

Check the output file at exported_data.json

#### 7. Goto Admin panel to clear data

http://127.0.0.1:8000/admin/login/?next=/admin/

- Username : Admin
- Password : 1234

#### 8. Ckear Data

=> Select LIBRARY => Authors => tick all NAME => Goto ACTION Dropdown => Select delete selected authors => Press buttons Go then Yes
