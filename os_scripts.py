import os
#
# # 1. Create a directory.
# # - so we can start manipulating it, and this is where we will store the code that we ll use.
# # Directory
directory = "test_dir"
#
# #  Set a parent directory(for the one above)
parent_dir = "C:/Users/flori"
#
# #  Path
path = os.path.join(parent_dir, directory) # first parent directory, and then the actual directory
#
# #  Create the directory
#
# os.mkdir(path)
# print("Directory '%s' created" % directory) # % = what`s come out previously.


# 2. Make a new file.

filename = "testfile.txt"
filepath = os.path.join(path, filename)

# Write to the new file
with open(os.path.join(path, filename), "w") as file1: # with = allows you to use certain functions within python. "w" = write. as = within. file1 = variable created to store data.
    toFile = "Contents of my new file." # toFile = holds the content.
    file1.write(toFile)
print("File" + filename + "created in " + directory)




