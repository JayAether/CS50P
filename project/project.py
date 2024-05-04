from fpdf import FPDF
import os

class Note(FPDF):
    '''
    A class for managing notes and converting them to PDFs.

    This class extends FPDF to provide additional functionality for handling notes.
    It ensures the existence of necessary directories for storing notes and PDFs.
    '''
    def __init__(self):
        '''
        Initializes the Note class by ensuring the existence of 'notes' and 'pdf_notes' directories.

        If these directories do not exist, they are created.
        the functions in this class relies on these directories
        for storing notes and their PDF counterparts.
        '''
        super().__init__()
        if not os.path.exists('notes'):
            os.mkdir('notes')
        if not os.path.exists('pdf_notes'):
            os.mkdir('pdf_notes')

    def help_note(self, auxulary):
        '''
        returns a string explaining how a command works for the user.

        if auxulary is provided, returns just the single commands explination
        if auxulary was not provided. returns the full list of commands

        paramaters:
        auxulary (str, optional): the name of the command needed with help

        returns:
        str: full list of commands explination. only the command in auxulary explination.
        str: returns an error message if auxulary was provided and wasnt in existing_auxulary list.
        '''
        existing_auxulary = ('formilation', 'auxulary', 'help', 'add', 'write', 'delete', 'find', 'pdf', 'quit')
        command_list = {'formilation': '(command) (auxulary)',
                        'auxulary': 'help: optional|add: mandatory|write: mandatory|delete: mandatory|find: nonexistant|pdf: mandatory|quit: nonexistant',
                        'help': 'displays a list of commands and their functions',
                        'add': 'creates a new empty note',
                        'write': 'acceses existing notes and writes to it',
                        'delete': 'deletes existing notes',
                        'find': 'displays all existing notes',
                        'pdf': 'turn selected note into a pdf',
                        'quit': 'exits program',
                        }

        if auxulary:
            if auxulary in existing_auxulary:
                return f'{auxulary} > {command_list[auxulary]}'
            else:
                return 'ERROR: auxulary for help needs to be an existing command, type "help" with no auxulary for the full list'
        else:
            holder = ''
            for key, value in command_list.items():
                holder += f'{key} > {value}\n'
            return holder.strip()

    def add(self, note_name):
        '''
        creates a .txt file in notes directory named after note_name

        parameters:
        note_name (str): the name of the file to be created. must be alnum

        returns:
        str: returns a conformation that the note was created succesfuly
        str: returns an error massage if note_name was not alnum, note_name already existed, note_name was note given
        '''
        if not note_name:
            return 'ERROR: you must add and auxulary to use add'

        if not note_name.isalnum():
            return 'ERROR: file contains numbers or alphabets'

        if os.path.exists(f'notes/{note_name}.txt'):
            return 'ERROR: file already exists'
        else:
            with open(f'notes/{note_name}.txt', 'w'):
                return 'note created succesfuly'

    def write(self, note_name):
        '''
        writes into the .txt file per note_name in notes directory

        appends to the file one line per line
        exits note if entered a blank line

        parameters:
        note_name (str): the name of the file to be writen in. must exist as a file

        returns:
        str: returns 'you have exited write mode' when exiting file
        str: returns an error message if file note_name doesnt exist, if var note_name wasnt given
        '''
        if not note_name:
            return f'ERROR: you must add and auxulary to use write: Note().write()'

        if os.path.exists(f'notes/{note_name}.txt'):
            with open(f'notes/{note_name}.txt', 'a') as file:
                while True:
                    sentance = input('<=>')
                    if not sentance:
                        return 'you have exited write mode'
                    file.write(f'{sentance}\n')
        else:
            return f'ERROR: file {note_name} does not exist'

    def delete(self, note_name):
        '''
        deletes .txt file note_name in notes directory

        asks if you want to delete file (y/n),
        if y, deletes file and returns 'file secsesfuly deleted', if n, returns 'deletion canceled'

        parameters:
        str (str): the name of the file to be deleted. must exist as a file

        returns:
        str: 'deletion canceled' if deletion was canceled. 'file secsesfuly deleted' if deletion was continued
        str: returns an error message if note_name was not provided or note with note_name does not exist returns a str with 'ERROR:'
        '''
        if not note_name:
            return 'ERROR: you must add an auxulary to use delete'

        if os.path.exists(f'notes/{note_name}.txt'):
            os.remove(f'notes/{note_name}.txt')

            if os.path.exists(f'pdf_notes/{note_name}.pdf'):
                os.remove(f'pdf_notes/{note_name}.pdf')

            return 'file seccesfuly deleted'
        else:
            return 'ERROR: file must exist'

    def find(self):
        '''
        returns a str of all files in notes dir for display

        returns:
        str: just the file names without .txt
        '''
        all_files = os.listdir('notes/') + os.listdir('pdf_notes/')

        files = ''
        for selected_file in all_files:
            files += selected_file.replace('.txt', '') + ' '
        return files

    def turn_to_pdf(self, note_name):
        '''
        turns selected file into a pdf

        parameters:
        note_name (str): the name of the file to be turned to pdf

        returns:
        str: an error message if file note_name does not exist
        '''
        if not note_name:
            return 'ERROR: you must add and auxulary to use pdf'

        if not os.path.exists(f'notes/{note_name}.txt'):
            return 'ERROR: file does note exist'

        if os.path.exists(f'pdf_notes/{note_name}.pdf'):
            return 'ERROR: is already a pdf'

        pdf = FPDF()

        pdf.add_page()

        pdf.set_font("Arial", size = 12)

        with open(f'notes/{note_name}.txt') as note:
            for line in note:
                pdf.cell(10, 8, line, ln=True)

        pdf.output(f'pdf_notes/{note_name}.pdf')
        return 'pdf created succesfuly'


    def quit_note(self):
        '''
        returns a str that is deticted and quits the loop

        returns:
        str: the str that is looked for in every loop
        '''
        return 'deactivated'

    def commands(self, commands):
        '''
        calls functions depending on the users input

        parameter:
        commands (str): must be length of 1 or 2, if 0 returns an empty string.

        returns:
        str : if commands length more than 2 returns an error message
        str: returns an error message if command doesnt exist
        str: returns the return value of the function called
        '''
        if len(commands) == 0:
            return ''
        if len(commands) > 2:
            return 'ERROR: parameter must be either one or two'
        elif len(commands) == 1:
            command = commands[0]
            auxulary = None
        elif len(commands) == 2:
            command = commands[0]
            auxulary = commands[1]

        match command:
            case 'help':
                return self.help_note(auxulary)
            case 'add':
                return self.add(auxulary)
            case 'write':
                return self.write(auxulary)
            case 'delete':
                return self.delete(auxulary)
            case 'find':
                return self.find()
            case 'pdf':
                return self.turn_to_pdf(auxulary)
            case 'quit':
                return self.quit_note()
            case _:
                return 'ERROR: command does not exist, type "help" for existing commands'


def main():
    note = Note()

    print('type "help" for help')
    status = True
    while status:
        user_command = input('--').strip().split()
        command = note.commands(user_command)

        if command:
            print(command)

        if command == 'deactivated':
            status = False


if __name__ == '__main__':
    main()
