*** Settings ***
Documentation       Shared configuration file for all tests
Library             SeleniumLibrary  timeout=60s  run_on_failure=NONE
Library             Collections
Library             Dialogs
Library             String
Library             Process
Library             common.py

*** Variables ***
${URL}  http://localhost:8080/
${BROWSER}  chrome
${TABNAME}  Technical Challenge for CDS
${CSVFILELOC}  C:\\Users\\ronwald.Sandoval\\Downloads\\toppantest.csv

*** Keywords ***
Insert Single Record
    Sleep  5
    Insert Single Record Test
    Sleep  3

Insert Multiple Record
    Launch App Toppan
    Sleep  5
    Insert Multiple Record Test
    Sleep  3

Launch App Homepage
    Open Browser  ${URL}   ${BROWSER}
    Maximize Browser Window

Upload CSV File
    Sleep  5
    Switch Window    ${TABNAME}
    Click Upload CSV File Button
    Enter CSV File Location  ${CSVFILELOC}

Launch App Jar File
    Launch App Toppan
    Sleep  5

Verify Correct Tax Relief Computation
    Check Tax Compute   10000  2000   37  Male

Verify Appearance Of Button
    Verify Button Is Red
    Verify Text Is Dispense Now

Verify Result After Button Click
    Verify Cash Dispensed Text Displayed

Close Terminal
    Close App Toppan

Return And Verify Record Tax Relief
    Retrieve TaxRelief NatID Name
    Verify 5th Character Dollar Sign
    Verify TaxRelief Has Two Decimal Places