*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page And Begin

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kissa
    Set Password  hiirulainen9
    Confirm Password  hiirulainen9  
    Click Button  Register
    Welcome Page Should Be Open

Register With Too Short Username And Valid Password
    Set Username  ki
    Set Password  hiirulainen9
    Confirm Password  hiirulainen9
    Click Button  Register
    Register Should Fail With Message  Not a valid username.

Register With Valid Username And Too Short Password
    Set Username  kissa
    Set Password  hii99
    Confirm Password  hii99
    Click Button  Register
    Register Should Fail With Message  Not a valid password.

Register With Nonmatching Password And Password Confirmation
    Set Username  koira
    Set Password  hiirulainen9
    Confirm Password  j
    Click Button  Register
    Register Should Fail With Message  Password and confirmation don't match.

*** Keywords ***
Go To Register Page And Begin
    Go To Register Page
    Register Page Should Be Open

Welcome Page Should Be Open
    Title Should Be  Welcome to Ohtu Application!

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}


    
