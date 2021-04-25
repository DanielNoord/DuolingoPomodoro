[![Python CI](https://github.com/DanielNoord/DuolingoPomodoro/actions/workflows/CI.yaml/badge.svg?branch=main&event=push)](https://github.com/DanielNoord/DuolingoPomodoro/actions/workflows/CI.yaml)

# Duolingo Pomodoro
A little menu-bar app for macOS that sends a notification which prompts the user to answer a question based on their vocabulary in duolingo.

## Downloading the app
#### By downloading a .app executable
The latest release can be found in the release section found to the right of this Readme. Note that the app is unsigned and macOS will throw an error when opening. This can be avoided by opening the app **by clicking while holding the control key**. This while allow you to ignore the warning and it will not return.

#### From source
For those who want to build from source, the latest version can be found on the `main` branch.
Build in the `dist` directory using the following command:
```
python3 py2app_setup.py py2app
```

## Using the app
Since the Duolingo API takes some time for requests to be fulfilled the app does not automatically log you in (although this can be toggled).

Logging in takes some time, but will eventually always tell you if it failed or succeeded.

Your vocabulary list is loaded during login, so you might want to restart the app/reload the vocabulary after you have finished additional lessons on Duolingo.


Built using [duolingo-api](https://github.com/KartikTalwar/Duolingo) and [rumps](https://github.com/jaredks/rumps)
