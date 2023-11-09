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




# Working with CSV Files
import csv 

with open("data.csv","w") as file:
    writer =  csv.writer(file)
    writer.writerow(["transaction_id","product_id","price_id"])
    writer.writerow([1000,1,5])