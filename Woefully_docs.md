#Woefully docs!

Before we talk what's in a program, let's talk about what's not. There are no characters but newlines, pipes, and spaces. There are no spaces next to newlines, or newlines next to spaces etc. Programs that have these will produce output "confuse :("

On the program, there are two pointers. Char pointer, and instruction pointer. The CP (char pointer) starts at the first char, and the IP starts at the CP. The ip moves across the lines until it finds a space, if there is no space on the current line, it will try the next line, etc. the top line is considered next to the bottom line for these purposes. Note that a program with no spaces produces the output "confuse :(". Once it finds a space, it will try to navigate down it as a path. navigation works like this: it checks if there is a space in the three adjacent squares below it:

     #
    /|\
if there is, it will go to the first one there. if there is not, it halts the program.
it will keep going in this direction, until there are no spaces in that direction anymore:

    (lines denote the spaces it checks)
                 #
                /|\
               /
              /
    (line end)|\
              |
             /|\
     (no more spaces near this space)

When it finds the end of the line in that direction, it executes a command based on the value. if the value is 2, it is a nop. if it greater than 2, execute a command (see below)

When the entire path ends, as in the example above, after the line ends, the ip is set to the cps position

---
Woefully uses stacks for its data

**There are two stacks, A and B**

Stacks start initialised with a single zero

Stack A is the main stack, and stack B is very much a secondary place to store data temporarily. All push commands are to A, except dupe, and A to B


-----
##Types of commands: down, diagonally down left, diagonally down right

**All two length commands are nops**

**Commands subtract three because the minimum length of a command is three because length two is a nop**

###DDL (diagonally down left)
path length is taken, minus three, pushed to stack A



###DOWN
river length is taken, minus three, mod 4,
then taken from this table

| |name|what it does|
|:-:|:-:|:-:|
|0|AtoB|pop a from A, push a to B    |
|1|diff|pop a from A, b from B, push a-b to A|
|2|mult|pop a from A, b from B, push a*b to A|
|3|dupe|peek a from A, push a to B   |


###DDR
take the length of a DDR river, subtract three, mod 5, then take from this table

moving works with negative integers; it moves back. Moving wraps at the line, and moves down a line, like regular text. it also wraps at the end, to the start.

| |name|what it does|
|:-:|:-:|:-:|
|0|move|pop a from A, move pointer by a|
|1|bool|pop a from A, push 1 if a!=0, else 0   |
|2|inpt|push input to A          |
|3|otpt|pop a from A, print a   |
|4|swap|swap decimal/text i/o (text supports utf-8)|
