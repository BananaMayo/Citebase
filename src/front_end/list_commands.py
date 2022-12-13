
def list_command_names(io):
    commands = [("\u001b[00mexit", "\u001b[00mExit app"), 
                ("\u001b[32mnew book", "\u001b[00mAdd new book"),
                ("\u001b[35mlist books", "\u001b[00mList all books"),
                ("\u001b[33mdelete book", "\u001b[00mDelete single book"),
                ("\u001b[31mdelete all", "\u001b[00mDelete all books"),
                ("\u001b[36mexport", "\u001b[00mExport all books to bib file"),
                ("\u001b[34mimport", "\u001b[00mImport all books from bib file")
                ]

    for command, explanation in commands:
        io.print(f"{command:20} {explanation}")

