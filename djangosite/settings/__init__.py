"""
Cascading settings.

    base.py
        Contains base settings that extend from one of the ``ixc_settings``
        modules (``develop``, ``production``, etc., or custom).

    project.py
        Contains settings for all deployments of this project.

    local.py
        Contains settings for this actual deployment. It should not be committed
        to version control, but a template with sample values can be committed
        as ``local.tmpl.py``.

        The first line of local.py should be::

            from .project import *

    calculated.py
        Contains settings that are calculated from other settings. E.g. to
        enable or disable functionality when ``DEBUG=True``.

"""
from .calculated import * 
