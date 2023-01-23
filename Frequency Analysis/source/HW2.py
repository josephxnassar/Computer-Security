with open ("question2.txt", "r") as infile:
    linesAsList = infile.readlines()

freq = dict()

mostFreqEnglish = ["e", "t", "a", "o", "i", "h", "n", "s", "r", "d", "l", "u", "w", "g", "c", "y", "m", "f", "p", "b", "k", "v", "q", "x", "j", "z"]

# Create dict with keys A,B,...,Z
for i in range(26):
    freq[chr(i + 65)] = 0

strippedList = list()

# Remove "\n"
for line in linesAsList:
    strippedList.append(line.strip())

# Increase freq for corresponding letter
for line in strippedList:
    for letter in line:
        if letter != "?":
            freq[letter] = freq[letter] + 1

print(freq)

# Sort freq dictionary
sort = dict(reversed(sorted(freq.items(), key = lambda item : item[1])))

print(sort)

key = dict()

mostFreqKeys = list(sort.keys())

# Get substitution key
for i in range(26):
    key[mostFreqKeys[i]] = mostFreqEnglish[i]

print(key)

plainTextList = list()

# # Cipher to plaintext
# for line in strippedList:
#     for i in range(26):
#         line = line.replace(mostFreqKeys[i], mostFreqEnglish[i])
#         line = line.replace("?", " ")
#     plainTextList.append(line)

# Alternative Cipher to plaintext
for line in strippedList:
    temp = str()
    for letter in line:
        if letter != "?":
            temp += key[letter]
        else:
            temp += (" ")
    plainTextList.append(temp)

# Output to file
with open("plaintext.txt", "w") as outfile:
    for line in plainTextList:
        outfile.write(line + "\n")
