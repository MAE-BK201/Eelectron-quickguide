import eel
import eel.browsers
import os
import sys

eel.init("static")


def resource_path(rel_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, rel_path)


@eel.expose
def increment_from_python(value):
    return int(value) + 1


# change to respective os extension
eel.browsers.set_path("electron", resource_path("electron\electron.exe"))

eel.start("index.html", mode="electron")


'''
    To run program:
        python <<filename.py>>
    To create a distributable:
        1) pip install pyinstaller
        2) pyinstaller <<filename.py>> --hidden-import bottle_websocket --add-data eel;eel --add-data <<webfolder name>>;<<webfolder name>> --add-data electron;electron --add-data main.js;electron/resources/app --add-data package.json;electron/resources/app --onefile --noconsole

        In this case: pyinstaller app.py --hidden-import bottle_websocket --add-data eel;eel --add-data static;static --add-data electron;electron --add-data main.js;electron/resources/app --add-data package.json;electron/resources/app --onefile --noconsole
'''
