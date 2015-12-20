Install From Source
===================

If you want to install the library form the source, you may first need to install *conda-build* :

    conda install conda-build

Then clone the repo or download it :

    git clone git@github.com:tounnas/mltoolkit.git

And build the project :

    cd mltoolkit/_build

    conda build .

You can then install the library :

    conda install --use-local mltoolkit