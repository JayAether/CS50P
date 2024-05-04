import pytest
from project import Note
import os

def test_note_initialization():
    note = Note()
    assert os.path.exists('notes')
    assert os.path.exists('pdf_notes')


def test_help_note():
    note = Note()
    assert note.help_note(None) == 'formilation > (command) (auxulary)\nauxulary > help: optional|add: mandatory|write: mandatory|delete: mandatory|find: nonexistant|pdf: mandatory|quit: nonexistant\nhelp > displays a list of commands and their functions\nadd > creates a new empty note\nwrite > acceses existing notes and writes to it\ndelete > deletes existing notes\nfind > displays all existing notes\npdf > turn selected note into a pdf\nquit > exits program'
    assert note.help_note('help') == 'help > displays a list of commands and their functions'
    assert note.help_note('eheh') == 'ERROR: auxulary for help needs to be an existing command, type "help" with no auxulary for the full list'


def test_add():
    note = Note()
    assert note.add('something') == 'note created succesfuly'
    assert note.add('something') == 'ERROR: file already exists'
    assert note.add('nothing') == 'note created succesfuly'
    assert os.path.exists('notes/something.txt')
    assert note.add(None) == 'ERROR: you must add and auxulary to use add'
    assert note.add('wh_at?') == 'ERROR: file contains numbers or alphabets'


def test_pdf():
    note = Note()
    assert note.turn_to_pdf('something') == 'pdf created succesfuly'
    assert os.path.exists('pdf_notes/something.pdf')
    assert note.turn_to_pdf('something') == 'ERROR: is already a pdf'
    assert note.turn_to_pdf('nono') == 'ERROR: file does note exist'
    assert note.turn_to_pdf(None) == 'ERROR: you must add and auxulary to use pdf'


def test_find():
    note = Note()
    assert note.find() == 'nothing something something.pdf '


def test_delete():
    note = Note()
    assert note.delete('something') == 'file seccesfuly deleted'
    assert note.delete('nothing') == 'file seccesfuly deleted'
    assert note.delete('nototo') == 'ERROR: file must exist'
    assert note.delete(None) == 'ERROR: you must add an auxulary to use delete'


def quit():
    note = Note()
    assert note.quit_note() == 'deactivated'

