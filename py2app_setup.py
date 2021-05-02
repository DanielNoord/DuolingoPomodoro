from setuptools import setup

APP = ["rumps_app.py"]
DATA_FILES = []
LICENSE = """MIT License

Copyright (c) 2021 Daniël van Noord

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
OPTIONS = {
    "argv_emulation": True,
    "iconfile": "static/icons/duolingo_icon.icns",
    "plist": {
        "CFBundleGetInfoString": "A little menu-bar app for macOS that sends a notification which prompts the user to answer a question based on their vocabulary in duolingo",  # pylint: disable=line-too-long
        "CFBundleShortVersionString": "0.2.0",
        "LSUIElement": True,
        "NSHumanReadableCopyright": "Copyright © 2021 Daniël van Noord. MIT License.",
    },
    "packages": ["rumps", "duolingo"],
    "resources": ["static"],
}
setup(
    app=APP,
    author="Daniël van Noord",
    data_files=DATA_FILES,
    install_requires=["rumps"],
    license=LICENSE,
    name="Duolingo Pomodoro",
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)
