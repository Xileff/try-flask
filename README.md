# try-flask

Steps to run app

For branch main
1. pip install -r requirements.txt
2. python
3. from app import db
4. db.create_all()
5. exit()
6. python app.py

For branch mysql
1. pip install -r requirements.txt
2. create a MySQL database with a table named 'todo'. 
the table columns are :
 - id int auto increment
 - name varchar(50)
3. create a .env file containing your MySQL host, username, password, and database name
4. run app.py
