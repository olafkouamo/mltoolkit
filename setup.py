from setuptools import setup, find_packages
import codecs
import os
import re


here = os.path.abspath(os.path.dirname(__file__))


# Read the version number from a source file.
# Why read it, and not import?
# see https://groups.google.com/d/topic/pypa-dev/0PkjVpcxTzQ/discussion
def find_version(*file_paths):
    # Open in Latin-1 so that we avoid encoding errors.
    # Use codecs.open for Python 2 compatibility
    with codecs.open(os.path.join(here, *file_paths), 'r', 'latin1') as f:
        version_file = f.read()

    # The version line must have the form
    # __version__='ver'
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


# Get the long description from the relevant file
with codecs.open('DESCRIPTION.rst', encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='mltoolkit',
    version=find_version('mltoolkit', '__init__.py'),

    install_requires=[
        # computing packages
        'numpy>=1.8.1',
        'scipy>=0.16.0',
        'bson>=0.4.0',
        'networkx>=1.8.1',
        # IO-related packages
        'sklearn>=0.0',
        'argparse>=0.0',
        'multiprocessing',
        'hyperopt'
        'pymongo>=2.7.2',
    ],
    tests_require=[
        'coverage',
        'rednose',
        'nose',
        'nose-exclude'
    ],
    test_suite='nose.collector',
    dependency_links=[
    ],

    description="Automated pricing math part.",
    long_description=long_description,

    license='',
    author="Thomas Ounaas.",
    author_email="",
    url="",
    download_url='',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Operating System :: OS Independent',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering',
    ],


    packages=find_packages(),
)
