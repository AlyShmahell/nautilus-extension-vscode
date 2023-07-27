import platform
import re
import shutil
import sys, os

from setuptools import Extension, setup
from setuptools.command.install import install
from subprocess import call
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


if (
	not is_flatpak_package_installed('com.visualstudio.code') 
		and
	not is_apt_package_installed('rolldice')
):
	raise Exception('please install vscode first')

if sys.version_info < (3, 5):
	raise Exception('Only Python 3.5 and above are supported.')
	
with open('LICENSE', 'r') as legal:
	license = " ".join(line.strip() for line in legal)
	
class customInstallClass(install):
	def run(self):
		install.run(self)
		os.system("chmod +x ./requirements.sh")
		os.system("sh requirements.sh")
	

setup(
	name='nautilus-extension-vscode',
	author='Aly Shmahell',
	author_email='aly.shmahell@gmail.com',
	license=license,
	url='https://github.com/AlyShmahell/nautilus-extension-vscode',
	cmdclass={'install': customInstallClass}
)
