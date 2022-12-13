
def list_command_names(io):
    names = ["\u001b[0mexit", "\u001b[32mnew book", "\u001b[35mlist books", "\u001b[33mdelete book", "\u001b[31mdelete all", "\u001b[36mexport", "\u001b[34mimport"]
    io.print('\n'.join(names))
    io.print(" ")
