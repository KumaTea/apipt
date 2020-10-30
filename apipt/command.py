import subprocess
if __package__:
    from .common import *
else:
    from common import *


def show_help():
    return print(help_message)


def show_version():
    return print(f'APIPT v.{version}')


def update():
    """
    Equivalent to apt update
    """
    return subprocess.run('apt update'.split())


def upgrade():
    """
    Equivalent to apt upgrade
    """
    print('Press any key if no [y/N] prompt.\n')
    apt_run = subprocess.Popen('apt upgrade'.split(), stdin=subprocess.PIPE)
    return apt_run.communicate(input().encode('utf-8'))


def install(packages):
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
            p = f.read().splitlines()
        packages.remove(file)
        packages.remove('-r')
        packages.extend(p)

    apt, pip = divide_packages(packages)

    apt_command.extend(apt)
    print(f'Running: ' + ' '.join(apt_command) + '\n' + 'Press any key if no [y/N] prompt.\n')
    apt_run = subprocess.Popen(apt_command, stdin=subprocess.PIPE)
    apt_run.communicate(input().encode('utf-8'))

    pip_command.extend(pip)
    print(f'Running: ' + ' '.join(pip_command) + '\n' + 'Press any key if no [y/N] prompt.\n')
    pip_run = subprocess.Popen(pip_command, stdin=subprocess.PIPE)
    pip_run.communicate(input().encode('utf-8'))

    return True
