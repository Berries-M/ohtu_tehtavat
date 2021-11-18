*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Login Command

Register With Already Taken Username And Valid Password
    Run Keyword and Expect Error  User with username kissa already exists  Create User  kissa  hiiriuusi99
    
Register With Too Short Username And Valid Password
    Run Keyword and Expect Error  UserInputError: Not a valid username.  Create User  ki  hiiriuusi99

Register With Valid Username And Too Short Password
    Run Keyword and Expect Error  UserInputError: Not a valid password.  Create User  kiiluinen  hii99

Register With Valid Username And Long Enough Password Containing Only Letters
    Run Keyword and Expect Error  UserInputError: Not a valid password.  Create User  kiiluinen  hiiruinen

*** Keywords ***
Input New Command And Create User
    Input  register 
    Create User  kissa  hiirulainen9
    
