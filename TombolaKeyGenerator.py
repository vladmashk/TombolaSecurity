import random

"""
Create the file TombolaKeys.txt in source folder

ticketAmount: amount of tickets
secNbLength: length of security number ! Recommended length is 6 or higher !
previousKeyListLength: length of the list of the previously generated keys if available

output: creates file TombolaKeys.txt in source folder
"""
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


"""
Return amount of duplicates in keyList + previousKeyList (can be left blank)
"""
def noDuplicatesTest(keyList, previousKeyList = []):
    mergedList = list(keyList) + list(previousKeyList)
    keySet = set(mergedList)
    if len(mergedList) == len(keySet):
        return 0
    else:
        return len(mergedList) - len(keySet)


"""
Return the security keys as a list from the TombolaKeys.txt file in source folder
"""
def readList():
    file = open("TombolaKeys.txt", "r")
    keyList = []

    for line in file:
        keyList.append(line.split()[1])

    return keyList


# Example

#myKeyList = generateTicketList(100, 6)
#print(noDuplicatesTest(myKeyList), "duplicate(s) found")

# previousKeys = readList()
# myKeyList2 = generateTicketList(400, 6, len(previousKeys))
# print(noDuplicatesTest(myKeyList, myKeyList2), "duplicate(s) found")