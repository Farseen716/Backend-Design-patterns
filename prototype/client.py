"""Prototype use case example code by Farseen Ashraf"""
"""This code all contains practice of deep and shallow copy"""
from document import Document

# Create a new Document containing a list of two lists
ORIGINAL_DOCUMENT = Document(name="Original", li=[[1, 2, 3, 4], [5, 6, 7, 8]])
print(ORIGINAL_DOCUMENT)
print()

Document_COPY_1 = ORIGINAL_DOCUMENT.clone(1)
Document_COPY_1.name = "Clone 1"

# This also modifies the original document because of using mode as 1
# when cloning the document
Document_COPY_1.list[1][2] = 200
print(Document_COPY_1)
print(ORIGINAL_DOCUMENT)
print()

Document_COPY_2 = ORIGINAL_DOCUMENT.clone(2)  # 2 level shallow copy
Document_COPY_2.name = "Clone 2"

# This does NOT modify the ORIGINAL_DOCUMENT because it changes the list[1]
# reference that was deep copied when using mode 2
Document_COPY_2.list[1] = [9, 10, 11, 12]
print(Document_COPY_2)
print(ORIGINAL_DOCUMENT)
print()

Document_COPY_3 = ORIGINAL_DOCUMENT.clone(2)  # 2 level shallow copy
Document_COPY_3.name = "Clone 3"

# This does change the ORIGINAL_DOCUMENT because it changes
# list[1][2] which was not deep copied recursively when using mode as 2

Document_COPY_3.list[1][2] = 12
print(Document_COPY_3)
print(ORIGINAL_DOCUMENT)
print()

Document_COPY_4 = ORIGINAL_DOCUMENT.clone(3)  # deep copy
Document_COPY_4.name = "Clone 4"

# This does not modify ORIGINAL_DOCUMENT because it
# deep copies all levels when using mode as 3

Document_COPY_4.list[1][2] = 20
print(Document_COPY_4)
print(ORIGINAL_DOCUMENT)
print()
