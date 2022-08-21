.. CQTRNG documentation master file, created by
   sphinx-quickstart on Sun Aug 21 10:25:45 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to CQTRNG's documentation!
==================================

The CQTRNG package was developped for the `Womanium <https://www.womanium.org/>`_ & `ORCA Computing <https://www.orcacomputing.com/>`_'s hackathon. 

The challenge was about generating random numbers using boson sampling. As you will see, the package not only provide 
way(s) to generate random numbers via boson sampling but also implements other ways to generate random numbers. 
In addition, the package was designed to be extensible such that the end-user (or third-parties) can add new entropy sources and post processors.

Installation
==============
To install the package, run the following command::

   $ pip install cqt_rng
   

.. toctree::
   :maxdepth: 2
   :glob:
   :caption: Core:

   api/core/*

.. toctree::
   :maxdepth: 2
   :glob:
   :caption: Entropy Sources:

   api/ents/*


.. toctree::
   :maxdepth: 2
   :glob:
   :caption: Postprocessors:

   api/pp/*


.. toctree::
   :maxdepth: 2
   :glob:
   :caption: Utilities:

   api/utils/*

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
