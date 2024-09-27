.. |icon| image:: ./media/icon.svg
   :width: 50

###################
 |icon| code-scribe
###################

|Code style: black|

Jobrunner is a command line tool to manage and deploy computational
experiments, organize workflows, and enforce a directory-based hierarchy
to enable reuse of files and bash scripts along a directory tree.
Organization details of the tree are encoded in Jobfiles, which provide
an index of files and scripts on each node and indicate their
relationship with Jobrunner commands. It is a flexible tool that allows
users to design their own directory structure and maintain consistency
with the increase in complexity of their workflows and experiments.

Read our paper here: https://arxiv.org/abs/2308.15637

**************
 Installation
**************

There maybe situations where users may want to install Jobrunner in
development mode $\\textemdash$ to design new features, debug, or
customize options/commands to their needs. This can be easily
accomplished using the ``setup`` script located in the project root
directory and executing,

.. code::

   ./setup develop --with-instruments

Development mode enables testing of features/updates directly from the
source code and is an effective method for debugging. Note that the
``setup`` script relies on ``click``, which can be installed using,

.. code::

   pip install click

The ``jobrunner`` script is installed in ``$HOME/.local/bin`` directory
and therfore the environment variable, ``PATH``, should be updated to
include this location for command line use.

*******************
 Statement of Need
*******************

Use of software for data acquisition, analysis, and discovery in
scientific studies has allowed integration of sustainable software
development practices into the research process, enabling physics-based
simulation instruments like Flash-X (https://flash-x.org) to model
problems ranging from pool boiling to stellar explosions. However, the
design and management of software-based scientific studies is often left
to individual researchers who design their computational experiments
based on personal preferences and the nature of the study.

Although applications are available to create reproducible capsules for
data generation (https://codeocean.com), they do not provide tools to
manage research in a structured way which can enhance knowledge related
to decisions made by researchers to configure their software
instruments. A well-organized lab notebook and execution environment
enables systematic curation of the research process and provides
implicit documentation for software configuration and options used to
perform specific studies. This in turn enhances reproducibility by
providing a roadmap towards data generation and contributing towards
knowledge and understanding of an experiment.

Jobrunner addresses this need by enabling the management of software
environments for computational experiments that rely on a Unix-style
interface for development and execution. The design and operation of the
tool allow researchers to efficiently organize their workflows without
compromising their design preferences and requirements. We have applied
this tool to manage performance and computational fluid dynamics studies
using Flash-X.

.. |Code style: black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
