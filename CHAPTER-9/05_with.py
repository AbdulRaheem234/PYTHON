f = open("C:\\Users\\Admin\\OneDrive\\Desktop\\PYTHON\\CHAPTER-9\\file.txt", "r")
print(f.read())
f.close()
with open("C:\\Users\\Admin\\OneDrive\\Desktop\\PYTHON\\CHAPTER-9\\file.txt", "r") as f:
    print(f.read())
