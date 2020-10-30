import os


version = '0.1'
apt_path = '/var/lib/apt/lists'
help_message = ''


def get_apt_packages(python=True):
    packages = []
    python_packages = []
    package_files = [file for file in os.listdir(apt_path) if file.endswith('Packages')]
    if not package_files:
        exit('Cannot read APT packages.')
    for file in package_files:
        # with open(os.path.join(apt_path, file), 'r') as f:
        with open(f'{apt_path}/{file}', 'r') as f:
            for line in f:
                if line.startswith('Package:'):
                    if python and line.startswith('Package: python3-'):
                        python_packages.append(line[9:-1])  # remove 'Package:' and '\n'
                    else:
                        packages.append(line[9:-1])
    return list(set(packages)), list(set(python_packages))


def divide_packages(packages):
    apt_list, apt_py_list = get_apt_packages()
    apt = []
    pip = []
    # DO NOT use apt = pip = [] since they will be tied up
    for package in packages:
        if f'python3-{package}' in apt_py_list:
            apt.append(f'python3-{package}')
        elif package in apt_list:
            apt.append(package)
        else:
            pip.append(package)
    return apt, pip
