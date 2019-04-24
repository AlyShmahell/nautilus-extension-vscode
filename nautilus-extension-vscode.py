from gi import require_version
require_version('Gtk', '3.0')
require_version('Nautilus', '3.0')
from gi.repository import Nautilus, GObject
from subprocess import call
import os

class nautilusExtensionVSCode(GObject.GObject, Nautilus.MenuProvider):

    def launch_vscode(self, _, files):
        filepath = ''
        for file in files:
            filepath += '"' + file.get_location().get_path() + '" '
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

