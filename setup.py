import os
import subprocess
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as f:
    lines = [line.strip() for line in f]
    requirements = [line for line in lines if line and not line.startswith('#')]


def detect_os():
    if os.name != 'posix':
        raise RuntimeError('Sorry, this package can only work on Linux.')
    try:
        result = subprocess.run('apt --version'.split(), capture_output=True)
        if result.returncode != 0:
            raise RuntimeError('Sorry, your APT might be broken.')
    except FileNotFoundError:
        raise RuntimeError('Sorry, this package can only run on distros with APT.')
    return True


setup(
    name='apipt',
    version='0.1',
    description='',
    url='https://github.com/KumaTea/apipt',
    author='KumaTea',
    author_email='contact@maku.ml',
    license='MIT',
    keywords=('apipt',),
    packages=find_packages(),
    platforms='posix',
    python_requires='>=3.6',
    install_requires=requirements,
    cmdclass={'install': detect_os},
    entry_points={
        'console_scripts': [
            'apipt=apipt.app:main'
        ]
    }
)
