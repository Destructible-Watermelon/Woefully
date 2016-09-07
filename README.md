# Woefully
For the esolang Woefully

###Woefully is a 2d language, with two stacks, and two pointers. It is different to other 2d languages, but hard to explain easily.

The pointers are a char pointer and an instruction pointer. the instruction pointer goes down paths of spaces, executing commands. the char pointer stays stationary unless moved by commands. when the instruction pointer finds the end of the path, it goes back to the char pointer, finds the next path of spaces (which could be the one just executed), and goes down it, executing commands again. Moving the char pointer is the only control flow. conditionals do not exist, apart from a command that pops a value, and pushes 1 if it isn't zero, and pushes zero if it is. Combine the char pointer movement and the not zero command and you have real control flow.
