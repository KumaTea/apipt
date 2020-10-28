import os
import subprocess

apt_path = '/var/lib/apt/lists'


def update(output=True):
    """
    Equivalent to apt update
    """
    return subprocess.run('apt update'.split(), capture_output=not output)


def upgrade(output=True):
    """
    Equivalent to apt upgrade
    """
    return subprocess.run('apt upgrade'.split(), capture_output=not output)


def get_apt_packages(python_only=False):
    packages = []
    package_files = [file for file in os.listdir(apt_path) if file.endswith('Packages')]
    if python_only:  # judge only once
        for file in package_files:
            with open(os.path.join(apt_path, file), 'r') as f:
                for line in f:
                    if line.startswith('Package: python3-'):
                        packages.append(line[9:-1])  # remove 'Package:' and '\n'
    else:
        for file in package_files:
            with open(os.path.join(apt_path, file), 'r') as f:
                for line in f:
                    if line.startswith('Package:'):
                        packages.append(line[9:-1])  # remove 'Package:' and '\n'
    return list(set(packages))


def execute():
    pass
