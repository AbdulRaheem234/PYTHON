with open ("C:\\Users\\Admin\\OneDrive\\Desktop\\PYTHON\\CHAPTER-9\\old.txt") as f:
    content = f.read()
with open ("C:\\Users\\Admin\\OneDrive\\Desktop\\PYTHON\\CHAPTER-9\\renamed_by_python.txt", "w") as f:
    f.write(content)    