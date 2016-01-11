from setuptools import setup

def version():
    import subprocess
    vers = str(subprocess.check_output('git describe --always', shell=True))
    return vers

NAME = 'Slack message send helper'
VERSION = version()

setup(
    name=NAME,
    version=VERSION,
    scripts=[
        'ssend',
        'ssend-notify'
    ],
)
