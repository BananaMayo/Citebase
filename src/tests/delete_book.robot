*** Settings ***
Resource  resources.robot

*** Test Cases ***
Deleting One Book
    Add Book  Harry Potter  JK Rowling  2000  Otava
    Add Book  Tirakirja  Antti Laaksonen  2020  HY
    Input  delete book
    Input  Tirakirja
    Input  list books
    Input  exit
    Run Application
    Output Should Contain  Harry Potter
