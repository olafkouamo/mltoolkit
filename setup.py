from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='mltoolkit',
      version='0.1',
      description='some modelling tools',
      long_description=readme(),
      url='https://github.com/tounnas/mltoolkit',
      author='tounnas',
      author_email='',
      license='new BSD',
      packages=find_packages(),
      install_requires=['numpy', 'sklearn', 'argparse', 'multiprocessing', 'hyperopt'] +
                       ['bson', 'pymongo', 'networkx', 'scipy'],
      test_suite='nose.collector',
      tests_require=['nose'],
      scripts=[],
      include_package_data=True,
      zip_safe=False)
