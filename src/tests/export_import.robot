*** Settings ***
Library  ../AppLibrary.py
Resource  resources.robot

*** Test Cases ***
Book Can Be Exported And Imported
    Add Book  Harry Potter  JK Rowling  2000  Otava
    input  export
    input  robot_exported
    input  delete all
    input  import
    input  robot_exported.bib
    input  list books
    input  exit
    Run Application
    output should contain  Harry Potter