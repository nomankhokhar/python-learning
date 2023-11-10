# Path Lib in Python
from pathlib import Path
from time import ctime
path = Path(r"C:\Program Files")

print(path.exists())
print(path.is_file())
print(path.is_dir())
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
path = path.with_name('file.txt')
print(path)
print(path.absolute())
path = path.with_suffix('.txt')
print(path)

paths = [dir for dir in path.iterdir() if dir.is_dir()]
pyFiles = [pyfile for pyfile in path.glob("*.py")]
pyFiles = [pyfile for pyfile in path.rglob("*.py")]
print(paths)
print(pyFiles)



target = Path("ecommerce/__init__.py") 
source = Path() / "__init__.py"
target.exists()
target.rename("init.txt")
target.unlink()   # will delete the files
print(ctime(target.stat().st_atime))

print(source.write_text("knkjnkjnk"))

# Write one file data into Another file
target.write_text(source.read_text())

# Above one is not bettter there is better way to do that
import shutil
shutil.copy(source , target)



# Working with Zip files
from zipfile import ZipFile

with ZipFile("files.zip","w") as zip:
    for path in Path("ecommerce").rglob("*.*"):
        zip.write(path)
        
        
with ZipFile("files.zip") as zip:
    print(zip.namelist())
    info = zip.getinfo("ecommerce/__init__.py")
    print(info.file_size)
    print(info.compress_size)
    zip.extractall("noman")




# Working with CSV Files
import csv 

with open("data.csv","w") as file:
    writer =  csv.writer(file)
    writer.writerow(["transaction_id","product_id","price_id"])
    writer.writerow([1000,1,5])
    writer.writerow([1001,3,15])

with open('data.csv') as file:
    reader = csv.reader(file)
    print(list(reader))
    for row in reader:
        print(row)


# Working with JSON

import json
movies = [
    {"id":1,"title":"Terminator", "year":1989},
    {"id":2,"title":"Terminator Genisis", "year":1993}    
]

data = json.dumps(movies)
Path("movies.json").write_text(data)

data = Path("movies.json").read_text()
movies = json.loads(data)
print(movies)



# Working with SQLite in Python

import sqlite3
import json
from pathlib import Path

# You will get and error because you have to install Sqlite DB for inserting data
movies = json.loads(Path("movies.json").read_text())
with sqlite3.connect("sb.sqlite3") as conn:
    command = "INSERT INTO Movies VALUES(?,?,?)"
    for movie in movies:
        conn.execute(command , tuple(movie.values()))
    conn.commit()
    

with sqlite3.connect("sb.sqlite3") as conn:
    command = "SELECT * FROM Movies"
    cursor = conn.execute(command)
    for row in cursor:
        print(row)
    movies = cursor.fetchall()
    print(movies)
    conn.commit()
    


# Working with timeStamp

import time

def send_emails():
    for i in range(10000):
        pass
    
start = time.time()
send_emails()
end = time.time()
duration = end - start
print(duration)


# Working with datetime

from datetime import datetime
import time

dt1 = datetime(2018, 1, 1)
dt2= datetime.now()
dt = datetime.strptime("2018/01/01", "%Y/%m/%d")
dt = datetime.fromtimestamp(time.time())
print(dt)

print(f"{dt.year}/{dt.month}/{dt.day}")
print(dt.strftime("%Y/%m/%d"))
print(dt2 > dt1)



# Working with Random Values

import random
import string

print(random.random())
print(random.randint(1,10))
print(random.choice([1, 2, 3, 4]))
print(random.choices([1, 2, 3, 4] , k = 2))
print("".join(random.choices(string.ascii_letters + string.digits , k = 4)))

# this will rearrange the Number's
numbers = [1,2,3,5]
random.shuffle(numbers)
print(numbers)


# Opening the Browser 

import webbrowser

print("Deployement completed")
webbrowser.open("http://google.com")



# Sending mail to the Person's and template


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib

template = Template(Path('template.html').read_text())

