========================
Machine Learning Toolkit
========================
mltoolkit
---------


Installation
############

Create your specific environment (with conda)
=============================================

An empty one
^^^^^^^^^^^^

.. code-block:: bash

    conda create --name datasc python


From a existing one
^^^^^^^^^^^^^^^^^^^
You can check the list of current envs as follow

.. code-block:: bash

    conda info --list


You can then clone the root env like this

.. code-block:: bash

    conda create --name datasc --clone root


Activate your environment
=========================

.. code-block:: bash

    source activate datasc


Install the mltools library
===========================

From Binstar (Anaconda.org)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    conda install --channel https://conda.anaconda.org/tounnas mltoolkit


From source
^^^^^^^^^^^

.. code-block:: bash

    conda install conda-build
    git clone git@github.com:tounnas/mltoolkit.git
    cd mltoolkit/_build
    conda build .
    conda install --use-local mltoolkit


Utilisation
###########

Have a look to the examples folder

