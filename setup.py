from setuptools import setup

from cheesebread import __version__ as VERSION

with open('README.rst') as fobj:
    long_description = fobj.read()

setup(
    author='g4brielvs',
    author_email='g4brielvs@g4brievs.me',
    name='cheesebread',
    version=VERSION,
    description='cheesebread: a toolbox for data science',
    long_description=long_description,
    keywords='toolbox, data science',
    license='MIT',
    url='https://github.com/g4brielvs/cheesebread',
    python_requires='>=3.7',
    packages=[
        'cheesebread',
        'cheesebread.datasets',
        'cheesebread.helpers',
        'cheesebread.wrappers',
    ],
    install_requires=[
        'aiofiles',
        'aiohttp',
        'boto3',
        'pandas>=0.24',
        'requests',
        'riprova',
        'tqdm',
    ],
    zip_safe=False,
)
