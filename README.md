# Academic Management Portal  

This portal is a Flask-based application designed for managing academic activities. It enables file uploads for each academic year, stores student queries through a contact form, and dynamically displays uploaded content.  

## Features  
- **Year-Specific File Uploads**:  
  Upload and organize academic resources by first, second, and third years.  
- **Student Query Management**:  
  Collect and store student queries via a contact form integrated with an SQLite database.  
- **Result Display**:  
  Show uploaded academic files dynamically in a user-friendly table format.  
- **User-Friendly Interface**:  
  Separate pages for academic years, courses, and contact queries.  

## Installation  

1. Clone the repository:  
   ```bash  
   git clone https://github.com/your-repo/academic-management-portal.git  
   cd academic-management-portal
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt  
    ```
4. Configure the file upload paths in ```app.config```:
   ```bash
   app.config['UPLOAD_FOLDER1'] = '<path_to_first_year_files>'  
   app.config['UPLOAD_FOLDER2'] = '<path_to_second_year_files>'  
   app.config['UPLOAD_FOLDER3'] = '<path_to_third_year_files>'
   ```
5. Initialize the database:
   ```bash
   python  
    >>> from app import db  
    >>> db.create_all()  
    >>> exit()
   ```
6. Run the application:
   ```bash
   python app.py  
   ```
 
