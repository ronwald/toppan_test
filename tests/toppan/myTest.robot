*** Settings ***
Resource        ../../resources/config/common.robot
Test Teardown    Close Browser


***Test Cases***
#User Story 1
Insert Single Record Working Class Hero
    Launch App Jar File
    Insert Single Record
    Launch App Homepage


#User Story 2
Insert Multiple Record Working Class Hero
    Launch App Jar File
    Insert Multiple Record
    Launch App Homepage

#User Story 3
Upload CSV File To Populate DB From UI
    Launch App Jar File
    Launch App Homepage
    Upload CSV File

#User Story 4
Query Amount Of Tax Relief
    Launch App Jar File
    Insert Single Record
    Launch App Homepage
    Verify Correct Tax Relief Computation
    Return And Verify Record Tax Relief

#User Story 5
Dispense Tax Relief
    Launch App Jar File
    Launch App Homepage
    Verify Appearance Of Button
    Verify Result After Button Click
    
    
