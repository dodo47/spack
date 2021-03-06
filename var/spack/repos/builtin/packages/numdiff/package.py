# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Numdiff(AutotoolsPackage):
    """Numdiff is a little program that can be used to compare putatively
    similar files line by line and field by field, ignoring small numeric
    differences or/and different numeric formats."""

    homepage  = 'https://www.nongnu.org/numdiff'
    url       = 'http://nongnu.askapache.com/numdiff/numdiff-5.8.1.tar.gz'

    version('5.9.0', '794461a7285d8b9b1f2c4a8149889ea6')
    version('5.8.1', 'a295eb391f6cb1578209fc6b4f9d994e')

    variant('nls', default=False,
            description="Enable Natural Language Support")
    variant('gmp', default=False,
            description="Use GNU Multiple Precision Arithmetic Library")

    depends_on('gettext', when='+nls')
    depends_on('gmp', when='+gmp')

    def configure_args(self):
        spec = self.spec
        args = []
        if '+nls' in spec:
            args.append('--enable-nls')
        else:
            args.append('--disable-nls')

        if '+gmp' in spec:
            # compile with -O0 as per upstream known issue with optimization
            # and GMP; https://launchpad.net/ubuntu/+source/numdiff/+changelog
            # http://www.nongnu.org/numdiff/#issues
            # keep this variant off by default as one still encounter
            # GNU MP: Cannot allocate memory (size=2305843009206983184)
            args.extend([
                '--enable-gmp',
                'CFLAGS=-O0'
            ])
        else:
            args.append('--disable-gmp')

        return args
