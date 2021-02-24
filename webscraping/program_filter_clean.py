# filter and convert...

from os import listdir
directory = "./test/"

files = []
for file in listdir(directory):
    if ".txt" in file and "dictionary" not in file:
        files.append(file)

for file in files:
    programs = []
    with open(directory+file, "r") as f:
        f = eval(f.read())

    for x in range(0, len(f), 4):
        currentProgram = f[x:x + 4]
        currentProgram[3] = currentProgram[3][0]
        for information in currentProgram:
            popList = []
            for index, string in enumerate(information):
                # directly strip
                information[index] = string.strip()
                # calculate emptys
                if string == "": popList.append(index)
            # reverse pop to not mess with indexes
            popList.reverse()
            [information.pop(index) for index in popList]
            while "" in information: information.remove("")
        programs.append(currentProgram)

    # now we have them in list form and cleaned up, its time to put them into dictionaries
    programDictionaries = []
    programDictDetailKeys = ["education", "credential", "length", "coop", "parttime"]
    programDictDetailSearchValues = ["Education Required", "Credentials Awarded", "Program Length", "Co-op Option",
                                     "Part Time Study Option"]
    programDictExpenseKeys = ["tuition-canadian", "tuition-international", "residence-cost", "meal-plan-cost"]
    programDictExpenseSearchValues = ["Tuition (In-Province)", "Tuition (International)", "Residence Cost",
                                      "Meal Plan Cost"]
    for currentProgram in programs:
        programDict = {}
        programDict["name"] = currentProgram[0][0]
        programDict["institution"] = currentProgram[0][1]

        # search for programDetails...
        programDetails = currentProgram[1]
        for index, key in enumerate(programDictDetailKeys):
            programDict[key] = programDetails[programDetails.index(programDictDetailSearchValues[index]) + 1]

        programExpenses = currentProgram[2]
        for index, key in enumerate(programDictExpenseKeys):
            programDict[key] = programExpenses[programExpenses.index(programDictExpenseSearchValues[index]) + 1]

        programDict["course-req"] = currentProgram[3]

        programDictionaries.append(programDict)

    with open(directory+"dictionary"+file, "w") as f:
        f.write("\n".join([str(x) for x in programDictionaries]))
