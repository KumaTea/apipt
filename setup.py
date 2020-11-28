import os
import subprocess
from setuptools import setup, find_packages
from setuptools.command.install import install


with open("README.md", "r") as fh:
    long_description = fh.read()
with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as f:
    lines = [line.strip() for line in f]
    requirements = [line for line in lines if line and not line.startswith('#')]


def detect():
    if os.name != 'posix':
        raise RuntimeError('Sorry, this package can only work on Linux.')
    try:
        result = subprocess.run('apt --version'.split(), capture_output=True)
        if result.returncode != 0:
            raise RuntimeError('Sorry, your APT might be broken.')
    except FileNotFoundError:
        raise RuntimeError('Sorry, this package can only run on distros with APT.')
    return True


class DetectOS(install):
    def run(self):
        detect()
        install.run(self)


setup(
    name='apipt',
    version='0.1.1',
    description='Install Python packages by apt',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/KumaTea/apipt',
    author='KumaTea',
    author_email='contact@maku.ml',
    license='MIT',
    keywords=['apipt'],
    packages=find_packages(),
    platforms='posix',
    python_requires='>=3.6',
    install_requires=requirements,
    cmdclass={'install': DetectOS},
    entry_points={
        'console_scripts': [
            'apipt=apipt.app:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Topic :: Utilities"
    ],
)
