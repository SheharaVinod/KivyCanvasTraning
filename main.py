import pathlib
import os

classes = """

class {name}:
    pass

"""

cwd = pathlib.Path.cwd()
os_dir = os.listdir(cwd)
ignore = ['.git', '.idea', 'main.py']

for i in ignore:
    os_dir.remove(i)
new_dir = os_dir.copy()

for dir in os_dir:
    with open(dir+f"/{dir.lower()}.py", "w") as script:
        script.write(classes.format(name=dir))

