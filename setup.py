from setuptools import setup

REQUIREMENTS = [
    'requests',
    'click',
    'pyfiglet'
]

VERSION = 0.5
REPO_URL = 'https://github.com/BoxingOctopus/toxin'

setup(
    name='toxin',
    packages=['toxin'],
    scripts=['toxin/toxin'],
    version=VERSION,
    description='An LFI (Local File Inclusion) Exploitation Tool',
    author='Ryan Draga',
    author_email='ryan.draga@boxingoctop.us',
    url=REPO_URL,
    download_url=F'{REPO_URL}/archive/{VERSION}.tar.gz',
    keywords=['LFI', 'Exploit'],
    python_requires='>=3.0',
    install_requires=REQUIREMENTS,
    classifiers=[]
)
