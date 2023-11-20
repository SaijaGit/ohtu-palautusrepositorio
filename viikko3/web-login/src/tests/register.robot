*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  nalle
    Set Password  nalle123
    Set Password Confirmation  nalle123
    Submit Registration
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  k
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Registration
    Register Should Fail With Message  Username is too short (min 3 characters)

Register With Valid Username And Invalid Password
    Set Username  kalle
    Set Password  kallekalle
    Set Password Confirmation  kallekalle
    Submit Registration
    Register Should Fail With Message  Password can not contain only letters

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  palle123
    Submit Registration
    Register Should Fail With Message  Password and password confirmation don't match

Login After Successful Registration
    Set Username  palle
    Set Password  palle123
    Set Password Confirmation  palle123
    Submit Registration
    Register Should Succeed
    Go To Main Page
    Log Out
    Set Username  palle
    Set Password  palle123
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  valle
    Set Password  valle123
    Set Password Confirmation  valle321
    Submit Registration
    Register Should Fail With Message  Password and password confirmation don't match
    Go To Login Page
    Set Username  valle
    Set Password  valle123
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Registration
    Click Button  Register

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Log Out
    Click Button  Logout