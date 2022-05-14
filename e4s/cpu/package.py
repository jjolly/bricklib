from spack import *

class Bricks(CMakePackage):

    """Bricks is a data layout and code generation framework, enabling performance-portable stencil computations across a multitude of architectures."""

    # url for your package's homepage here.
    homepage = "https://bricks.run/"
    url      = "https://github.com/jjolly/bricklib/archive/refs/heads/jjolly-buildarch.zip"

    # List of GitHub accounts to notify when the package is updated.
    maintainers = ['ztuowen', 'drhansj']

    version('r0.1', sha256='f99d5f3db3a540d05418ca86e53be12bc42234eef335896986a83e2d2052d1b1')

    # FIXME: Add dependencies if required.
    depends_on('autoconf', type='build', when='@r0.1')
    depends_on('automake', type='build', when='@r0.1')
    depends_on('libtool', type='build', when='@r0.1')
    depends_on('mpi')

    def cmake_args(self):

        # FIXME: Add arguments other than --prefix

        # FIXME: If not needed delete this function

        args = ["-DBUILD_ARCH=icelake-server"]
        return args
