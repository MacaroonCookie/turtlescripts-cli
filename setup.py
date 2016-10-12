from setuptools import setup

__version__ = '0.0.1-alpha.1'
__license__ = ''

setup(
    name = 'TurtleScripts Remote API Utility',
    version = __version__,
    description = '',
    long_description = '',
    author = 'Seth Cook',
    author_email = 'cooker52@gmail.com',
    url = '',
    packages = [ 'turtlescripts' ],
    license = __license__,
    classifiers = [
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.5',
        'Operating System :: Unix',
        'Development Status :: 3 - Alpha'
    ],
    install_requires = [
        'requests>2.11.0'
    ],
    entry_points = {
        'console_scripts': [
            'turtlescripts=TurtleScripts.__main__:main'
        ]
    }
)
