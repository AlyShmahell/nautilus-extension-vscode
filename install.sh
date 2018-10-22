#!/bin/bash
sudo apt install python-gi python-gi-cairo python3-gi python3-gi-cairo gir1.2-gtk-3.0
mkdir -p ~/.local/share/nautilus-python/extensions && cp -f nautilus-extension-vscode.py ~/.local/share/nautilus-python/extensions/nautilus-extension-vscode.py && nautilus -q && nautilus
