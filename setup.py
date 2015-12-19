from setuptools import setup, find_packages

from mltoolkit import __version__ as current_version
from mltoolkit import __author__ as author


def readme():
    with open('README.md') as f:
        return f.read()

setup(name='mltoolkit',
      version=current_version,
      description='Some modelling tools',
      long_description=readme(),
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Operating System :: OS Independent',
          'Intended Audience :: Science/Research',
          'Programming Language :: Python :: 2.7',
          'Topic :: Scientific/Engineering'
      ],
      url='https://pypi.python.org/pypi/mltoolkit',
      download_url="https://github.com/tounnas/mltoolkit",
      author=author,
      author_email='',
      license='new BSD',
      packages=find_packages(),
      install_requires=['numpy', 'scikit-learn', 'argparse', 'multiprocessing', 'hyperopt'] +
                       ['bson', 'pymongo', 'networkx'],
      test_suite='nose.collector',
      tests_require=['nose'],
      scripts=[],
      include_package_data=True,
      zip_safe=False)
