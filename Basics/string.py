
# Entering Strings with Different Quotes
print("This is a string using a double quote")
print("This is a string using a single quote")
print("""This string has
         three quotes look at
         what it can do!""")
# backslash (\), or escape character ->treat the double quote as a character
print("I said, \"Don’t do it\"")
print(" Roses are red \n Violets are blue \n I just printed multiple lines \n And you did too!")
print("John" + "Everyman")
print("John"  " Everyman")
print("John Q. %s" % ("Public"))
print("John %s %s" % ("Every" , "Man"))
#10s give the string space 10 to the left
print("%s %s %10s" % ("John" , "Every", "Man"))
#-5s give the string space 5 to the right
print("%-5s %s %10s" % ("John" , "Every", "Man"))
