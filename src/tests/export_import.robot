*** Settings ***
Library  ../AppLibrary.py

*** Test Cases ***
Book Can Be Imported
    input  import
    input  src/tests/resources/test
    input  list books
    input  exit
    Run Application
    output should contain  How to Import