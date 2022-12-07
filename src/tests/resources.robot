*** Settings ***
Library  ../AppLibrary.py

*** Keywords ***
Add Book
    [Arguments]  ${title}  ${author}  ${year}  ${publisher}
    Input  new book
    Input  ${title}
    Input  ${author}
    Input  ${year}
    Input  ${publisher}