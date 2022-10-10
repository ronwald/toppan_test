## Requirements

1. [Visual Studio Code](https://code.visualstudio.com/)
2. [Python 3.9](https://www.python.org/downloads/windows/) - must be 3.9 32-bit, as later versions are incompatible with some libraries we use
    If your PC has not installed Python yet, please execute [install.bat] file for auto downloading and installing Python 3.9.0
    It also helps to install all required packets automatically.

3. ChromeDriver (we use a custom chromedriver) - should be in the root of the test automation project

4. Once Python is installed, cd to the root folder (anne-robot) then run the following in PowerShell to install all required python package:
    pip install -r requirements
    ## Important ##
    The selenium package version must be 3.141.0
    To install this specific version, let run the following command:  
    pip install selenium==3.141.0

5. In Visual Studio Code, install the following extensions

    1. Python
    2. Robot Framework Intellisense
    3. Material Icon Theme (QOL)
    4. Theme of your choice (QOL)

## Run test via vscode tasks
Visual Studio Code tasks.json (allows you to execute your tests inside the IDE)
```
{
    // See https://go.microsoft.com/fwlink/?LinkId=733558
    // for the documentation about the tasks.json format
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Run Selected Test Case",
            "type": "shell",
            "command": "robot",
            "args": [
                "-P",
                "${workspaceFolder}",
                "-d",
                "${workspaceFolder}\\logs",
                "-t",
                "${selectedText}",
                "-b",
                "debug.txt",
                "${file}"
            ],
            "presentation": {
                "reveal": "always",
                "panel": "shared"
            },
            "problemMatcher": [],
            "group": {
                "kind": "build",
                "isDefault": true
            }
        },
        {
            "label": "Run All Test Cases",
            "type": "shell",
            "command": "robot",
            "args": [
                "-P",
                "${workspaceFolder}",
                "-d",
                "${workspaceFolder}\\logs",
                "-b",
                "debug.txt",
                "-e",
                "Blocked",
                "${file}"
            ],
            "presentation": {
                "reveal": "always",
                "panel": "shared"
            },
            "problemMatcher": []
        },
        {
            "label": "Run Some Test Cases",
            "type": "shell",
            "command": "robot",
            "args": [
                "-P",
                "${workspaceFolder}",
                "-d",
                "${workspaceFolder}\\logs",
                "-b",
                "debug.txt",
                "-i",
                "Test",
                "${file}"
            ],
            "presentation": {
                "reveal": "always",
                "panel": "shared"
            },
            "problemMatcher": []
        },
        {
            "label": "Rerun All Failed Test Cases",
            "type": "shell",
            "command": "robot",
            "args": [
                "-P",
                "${workspaceFolder}",
                "--rerunfailed",
                "${workspaceFolder}\\logs\\output.xml",
                "--output",
                "${workspaceFolder}\\logs\\output1.xml",
                "-d",
                "${workspaceFolder}\\rerun-logs",
                "-b",
                "debug.txt",
                "${file}"
            ],
            "presentation": {
                "reveal": "always",
                "panel": "shared"
            },
            "problemMatcher": []
        },
        {
            "label": "Run All Test Suites",
            "type": "shell",
            "command": "robot",
            "args": [
                "-P",
                "${workspaceFolder}",
                "-d",
                "${workspaceFolder}\\logs",
                "-b",
                "debug.txt",
                "${workspaceFolder}\\tests"
            ],
            "presentation": {
                "reveal": "always",
                "panel": "shared"
            },
            "problemMatcher": []
        }
    ]
}
```
## Mapping Notices
A. How mapping modules work:
    1. Run the automated suites.
    2. Select Option For Mapping: 
        2.1:    No Mapping
        2.2:    Mapping to an existing test-plan
    3. Mapping completed, result will be mapped to test-plan.
    Check the detailed log under Publish Results And Mapping keyword on the log file

B. Detect editionID and editionName when mapping to an existing test-plan:
    1. If editionID = 0, that means we're testing with based device  
    => Mapping all runs have not the edition config, that mean don't map edition runs
    2. If editionID != 0, that means we're testing with a specific edition device  
    => Check the editionName:
        2.1: If editionName exists   => only mapping the run has the edition config same as editionName.
        2.2: If editionName is blank, means could not get the editionName. 
        => Must get edition name from dialog => only mapping the run has the edition config same as getting editionName from runner.

C. How to deal with failed cases when mapping:
    1. If the pass rate larger than 70%, try to mapping
    2. Use task from vscode to rerun all failed test cases (Rerun All Failed Test Cases) 
    => try to mapping if there some previous failed cases have been passed.
    3. Retest manually all failed case to check whether they are bug.
