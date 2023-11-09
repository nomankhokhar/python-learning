# # Path Lib in Python
from pathlib import Path
# from time import ctime
# path = Path(r"C:\Program Files")

# print(path.exists())
# print(path.is_file())
# print(path.is_dir())
# print(path.name)
# print(path.stem)
# print(path.suffix)
# print(path.parent)
# path = path.with_name('file.txt')
# print(path)
# print(path.absolute())
# path = path.with_suffix('.txt')
# print(path)

# paths = [dir for dir in path.iterdir() if dir.is_dir()]
# pyFiles = [pyfile for pyfile in path.glob("*.py")]
# pyFiles = [pyfile for pyfile in path.rglob("*.py")]
# print(paths)
# print(pyFiles)



# target = Path("ecommerce/__init__.py") 
# source = Path() / "__init__.py"
# target.exists()
# target.rename("init.txt")
# target.unlink()   # will delete the files
# print(ctime(target.stat().st_atime))

# print(source.write_text("knkjnkjnk"))

# # Write one file data into Another file
# target.write_text(source.read_text())

# # Above one is not bettter there is better way to do that
# import shutil
# shutil.copy(source , target)



# # Working with Zip files
# from zipfile import ZipFile

# with ZipFile("files.zip","w") as zip:
#     for path in Path("ecommerce").rglob("*.*"):
#         zip.write(path)
        
        
# with ZipFile("files.zip") as zip:
#     print(zip.namelist())
#     info = zip.getinfo("ecommerce/__init__.py")
#     print(info.file_size)
#     print(info.compress_size)
#     zip.extractall("noman")




# # Working with CSV Files
# import csv 

# with open("data.csv","w") as file:
#     writer =  csv.writer(file)
#     writer.writerow(["transaction_id","product_id","price_id"])
#     writer.writerow([1000,1,5])
#     writer.writerow([1001,3,15])

# with open('data.csv') as file:
#     reader = csv.reader(file)
#     print(list(reader))
#     for row in reader:
#         print(row)


# # Working with JSON

# import json
# movies = [
#     {"id":1,"title":"Terminator", "year":1989},
#     {"id":2,"title":"Terminator Genisis", "year":1993}    
# ]

# data = json.dumps(movies)
# Path("movies.json").write_text(data)

# data = Path("movies.json").read_text()
# movies = json.loads(data)
# print(movies)



# # Working with SQLite in Python

# import sqlite3
# import json
# from pathlib import Path

# # You will get and error because you have to install Sqlite DB for inserting data
# movies = json.loads(Path("movies.json").read_text())
# with sqlite3.connect("sb.sqlite3") as conn:
#     command = "INSERT INTO Movies VALUES(?,?,?)"
#     for movie in movies:
#         conn.execute(command , tuple(movie.values()))
#     conn.commit()
    

# with sqlite3.connect("sb.sqlite3") as conn:
#     command = "SELECT * FROM Movies"
#     cursor = conn.execute(command)
#     for row in cursor:
#         print(row)
#     movies = cursor.fetchall()
#     print(movies)
#     conn.commit()
    


# # Working with timeStamp

# import time

# def send_emails():
#     for i in range(10000):
#         pass
    
# start = time.time()
# send_emails()
# end = time.time()
# duration = end - start
# print(duration)


# # Working with datetime

# from datetime import datetime
# import time

# dt1 = datetime(2018, 1, 1)
# dt2= datetime.now()
# dt = datetime.strptime("2018/01/01", "%Y/%m/%d")
# dt = datetime.fromtimestamp(time.time())
# print(dt)

# print(f"{dt.year}/{dt.month}/{dt.day}")
# print(dt.strftime("%Y/%m/%d"))
# print(dt2 > dt1)


