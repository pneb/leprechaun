from setuptools import setup

with open('README.md') as fp:
    long_description = fp.read()

setup(
    name='leprechaun',
    version='0.0.1',
    packages=['leprechaun'],
    description='A lightweight and efficient asyncio-like library for Python 3.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Bernward Sanchez',
    url='https://github.com/pneb/leprechaun',
    author_email='contact@bern.codes',
    license='MIT',
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
    ],
)
