*** Settings ***
Resource  resource.robot
Test Setup  Input Create User

*** Test Cases ***
Register With Valid Username And Password
  Input Credentials  test  tester123
  Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  test  tester123
    Input Create User
    Input Credentials  test  tester124
    Output Should Contain  User with username test already exists

Register With Too Short Username And Valid Password
  Input Credentials  te  tester123
  Output Should Contain  Username must be of length 3 or longer

Register With Valid Username And Too Short Password
  Input Credentials  test  tester1
  Output Should Contain  Password must be of length 8 or longer

Register With Valid Username And Long Enough Password Containing Only Letters
  Input Credentials  test  testeriiii
  Output Should Contain  Password can contain letters a-z