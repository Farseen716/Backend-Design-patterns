# Composite design pattern use case by Farseen Ashraf

from folder import Folder
from file import File

filesystem = Folder("root")
file_1 = File("abc.txt")
file_2 = File("123.txt")
filesystem.attach(file_1)
filesystem.attach(file_2)
folder_a = Folder("folder_a")
filesystem.attach(folder_a)
file_3 = File("xyz.txt")
folder_a.attach(file_3)
folder_b = Folder("folder_b")
file_4 = File("456.txt")
folder_b.attach(file_4)
filesystem.attach(folder_b)
filesystem.dir()


# Now move folder_a and its contents to folder_b
folder_b.attach(folder_a)
filesystem.dir()
