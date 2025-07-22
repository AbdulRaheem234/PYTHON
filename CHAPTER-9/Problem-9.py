with open ("C:\\Users\\Admin\\OneDrive\\Desktop\\PYTHON\\CHAPTER-9\\this.txt") as f:
    content1 = f.read()

with open ("C:\\Users\\Admin\\OneDrive\\Desktop\\PYTHON\\CHAPTER-9\\this_copy.txt") as f:
    content2 = f.read()
if(content1 == content2):
    print("Yes these files are identical")
else:
    print("No these files are identical")            