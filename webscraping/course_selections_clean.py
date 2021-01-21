with open("scrapped.txt","r") as file:
    file = eval(file.read())

courseList = []
for string in file:
    dictionary = {}
    currentList = string.split("\n")
    for index, key in enumerate(["name", "grade", "course", "credit"]):
        if key == "credit":
            dictionary[key] = currentList[index][0]
        elif key == "grade":
            dictionary[key] = currentList[index][-2:]
        else:
            dictionary[key] = currentList[index]
    dictionary["description"] = " ".join(currentList[4:]).strip()
    courseList.append(str(dictionary) + "\n")

with open("scrapped.txt","w") as file:
    file.writelines(courseList)
