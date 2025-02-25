# More strings and text

x = "There are %d types of people." %10
# defined x and gave %d a vaule of 10
binary = "binary"
# made binary equal to binary
doNot = "don't"
# made doNot = "don't"
y = "Those who know %s and those who %s" % (binary, doNot)
# I made y a sentence and with vaules I filled in with binary, doNOt

print(x)
# printed out x definition
print(y)
# printed out y definition

print("I said %r.:" %x)
# made the computer quote my x definition
print("I also said: '%s'." %y)
# then made the computer quote my y def.
hilarious = True
# made any time I said hilarious to be equal to True
jokeEvalution = "Isn't that joke so funny?! %r"
# make jokeeva. to equal a certain phrase

print(jokeEvalution % hilarious)
# had comp. print jokeeva. and hilarious

w = "This is the left side of..."
# made w equal to certain phrase
e = " a string with a right side"
# made e equal to certain phrase
print(w+e)
# had comp. combine w and e phrases

# More printing fun
print("Mary had a little lamb")
#
print("Its fleece was white as %s" % 'snow')
print("And everywhere that Mary went")
print("." * 10)
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

print(end1 + end2 + end3 + end4 + end5 + end6)
print(end7 + end8 + end9 + end10 + end11 + end12)

# But wait! There's more:
formatter = "%r %r %r %r"
print(formatter % (1, 2, 3, 4))
print(formatter % ("one", "two", "three", "four"))
print(formatter % (True, False, True, False))
print(formatter % (formatter, formatter, formatter, formatter))

# why did I use%r instead of %s in the above example?

# which should I use on a regular basis
# using %s would be fine but if you wanted to use %r you could but it would give you exactly what you typed onto the python file

# why does %r sometimes give me a single quotes around things?

pies = "Blu Che Key Cho Cra App"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print("Here are different pies: ", pies)
print("Here are the months: ", months)

print("""
There's something going on here.
With three double quotes.
We"ll be able to type as much as we like.
Even 4 lines if we want. or 10, or 100
""")

# examine clearly the difference between the %r formatter and %s formatter
print("Here are the months: %r" % months)
# ^ gives you exactly what you typed
print("Here are the month: %s" % months)
# ^ creates a list for your values and puts each value on a new line

# escape sequences redux
bigdog = "\t I'm a big boy"
smalldog = "\t I'm \n small dude"
fatdog = "\t I'm \\ fat \r dog"
skinnydog = """
I'll do a list:
\t dog food
\t* Bones
\t* Yard\n\t* Grass
"""
print(bigdog)
print(smalldog)
print(fatdog)
print(skinnydog)
dude = "dude"

# Escape Seq                   What it Does?
# \\
"\\ dude"
#^ creates a backslash
# \'
"\' dude"
# ^ gives an ' for something
# \"
"\" dude"
# gives quotation marks for a line
# \a
"\a dude"
#^ creates a bell
# \b
"\b dude"
# ^ makes a backspace
# \f
"du \f de"
# ^ makes a question mark in box
# \n
"\' dude"
# ^ creates a new line
# \N{name}
"\' dude"
# ^ creates a name within the database
# \r
"\r dude"
# ^ does a return
# \t
"\t dude"
# ^ tabs the line
# \uxxxx
print("\u6465")
# ^ converts four hexadecimal value into a character
# \Uxxxxxxx
# ^ converts hex values to letters but must be eight hexadecimal values
# \v
print(" du\vde")
# ^ creates a box with with a symbol in it
# \ooo
print("\110\145\154\154\157")
# ^ converts octal values to letters
# \xhh
print("\x48\x65\x6c\x6c\x6f")
# ^it translates hexadecimal values into letters

# What dos the following code block do: it continues to go until you stop it
#       while True:
#           for i in{ "/" , "-", "\", "\\", "|"}:
#           print("%s\r" % i, end='')

# ^ creates an endless loop that goes on until you press the stop button in the top right

# Can you use ''' instead of """? Yes
print('''hello
dog 
boy''')



age = input("how old are you")
height = input("How tall are you?")

print("So are %r old and %r tall" % (age, height))

# ask 4 more questions and handle those reponses12

pie = input("Do you like pie")
flavor = input("What flavor do you like")
crust = input("Do you like the crust on pie")
cake = input("Is pie supierior to cake?")

print(pie, flavor, crust, cake)

print("Hello and welcome to story time with Jeff.")

character = input("Once there was a")
action = input("and they were amazing at..")
adjective = input("but they were ...")
print("Let's recap our character is %r and their talent is %r but they are %r." % (character, action, adjective))
quest = input("Now our %r began his quest for" % (character))
value = input("which was valuable due to its")
location = input("that was located in")
evil = input("and a/an ")
print("was guarding the %r" % (quest))
attempt = ("our %r finally reached %r for his quest but " % (character, quest))
print("at %r and " % (location))
problem = input("which lead to %r to(verb)" % (character) )
print("during their quest")
final = ("%r ended up " % (character))
print("Once there was a %r and they were amazing at %r but they were %r" % (character, action, adjective))
print("%r began his quest for %r which was valuable due to its %r and was located in %r with a/an %r guarding the %r" % (character, quest, value, location, evil, quest))
print("This lead to %r to %r during their quest. %r with %r" % (character, problem, character, final))
