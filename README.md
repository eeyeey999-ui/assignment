## Django Project - Assignment for library data clear, import & export

#### **_ERB assignment submitted by L.. ..G ..E (14) on 3 Nov 2025_**

### Steps to run the assignment

### 1. Open terminal, Create a folder 'assignment' and Clone the repository from Github

```bash
mkdir assignment
cd assignment
git clone https://github.com/eeyeey999-ui/assignment.git
```

### 2. Create a virtual envirnment and Update the security key

```bash
mkvirtualenv assign
workon assign
code .
```

Create a file '.env ' to update the security key in VS code

### 3. Run the server

```bash
python manage.py runserver
```

Goto http://127.0.0.1:8000 to confirm the server is running

### 4. Open VS code again in the assignment folder using new terminal

```bash
code .
```

### 5. Import Data

Run the script at import_data.py using the 'Run Python File' button (Refer to the sample data file: sample_data.json)

### 6. Export Data

Check the output file: exported_data.json

### 7. Goto the Admin panel to Clear data

Visit http://127.0.0.1:8000/admin/login/?next=/admin/ to access the admin panel

- Username : Admin
- Password : 1234

Clear Data:
Goto LIBRARY → Click Authors → Tick all Names → ACTION Dropdown → Select 'Delete selected authors' → Press Go → Confirm with Yes
