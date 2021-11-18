*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Login Command

*** Test Cases ***
Login With Correct Credentials
    Input Credentials  kalle  kalle123
    Output Should Contain  Logged in

# Tämä lisätty, ei kirjaudu sisään
Login With Incorrect Password
    Input Credentials  kalle  vaara
    Input Login Command

# Ja tämä myös, ei kirjaudu sisään
Login With Nonexistent Username
    Input Credentials  outo  lintu
    Input Login Command

*** Keywords ***
Create User And Input Login Command
    Create User  kalle  kalle123
    Input Login Command
