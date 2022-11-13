*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password      
    Set Username  tester
    Set Password  tester123
    Set Password Confirmation  tester123
    Submit Credentials
    Title Should Be  Welcome to Ohtu Application!

Register With Too Short Username And Valid Password
    Set Username  te
    Set Password  tester123
    Set Password Confirmation  tester123
    Submit Credentials
    Register Should Fail With Message  Username must be of length 3 or longer

Register With Valid Username And Too Short Password
    Set Username  tester
    Set Password  test1
    Set Password Confirmation  test1
    Submit Credentials
    Register Should Fail With Message  Password must be of length 8 or longer

Register With Nonmatching Password And Password Confirmation
    Set Username  tester
    Set Password  tester123
    Set Password Confirmation  tester124
    Submit Credentials
    Register Should Fail With Message  Passwords does not match

*** Keywords ***

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Submit Credentials
    Click Button  Register

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}