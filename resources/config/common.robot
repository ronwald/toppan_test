*** Settings ***
Documentation       Shared configuration file for all tests
Library             SeleniumLibrary  timeout=60s  run_on_failure=NONE
Library             Collections
Library             Dialogs
Library             String
Library             Process
Library             common.py


*** Keywords ***
Insert Single Record
    Launch App Toppan