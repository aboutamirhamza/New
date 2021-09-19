# 16. Input a fruit name , if fruit name start with vowel print 
# “this is an fruit_name” else, this is a fruit_name
# Example:
# Input: Enter a fruit name: “apple”
# Output: “this is an apple”
# Input: Enter a fruit name: “banana”
# Output: “this is a banana
# Without If Else

# a = input("Enter fruit name: ")
# print("this is an",a)

# With If Else
b = input("Enter fruit name: ")
if b[0] == "a" or b[0] == "e" or b[0] == "i" or b[0] == "o" or b[0] == "u":
    print("this is an",b)
elif b[0] == "A" or b[0] == "E" or b[0] == "I" or b[0] == "O" or b[0] == "U":
    print("this is an",b)
else:
    print("this is a",b)