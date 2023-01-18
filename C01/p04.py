#4.count the occurence of each word in line of text

def word_count(str):
    counts=dict()
    words=str.split()
    print(words)
    for word in words:
        if word in counts:
            counts[word]+=1
        else:
            counts[word]=1
    return counts
print(word_count("the quick brown fox  jumbs over the lazy dog"))
