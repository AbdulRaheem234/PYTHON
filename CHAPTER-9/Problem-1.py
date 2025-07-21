f = open("C:\\Users\\Admin\\OneDrive\\Desktop\\PYTHON\\CHAPTER-9\\poem.txt", "r")
content = f.read()
if("Twinkle" in content):
    print("The word twinkle is present in the content")
else:
    print("The word twinkle is not present in the content")    
f.close()