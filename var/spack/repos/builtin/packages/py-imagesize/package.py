# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyImagesize(PythonPackage):
    """Parses image file headers and returns image size. Supports PNG, JPEG,
    JPEG2000, and GIF image file formats."""

    homepage = "https://github.com/shibukawa/imagesize_py"
    url      = "https://pypi.io/packages/source/i/imagesize/imagesize-0.7.1.tar.gz"

    import_modules = ['imagesize']

    version('1.1.0',  sha256='f3832918bc3c66617f92e35f5d70729187676313caa60c187eb0f28b8fe5e3b5')
    version('0.7.1', '976148283286a6ba5f69b0f81aef8052')

    depends_on('py-setuptools', type='build')
