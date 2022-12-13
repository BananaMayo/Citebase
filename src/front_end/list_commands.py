
def list_command_names(io):
    commands = [("\u001b[1;38;5;064mexit", "\u001b[0;000mExit app"), 
                ("\u001b[1;38;5;084mnew book", "\u001b[0;000mAdd new book"),
                ("\u001b[1;38;5;221mlist books", "\u001b[0;000mList all books"),
                ("\u001b[1;38;5;208mdelete book", "\u001b[0;000mDelete single book"),
                ("\u001b[1;38;5;196mdelete all", "\u001b[0;000mDelete all books"),
                ("\u001b[1;38;5;039mexport", "\u001b[0;000mExport all books to bib file"),
                ("\u001b[1;38;5;092mimport", "\u001b[0;000mImport all books from bib file")
                ]
    for command, explanation in commands:
        io.print(f"{command:26} {explanation}")

