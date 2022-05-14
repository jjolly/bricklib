FROM ecpe4s/ubuntu20.04-spack
MAINTAINER John Jolly (john.jolly@utah.edu)

RUN . /spack/share/spack/setup-env.sh && spack install bzip2
RUN . /spack/share/spack/setup-env.sh && spack install gdbm
RUN . /spack/share/spack/setup-env.sh && spack install perl
RUN . /spack/share/spack/setup-env.sh && spack install autoconf
RUN . /spack/share/spack/setup-env.sh && spack install automake
RUN . /spack/share/spack/setup-env.sh && spack install cmake
RUN . /spack/share/spack/setup-env.sh && spack install libtool
RUN . /spack/share/spack/setup-env.sh && spack install hwloc
RUN . /spack/share/spack/setup-env.sh && spack install openmpi

COPY package.py /spack/var/spack/repos/builtin/packages/bricks/

RUN . /spack/share/spack/setup-env.sh && spack install bricks

