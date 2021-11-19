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

Login After Successful Registration
    Set Username  koira
    Set Password  kiirulainen9
    Confirm Password  kiirulainen9  
    Click Button  Register
    Welcome Page Should Be Open
    Go To Login Page
    Login Page Should Be Open
    Set Username  koira
    Set Password  kiirulainen9
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  ko
    Set Password  koorulainen9
    Confirm Password  koorulainen9  
    Click Button  Register
    Go To Login Page
    Login Page Should Be Open
    Set Username  ko
    Set Password  koorulainen9
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

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


