from database import *

print("\n")
boardNamesList = []
for i in range(len(allData)): 
    bucketNames = []
    print("\n")
    print("-----------------------------------------------------------------------------------------------------------------")
    for j in range(len(allData[i][0])):
        if j == 0:
            boardName = allData[i][0][0]  # this is the Board's name
            boardName = boardName.replace("あ"," ")
            boardNamesList.append(boardName)
            print("\nBoard Title: ")
            print(boardName)
        else:
            bucketNames.append(allData[i][0][j].replace("あ"," ")) # the names of buckets for the respective board
    print("\nCard Title, Card Description, Bucket Name1, Bucket Name2,...,Bucket NameN: ")
    print(bucketNames, "\n")
    print("Card Title, Card Description, inBucket1, inBucket2,..., inBucketN: ")
    for k in range(len(allData[i])):
        cardInfo = []
        if k>0:
            for card in range(len(allData[i][k])):
                cardInfo.append(allData[i][k][card]) # all the info for each card.
            print(cardInfo)