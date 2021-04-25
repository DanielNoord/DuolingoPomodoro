from setuptools import setup

APP = ["rumps_app.py"]
DATA_FILES = []
OPTIONS = {
    "argv_emulation": True,
    "iconfile": "static/icons/duolingo_icon.png",
    "plist": {
        "CFBundleGetInfoString": "A little menu-bar app for macOS that sends a notification which prompts the user to answer a question based on their vocabulary in duolingo",  # pylint: disable=line-too-long
        "CFBundleShortVersionString": "0.1.0",
        "LSUIElement": True,
    },
    "packages": ["rumps", "duolingo"],
    "resources": ["static"],
}
setup(
    app=APP,
    name="Duolingo Pomodoro",
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
    install_requires=["rumps"],
)
