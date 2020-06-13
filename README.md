# Project-Hermes

# Mobile
I'll write brief explanations about the code

All markup and style (equivalent to HTML and CSS, in web dev) are in the file `design.kv`

There you'll find 3 "section": one main screen (with the graphs), one second screen (with the options to call police), and one popup/modal (with more info)

On the code (`app.py` file) each one of those section hare its own class

The code section I did something was MainWindow, that have functions to print something on screen (for debug only) or to show the popup/modal

The transitions from one screen to the next are described in the `design.kv` itself, using the hooks on_press, on_release, etc