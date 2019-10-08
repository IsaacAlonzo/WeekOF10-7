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

# examine clearly the difference between the %r formatter and 5s formatter
print("Here are the months: %r" % months)
print("Here are the month: %s" % months)

# escape sequences redux
bigdog = "\t I'm a big boy"
smalldog = "\t I'm \n small dude"
fatdog = "\t I'm \\ fat \\ dog"
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
"\' dude"
# \b
"\' dude"
# \f
"\' dude"
# \n
"\' dude"
# ^ creates a new line
"\' dude"
# \N{name}
"\' dude"
# \r
"\' dude"
# \t
"\' dude"
# \uxxx
"\' dude"
# \Uxxxxxxx
"\' dude"
# \v
"\' dude"
# \ooo
"\' dude"

# \xhh
"\' dude"

