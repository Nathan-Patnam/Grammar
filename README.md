# Context Free Grammar

Write a Python program (call it grammar.py) by completing the following steps:
In whichever approach you wish, have your program read in a text file called grammar.txt and construct a Grammar. This file will contain data that describes an Grammar.

The structure of grammar.txt will be as follows:

- Line 1: the variables of the grammar (separated by commas, if there is more than one state)
- Line 2: the terminals of the grammar (separated by commas, if there is more than one symbol)
- Line 3: the start symbol of the grammar
- Line 4 and onward: the grammar rules, where each rule takes the form A->B.

  - A will be the variable of the rule
    - B will be all the possible variable/terminal combinations. The empty string is denoted with a "@"
    -An example would be:


After your program constructs a grammer, read in another file called input.txt, where each line in the file is a string that will run on your grammer.

Both grammer.txt and input.txt should be assumed to be in the same directory as your Python program.

Simulate each string in input.txt using your grammer, and write the output (accept or reject) into a new file called output.txt (also in the same directory as your Python program, and each result on a new line).