message = MIMEMultipart()
message['from'] = "Noman Ali"
message['to'] = 'aliyounas084@gmail.com'
message['subject'] = 'this is test script'
body = template.subtitute({"name":"Noman Ali"})
message.attach(MIMEText(body , "Plain"))
message.attach(MIMEImage(Path("name.extension").read_bytes()))

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("email","password")
    smtp.send_message(message)
    print("Sent...")



# Command Line argument
import sys

if len(sys.argv) == 1:
    print("USAGE: python3 app.py <password>")
else:
    password =sys.argv[1]
    print(password)



# Running External Program

import subprocess

subprocess.call
subprocess.check_call
subprocess.check_output
subprocess.Popen

subprocess.run(['dir'])

import subprocess

# 1. Run a command and capture its output
result = subprocess.run(["ls", "-l"], stdout=subprocess.PIPE, text=True)
# The 'run' function executes the given command and returns a CompletedProcess object.
# stdout=subprocess.PIPE captures the command's standard output as a string.
# text=True specifies that the output should be decoded as text.

# 2. Accessing the command's output
output = result.stdout
print("Output of the command:", output)

# 3. Running a command and capturing both stdout and stderr
result = subprocess.run(["ls", "non_existent_file"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
# stderr=subprocess.PIPE captures the command's standard error output as a string.

# 4. Check the return code of the command
return_code = result.returncode
print("Return code:", return_code)

# 5. Running a command in the background (non-blocking)
process = subprocess.Popen(["ping", "example.com"])
# The 'Popen' function starts the command and returns a Popen object.
# The command runs in the background and doesn't block the main script.

# 6. Communicate with the running process
stdout, stderr = process.communicate()
# The 'communicate' method waits for the process to finish and returns its stdout and stderr.

# 7. Wait for a process to finish
process.wait()
# The 'wait' method blocks until the process is complete.

# 8. Sending input to a process
process = subprocess.Popen(["cat"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
process.stdin.write("Hello, subprocess!")
process.stdin.close()
output = process.stdout.read()
# We create a 'cat' process and write input to it using the stdin attribute.

# 9. Specifying a custom working directory
result = subprocess.run(["ls", "-l"], stdout=subprocess.PIPE, text=True, cwd="/path/to/directory")
# The 'cwd' parameter allows you to set the working directory for the command.

# 10. Handling exceptions for command execution
try:
    result = subprocess.run(["ls", "non_existent_file"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
except subprocess.CalledProcessError as e:
    print("Error executing command:", e)
# 'check=True' raises a CalledProcessError if the command returns a non-zero exit code.

# 11. Shell command execution (use with caution)
result = subprocess.run("echo 'Hello, subprocess!'", shell=True, stdout=subprocess.PIPE, text=True)
# Using 'shell=True' allows you to run commands with shell features like pipes and variables.
# Be careful with user-provided input to avoid security risks.

# 12. Timeout for command execution
try:
    result = subprocess.run(["sleep", "5"], timeout=3)
except subprocess.TimeoutExpired as e:
    print("Command timed out:", e)

# 13. Capturing environment variables
env_vars = subprocess.Popen(["env"], stdout=subprocess.PIPE, text=True).communicate()[0]
print("Environment variables:", env_vars)

# 14. Specifying a custom environment
custom_env = {"MY_VARIABLE": "12345"}
result = subprocess.run(["echo", "$MY_VARIABLE"], stdout=subprocess.PIPE, text=True, env=custom_env)
# 'env' allows you to set environment variables for the command.

# 15. Redirecting input/output to files
with open("output.txt", "w") as output_file:
    subprocess.run(["ls", "-l"], stdout=output_file, text=True)
# You can redirect input/output to files by passing file handles instead of subprocess.PIPE.



# pip packages modules helpers

import requests

res = requests.get("http://google.com")
print(res)



# Manageing the Dependencies of Packages command's

# pipenv graph
# pipenv uninstall requests
# pipenv install requests=2.9.*
# pipenv update --outdated
# pipenv update --outdated
# pipenv update "request" this will update only request package 