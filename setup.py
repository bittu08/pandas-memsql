from distutils.core import setup
setup(
    name = 'pandas-memsql',
    version = '0.0.1',
    author = 'Bittu08',
    author_email = 'bittukumardh@gmail.com',
    packages = [
        'ply',
        'ply.vendor',
    ],
    description = 'SQL query over pandas dataframe',
    long_description = open('README.rst').read(),
    license = 'Apache License 2.0',
    url = 'https://github.com/bittu08/pandas-memsql',
    classifiers = [],
)