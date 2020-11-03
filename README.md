# Optimization Algorithms course

This repo is based on RAI code, including its python bindings. See https://github.com/MarcToussaint/rai for a README of the RAI code.



## Quick Start

This assumes a standard Ubuntu 18.04 machine.

* The following assumes $HOME/git as your git path, and $HOME/opt
to install 3rd-party libs -- please stick to this (no system-wide installs)
* Install Ubuntu packages:
```
sudo apt-get install \
	g++ make gnupg gdb cmake gnuplot libjsoncpp-dev libx11-dev \
	liblapack-dev libf2c2-dev libeigen3-dev \
	libx11-dev \
	liblapack-dev libf2c2-dev \
	libnlopt-dev gfortran coinor-libipopt-dev \
	python3 python3-dev python3-numpy python3-pip python3-distutils
```
* Install python packages:
```
pip3 install --user \
	pybind11
	jupyter matplotlib
```
* Clone and compile the code:
```
mkdir -p $HOME/git
cd $HOME/git
git clone https://github.com/MarcToussaint/optimization-course.git
cd optimization-course

git submodule init
git submodule update

mkdir build
cd build
cmake ..
make -j $(command nproc)
```
* Test
```
jupyter-notebook tutorials/opt-1.ipynb
```

* For a Docker with Ubuntu 18.04, see [here](https://github.com/MarcToussaint/rai-maintenance/tree/master/docker/mini18) 

* When pulling updates for the repo, don't forget to also update the submodules:
```
git pull
git submodule update
```


# Documentation

* [Sphinx documentation (preliminary)](https://marctoussaint.github.io/optimization-course/)
