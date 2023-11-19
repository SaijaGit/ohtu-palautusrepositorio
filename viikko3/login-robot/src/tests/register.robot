*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Login Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  palle  palle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  k  kalle123
    Output Should Contain  Username is too short (min 3 characters)

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  k123456789  kalle123
    Output Should Contain  Username contains forbidden characters (only a-z allowed)

Register With Valid Username And Too Short Password
    Input Credentials  palle  palle12
    Output Should Contain  Password is too short (min 8 characters)

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  palle  pallepalle
    Output Should Contain  Password can not contain only letters

*** Keywords ***
Create User And Input Login Command
    Create User  kalle  kalle123
    Input New Command