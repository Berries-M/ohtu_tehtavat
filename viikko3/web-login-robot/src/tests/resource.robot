*** Settings ***
Library  SeleniumLibrary
Library  ../AppLibrary.py

*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  headlesschrome
${DELAY}  0 seconds
${HOME URL}  http://${SERVER}
${LOGIN URL}  http://${SERVER}/login
${REGISTER URL}  http://${SERVER}/register

*** Keywords ***
Open And Configure Browser
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Login Page Should Be Open
    Title Should Be  Login

Main Page Should Be Open
    Title Should Be  Ohtu Application main page

Go To Login Page
    Go To  ${LOGIN URL}

# Nämä 5 siirretty loginista
Login Should Succeed
    Main Page Should Be Open

Submit Credentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

# Nämä 6 itse
Go To Main Page
    Go To  ${HOME URL}

Register Page Should Be Open
    Title Should Be  Register

Click Login Link
    Click Button  Login

Click Register Link
    Click Button  Register

Go To Register Page
    Go to  ${REGISTER URL}

Input Register Command
    Input Text  register

Confirm Password
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}


