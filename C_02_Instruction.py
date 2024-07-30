def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration}")


def instructions():
    print("Instructions go here...")


statement_generator( statement="Instructions",decoration= "- ")


print('''
Instructions go here
- instructions 1
- instructions 2
- etc
    ''')


want_instructions = input("Press <ENTER> to read the instructions " 
                          "or any key to continue ")

if want_instructions == "":
    instructions()

print("Program Continues")
