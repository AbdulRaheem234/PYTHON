with open ("C:\\Users\\Admin\\OneDrive\\Desktop\\PYTHON\\CHAPTER-9\\this.txt") as f:
    content = f.read()
with open ("C:\\Users\\Admin\\OneDrive\\Desktop\\PYTHON\\CHAPTER-9\\this_copy.txt", "w") as f:
    f.write(content)    