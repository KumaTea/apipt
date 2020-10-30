import subprocess
if __package__:
    from .common import *
else:
    from common import *


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


def execute():
    pass
