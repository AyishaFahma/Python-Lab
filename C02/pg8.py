def longestLength(words):
    finalList=[]
    for word in words:
        finalList.append((len(word), word))
    finalList.sort()
    print("The word with the longest length is:", finalList[-1][1],
            " and length is ", len(finalList[-1][1]))
    print (finalList)
# Driver Program
a = ["one", "two", "third", "four"]
longestLength(a)
