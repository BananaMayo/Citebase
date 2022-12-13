*** Settings ***
Library  ../AppLibrary.py
Resource  resources.robot

*** Test Cases ***
Application Indicates Empty List In Listing
    input  list books
    input  exit
    Run Application
    Output Should Contain  No book titles!

Adding New Book Is Listed
    Add Book  Harry Potter  JK Rowling  2000  Otava
    input  list books
    input  exit
    Run Application
    Output Should Contain  Harry Potter
