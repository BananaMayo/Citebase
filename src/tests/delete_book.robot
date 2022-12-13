*** Settings ***
Resource  resources.robot
Test Setup  Add Default Books

*** Test Cases ***
User Can Delete Single Book
    Input  delete book
    Input  Tirakirja
    Input  list books
    Input  exit
    Run Application
    Output Should Contain  Harry Potter
    Output Should Not Contain  Tirakirja

User Can Delete All Books
    input  delete all
    input  list books
    input  exit
    run application
    Output Should Not Contain  Harry Potter
    Output Should Not Contain  Tirakirja
    output should contain  No book titles!

*** Keywords ***
Add Default Books
    Add Book  Harry Potter  JK Rowling  2000  Otava
    Add Book  Tirakirja  Antti Laaksonen  2020  HY