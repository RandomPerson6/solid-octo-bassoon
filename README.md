# Steps to run
## 1. Python Environment setup
Make environment
```
python3 -m venv env
```

Package installations:
```
pip install Django==2.1.*
pip3 install pymysql
```

## 2. Start Mariadb server

### Setup Mariadb
```
sudo apt update
sudo apt install mariadb-server
```

### Create mariadb user and database
In bash terminal:
```
sudo mysql
```

Create user, database and grant permissions:
```
create user 'projectadmin'@'localhost' identified by 'projectpass';
create database libdb;
grant all privileges on libdb.* to 'projectadmin'@'localhost';
```
