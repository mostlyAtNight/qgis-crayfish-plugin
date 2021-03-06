# -*- coding: utf-8 -*-

# Crayfish - A collection of tools for TUFLOW and other hydraulic modelling packages
# Copyright (C) 2012 Peter Wells for Lutra Consulting

# peter dot wells at lutraconsulting dot co dot uk
# Lutra Consulting
# 23 Chestnut Close
# Burgess Hill
# West Sussex
# RH15 8HN

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.from PyQt4.QtCore import *

import os
import sipconfig
from PyQt4 import pyqtconfig

# The name of the SIP build file generated by SIP and used by the build
# system.
build_file = "crayfish_viewer.sbf"

# Get the PyQt configuration information.
config = pyqtconfig.Configuration()

# Get the extra SIP flags needed by the imported PyQt modules.  Note that
# this normally only includes those flags (-x and -t) that relate to SIP's
# versioning system.
pyqt_sip_flags = config.pyqt_sip_flags

# Run SIP to generate the code.  Note that we tell SIP where to find the qt
# module's specification files using the -I flag.
os.system(" ".join([config.sip_bin, "-c", ".", "-b", build_file, "-I", config.pyqt_sip_dir, pyqt_sip_flags, "crayfish_viewer.sip"]))

# We are going to install the SIP specification file for this module and
# its configuration module.
installs = []

installs.append(["crayfish_viewer.sip", os.path.join(config.default_sip_dir, "crayfish_viewer")])

installs.append(["crayfish_viewerconfig.py", config.default_mod_dir])

# Create the Makefile.  The QtGuiModuleMakefile class provided by the
# pyqtconfig module takes care of all the extra preprocessor, compiler and
# linker flags needed by the Qt library.
makefile = pyqtconfig.QtGuiModuleMakefile(
    configuration=config,
    build_file=build_file,
    installs=installs
)

# Add the library we are wrapping.  The name doesn't include any platform
# specific prefixes or extensions (e.g. the "lib" prefix on UNIX, or the
# ".dll" extension on Windows).
# Linux
makefile.extra_lib_dirs = ["build/release"]
makefile.extra_libs = ["crayfishViewer"]
# Windows
# makefile.extra_libs = ["build/release/crayfishViewer"]

# Generate the Makefile itself.
makefile.generate()

# Now we create the configuration module.  This is done by merging a Python
# dictionary (whose values are normally determined dynamically) with a
# (static) template.
content = {
    # Publish where the SIP specifications for this module will be
    # installed.
    "crayfish_viewer_sip_dir":    config.default_sip_dir,

    # Publish the set of SIP flags needed by this module.  As these are the
    # same flags needed by the qt module we could leave it out, but this
    # allows us to change the flags at a later date without breaking
    # scripts that import the configuration module.
    "crayfish_viewer_sip_flags":  pyqt_sip_flags
}

# This creates the helloconfig.py module from the helloconfig.py.in
# template and the dictionary.
sipconfig.create_config_module("crayfish_viewer_config.py", "crayfish_viewer_config.py.in", content)
