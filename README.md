# Multiple timer app
- Run from the command line with `python path/to/Time_App.py 00:10:00 01:00:00`
- This creates one 10-minute timer and 1-hour timer, they do not run parallel, the first timer must finish before the second one starts.
- You can add as many add 15 timers.
- The app automatically closes when all timers are finished.
- Configurations file, add custom configurations and run them by just calling `python path/to/Time_App.py Configurations config_name`

## Keyboard shortcuts 
- Only for mac
- Create a folder with any name, inside the folder you will make a file with the .sh extension.
- Inside this file, write this code:
```
#!/bin/bash
cd path/to/Time_App folder
/usr/local/bin/python3 Time_App.py Configurations config_name
```
- Save the file and close it.
- Open the terminal and run `chmod +x path/to/file.sh`
- Open the automator app, create a new application, and add the "Run shell script" action.
- After creating the action, go to system preferences -> keyboard -> shortcuts -> services -> general and add a shortcut for the app you just created.
##### As of now, if you exit the timers before they are finished, the app with raise an error, you can ignore it.

## Coming soon
- The ability to change the sound
- Set alarms
- Set different sounds for each timer
- Set timers to run parallel
- Handle errors when incorrect input is provided