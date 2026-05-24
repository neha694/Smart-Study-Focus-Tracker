productive_apps = [
    "Visual Studio Code",
    "PyCharm",
    "Jupyter",
    "Word",
    "PowerPoint",
    "Google Chrome"
]

distracting_apps = [
    "YouTube",
    "Instagram",
    "Netflix",
    "Prime",
    "Hotstar",
    "Spotify"
]

def classify_app(app_name):

    app_name = str(app_name)

    for app in productive_apps:
        if app.lower() in app_name.lower():
            return "Productive"

    for app in distracting_apps:
        if app.lower() in app_name.lower():
            return "Distracting"

    return "Neutral"