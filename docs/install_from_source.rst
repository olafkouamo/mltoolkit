Install From Source
===================

If you want to install the library form the source, you may first need to install *conda-build* :

.. code-block:: bash

    conda install conda-build

Then clone the repo or download it :

.. code-block:: bash

    git clone git@github.com:tounnas/mltoolkit.git

And build the project :

.. code-block:: bash

    cd mltoolkit/_build
    conda build .

You can then install the library :

.. code-block:: bash

    conda install --use-local mltoolkit