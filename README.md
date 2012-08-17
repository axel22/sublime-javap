sublime-javap
=============

Javap support for the Sublime Text 2 editor.
Presents JVM classfiles in a readable format - ideal for viewing your bytecode.


Installation
============

Go to your Sublime Packages folder and clone this repository there:

    cd ~/Library/Application Support/Sublime Text 2/
    git clone git://github.com/axel22/sublime-javap.git sublime-javap

Usage
=====

Open a class file in Sublime (tip: by default class files are ignored by Sublime - open `Prefrences -> Settings Default`, and search for `"file_exclude_patterns"` to remove `.class` files from the exclusion list). Then run the `Javap decompilation` command from your command pane.
The `javap` output will be shown in a new window.

To set up a keybinding, add the following line to your keybindings:

    { "keys": ["ctrl+c", "ctrl+j", "ctrl+p"], "command": "javap" },


License
=======

No license, no liability, use as you see fit.