# Electron with Eel Quick Guide

This is a simple repo you can clone to get started on working with python and electron using the library eel.

## Getting started

### Install pyinstaller (the bundler)

<code>pip install pyinstaller</code>

### Download electron version of choosing <a href="https://github.com/electron/electron/releases/">@</a>

Extract contents to directory "./electron"

## Running Application

<code>python <filename.py></code>

<blockquote>filename being app.py in this case</blockquote>

## Packaging application

<code>pyinstaller <strong><(filename.py)></strong> --hidden-import bottle_websocket --add-data eel;eel --add-data <strong> <(webfolder)>;<(webfolder)> </strong> --add-data electron;electron --add-data main.js;electron/resources/app --add-data package.json;electron/resources/app --onefile --noconsole`
</code>

### In this project setup

`pyinstaller app.py --hidden-import bottle_websocket --add-data eel;eel --add-data static;static --add-data electron;electron --add-data main.js;electron/resources/app --add-data package.json;electron/resources/app --onefile --noconsole`
<br/>
Credits goes to <a href="https://github.com/amiotk">@amiotk</a> for posting a setup that both works for development and production.

Issue page: <a href="https://github.com/ChrisKnott/Eel/issues/57">here</a>
