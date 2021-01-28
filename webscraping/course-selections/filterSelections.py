def selectionRankFilter(selections, gradeFilter):
    filteredSelections = []
    for course in selections:
        if int(course['grade']) == gradeFilter: filteredSelections.append(course)

    selections = []
    for course in filteredSelections:
        print(course['name'], "-", course['course'])
        print(course['description'].replace(". ", ".\n"))
        while True:
            userInput = input("Would this be an interesting choice? [y/n] \n").lower()
            if userInput == "y":
                selections.append(course)
                break
            elif userInput == "n":
                break
            else:
                print("Invalid Option")
    return selections

def getInfo(selections):
    for course in selections:
        print(course['name'], "-", course['course'])

selections = eval(input("Paste LIST of selections. [{course1},{course2}] "))
gradeFilter = int(input("Which Grade to filter by? "))
while True:
    selections = selectionRankFilter(selections, gradeFilter)
    if input("ReFilter? [Y/n]").lower() == "n":
        break
getInfo(selections)
