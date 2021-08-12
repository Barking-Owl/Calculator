text = input("Enter text: ")
rev = text[::-1]
print("Your reversed word: ")
print(rev)

shuf = text[len(text)-1] + text[1:len(text)-1] + text[0]
print("Swapping the first and last letters of the word (not reversed): ")
print(shuf)

revShuf = rev[len(rev)-1] + rev[1:len(rev)-1] + rev[0]
print("Swapping the first and last letters of the word (reversed): ")
print(revShuf)
