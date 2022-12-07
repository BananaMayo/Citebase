*** Settings ***
Library  ../AppLibrary.py

*** Test Cases ***
Application starts with prompt
    input  exit
    Run Application
    Output Should Contain  next command (new book, list books, exit, delete book, delete all):

Application indicates empty list in listing
    input  list books
    input  exit
    Run Application
    Output Should Contain  No book titles!

Adding New Book Is Listed
    input  new book
    input  Harry Potter2
    input  JK Rowling
    input  2000
    input  Otava
    input  list books
    input  exit
    Run Application
    Output Should Contain  Harry Potter2