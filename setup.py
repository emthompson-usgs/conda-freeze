from distutils.core import setup

setup(
    name='condafreeze',
    version=0.1,
    description='Helper for freezing conda dependencies',
    author='Eric Thompson',
    author_email='emthompson@usgs.gov',
    scripts=[
        'bin/freeze'
    ]
)
