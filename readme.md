## Requirements

1. [Visual Studio Code](https://code.visualstudio.com/)
2. [Python 3.9](https://www.python.org/downloads/windows/).
3. Open cmd prompt, and do pip install the following
    robotframework==3.2.2
    robotframework-seleniumlibrary==4.5.0
    robotframework-pythonlibcore==2.1.0
    requests==2.25.0
    pyotp==2.4.1
    pywinauto==0.6.8
    pywin32==300
    pyautogui==0.9.52
    pandas==1.3.0
    openpyxl==3.0.7
    numpy==1.21.0
    aiohttp==3.7.4.post0
    selenium==3.141.0
    jsonpath==0.82
    jsonpath-ng==1.5.3
    pygame==2.1.2
    py7zr==0.20.0
    xlsx2html==0.4.0
    msgpack-rpc-python==0.4.1

4. In Visual Studio Code, install the following extensions

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

The tests can also be run via terminal
