import subprocess
from .common import *


def show_default(unknown=False):
    message = f'APIPT v{version}\nRun \'apipt --help\' for help.'
    if unknown:
        message = 'Unknown command.\n' + message
    return print(message)


def show_help():
    return print(help_message)


def show_version():
    return print(f'APIPT v{version}')


def update():
    """
    Equivalent to apt update
    """
    subprocess.run('apt update'.split())
    # return True


def upgrade():
    """
    Equivalent to apt upgrade
    """
    print('Press any key if no [y/N] prompt.\n')
    apt_run = subprocess.Popen('apt upgrade'.split(), stdin=subprocess.PIPE)
    apt_run.communicate(input().encode('utf-8'))
    # return True


def install(packages):
    if not packages:
        exit('No package specified.')
    apt_command = ['apt', 'install']
    pip_command = ['pip', 'install']
    if '-y' in packages:
        apt_command.append('-y')
        pip_command.append('-y')
        packages.remove('-y')
    if '-r' in packages:
        try:
            file = packages[packages.index('-r')+1]
        except IndexError:
            file = None
            exit('No file specified.')
        with open(file, 'r') as f:
            lines = [line.strip() for line in f]
            p = [line for line in lines if line and not line.startswith('#')]
        packages.remove(file)
        packages.remove('-r')
        packages.extend(p)
    while '' in packages:
        packages.remove('')

    apt, pip = divide_packages(packages)
    if apt:
        apt_command.extend(apt)
        print(f'Running: ' + ' '.join(apt_command) + '\n' + 'Press any key if no [y/N] prompt.\n')
        apt_run = subprocess.Popen(apt_command, stdin=subprocess.PIPE)
        apt_run.communicate(input().encode('utf-8'))
    if pip:
        pip_command.extend(pip)
        print(f'Running: ' + ' '.join(pip_command) + '\n' + 'Press any key if no [y/N] prompt.\n')
        pip_run = subprocess.Popen(pip_command, stdin=subprocess.PIPE)
        pip_run.communicate(input().encode('utf-8'))

    # return True
