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

all_destinations = []
for dir in os_dir:
    all_destinations.append(str(cwd.joinpath(dir)))

for each_path in all_destinations:
    print(each_path)
    with open("", "w") as script:
        pass

print(all_destinations)
