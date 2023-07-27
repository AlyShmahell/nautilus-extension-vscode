from gi import require_version
require_version('Gtk', '3.0')
require_version('Nautilus', '3.0')
from gi.repository import Nautilus, GObject
from subprocess import call
import os
import subprocess 

def is_flatpak_package_installed(package_name):
    try:
        output = subprocess.check_output(["flatpak", "info", package_name], stderr=subprocess.STDOUT, text=True)
        return package_name in output
    except subprocess.CalledProcessError:
        return False
        
def is_apt_package_installed(package_name):
    try:
        output = subprocess.check_output(["apt", "list", package_name, '--installed'], stderr=subprocess.STDOUT, text=True)
        return package_name in output
    except subprocess.CalledProcessError:
        return False


class nautilusExtensionVSCode(GObject.GObject, Nautilus.MenuProvider):

    def launch_vscode(self, _, files):
        filepath = ''
        for file in files:
            filepath += '"' + file.get_location().get_path() + '" '
        if is_flatpak_package_installed('com.visualstudio.code'):
            call('flatpak run com.visualstudio.code' + ' --new-window ' + filepath + '&', shell=True)
        if is_apt_package_installed('code'):
            call('code' + ' --new-window ' + filepath + '&', shell=True)

    def get_file_items(self, _, files):
        item = Nautilus.MenuItem(
            name='OpenFileWithVSCode',
            label='Open with VSCode',
            tip='Opens the selected files with VSCode'
        )
        item.connect('activate', self.launch_vscode, files)
        return [item]

    def get_background_items(self, _, files):
        item = Nautilus.MenuItem(
            name='LaunchVSCodeInDirectory',
            label='Launch VSCode Here',
            tip='Launches VSCode in the current directory'
        )
        item.connect('activate', self.launch_vscode, [files])
        return [item]

