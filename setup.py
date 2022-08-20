from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = ''
LONG_DESCRIPTION = ''


def get_requires():
    reqs = []
    for line in open('requirements.txt', 'r').readlines():
        reqs.append(line)
    return reqs


# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="cqt_rng", 
        version=VERSION,
	author='',
	author_email='',
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=get_requires()
        
        keywords=['rng', 'quantum'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            'Programming Language :: Python :: 3.6',
        ]
)
