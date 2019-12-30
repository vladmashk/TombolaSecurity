import random

# ticketAmount is amount of tickets
# secNbLength is length of security number ! Recommended length is 6 or higher !
# previousKeyListLength is length of the list of the previously generated keys if available
#
# Creates the file TombolaKeys.txt in source folder
def generateTicketList(ticketAmount, secNbLength, previousKeyListLength = 0):

    file = open("TombolaKeys.txt", "w+")
    keyList = []
    characterList = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
                     "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w","x", "y", "z", "A", "B", "C", "D",
                     "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q","R", "S", "T", "U", "V", "W", "X",
                     "Y", "Z"]
    secure_random = random.SystemRandom()
    securityNumber = ""

    for ticketNumber in range(1 + previousKeyListLength, ticketAmount + 1 + previousKeyListLength):
        for i in range(secNbLength):
            securityNumber += secure_random.choice(characterList)

        if ticketNumber < ticketAmount:
            file.write(str(ticketNumber) + "\t" + securityNumber + "\n")
        else:
            file.write(str(ticketNumber) + "\t" + securityNumber)
        keyList.append(securityNumber)
        securityNumber = ""

    file.close()
    return keyList



# Check that no duplicates exist in keyList + previousKeyList
def noDuplicatesTest(keyList, previousKeyList = []):
    mergedList = list(keyList) + list(previousKeyList)
    keySet = set(mergedList)
    if len(mergedList) == len(keySet):
        print("No duplicate(s) found")
    else:
        print("Duplicate(s) found")
        print("Amount of Duplicates:", len(mergedList) - len(keySet))



# Returns the security keys as list from the TombolaKeys.txt file
def readList():
    file = open("TombolaKeys.txt", "r")
    keyList = []

    for line in file:
        keyList.append(line.split()[1])

    return keyList

# =======================================================================

myKeyList = generateTicketList(10000, 6)
noDuplicatesTest(myKeyList)

# previousKeys = readList()
# myKeyList2 = generateTicketList(5000, 6, len(previousKeys))
# noDuplicatesTest(myKeyList, myKeyList2)


print("")
input("Press any key to exit")