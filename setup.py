from setuptools import setup

from cheesebread import __version__ as VERSION

with open('README.rst') as fobj:
    long_description = fobj.read()

setup(
    author='Gabriel Stefanini Vicente',
    author_email='g4brielvs@g4brievs.me',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3.7',
        'Topic :: Utilities',
    ],
    description='cheesebread: a toolbox for data science',
    keywords='toolbox, data science',
    license='Proprietary',
    long_description=long_description,
    name='cheesebread',
    packages=[
        'cheesebread',
    ],
    url='https://github.com/g4brielvs/cheesebread',
    python_requires='>=3.7',
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
    scripts=['cheesebread/cheesebread'],
    version=VERSION,
)
