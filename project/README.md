# Note Manager
#### Video Demo: sorry, kinda private. i still sent it to harvard though! 
#### Description:

## note manager is used to manage notes, create notes, write notes, turn notes into pdfs, deletes notes.

### `Note()` class
when running note manager, the `__init__` of the class `Note()` checks if the directory `notes/` and the directory `pdf_notes/`.
contains multiple functions that mostly revolve around notes.

### `main()` function
when the file is run, the program prints `'type "help" for help'` from the `main()` function before starting a `while` loop that promts the user for input infinitly.
`input('--').strip().split()` is used to prompt the user before calling the function with `print(note.commands())` as its input to then print it after being called.
checks if the str is 'deactavated', if so breaks the while loop by turning `status` var from `'True'` to `'False'`

### `Note().commands()` function
the `Note().commands()` function is used to call other functions depending on the given argument, if first argument given is not within existing commands, returns a error message str. defults to `None` if no aditional args where given.
takes a list and returns a `''` to be prompted if the list was empty where given, if only one string is in the list is given it assains the argument to `command` var and assains `auxulary` to `None`. if a list of two where given, it assains the first arg to `command` while the second to `auxulary`. if more than two where given an error message str would be returned.
commands that are accepted when given by the user include: `'help'` `'add'` `'write'` `'pdf'` `'find'` `'delete'` `'quit'`. these commands, in str form, call other functions withing the class. returns an error message str if the command given was not within possible commands

### `Note().help_note()` function
`Note().help_note()` takes an optional arg, the arg isnt technecly optional but it is put to be `None` if no auxulary arguments are called by the `Note().commands()` function.
if no auxulary args is `None` (aka the user didnt put any auxulry) it returns a full list of all the help lines there are-
> auxulary > help: optional|add: mandatory|write: mandatory|delete: mandatory|find: nonexistant|pdf: mandatory|quit: nonexistant
> help > displays a list of commands and their functions
> add > creates a new empty note
> write > acceses existing notes and writes to it
> delete > deletes existing notes
> find > displays all existing notes
> pdf > turn selected note into a pdf
> quit > exits program
if an auxulary was given, it would check if it is within existing commands, if so returns the help line per the list of lines above.
eg. `help_note('help')`
> help > displays a list of commands and their functions
if an auxulary was given but it isnt an existing command, returns an error message str

### `Note.add()` function
`Note().add()` takes an mandatory arg.
returns an error message str if the file already exists, is not alnum, or if no args where given.
return 'note created succesfuly' when run succesfuly.

### `Note.write()` function
`Note().write()` takes an mandatory arg.
keeps prompting the user infinitly for input one line at a time to append into the file. exits loop if a blank line was inputed. returns 'you have exited write mode' when exiting
returns an error message str if the file doesnt exists, or if no args where given.

### `Note.delete()` function
`Note().delete()` takes an mandatory arg.
deletes file in `notes/` and `pdf_notes/` dir if they exist. returns 'file seccesfuly deleted' if deleted succesfuly
returns an error message str if file doesnt exist, if no auxulary was given

### `Note.find()` function
`Note().find()` doesnt take any argument.
returns all the existing notes and pdfs

### `Note.turn_to_pdf()` function
`Note().turn_to_pdf()` takes an mandatory arg.
turns the file per the arg to a pdf. returns 'pdf created succesfuly' str if created succesfuly
return an error message if file does not exist, arg was not given, pdf of file already exists

### `Note.quit_note()` function
`Note().quit_note()` doesnt take any argument.
only returns 'deactavated' str that is detected in the main() func and ends the loop

