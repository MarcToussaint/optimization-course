# Optimization Algorithms course

This repo is based on the RAI code, including its python bindings. See https://github.com/MarcToussaint/rai for a README of the RAI code.



## Quick Start

This assumes a standard Ubuntu 18.04 machine.

* The following assumes $HOME/git as your git path, and $HOME/opt
to install 3rd-party libs -- please stick to this (no system-wide installs)

* Clone the repo, install Ubuntu packages, & compile with cmake:
```
mkdir -p $HOME/git
cd $HOME/git
git clone https://github.com/MarcToussaint/optimization-course.git
cd optimization-course

git submodule init
git submodule update

make -j1 printUbuntuAll    # for your information: what the next step will install
make -j1 installUbuntuAll  # calls sudo apt-get install; you can always interrupt

mkdir build
cd build
cmake ..
make -j $(command nproc)
```

* Install python packages:
```
pip3 install --user \
	pybind11 \
	jupyter matplotlib
```

* Test
```
jupyter-notebook tutorials/how_to_query_an_NLP.ipynb
```

* For a Docker with Ubuntu 18.04, see [here](https://github.com/MarcToussaint/rai-maintenance/tree/master/docker/full18)

* When pulling updates for the repo, don't forget to also update the submodules:
```
git pull
git submodule update
```


# Documentation

* [Sphinx documentation (preliminary)](https://marctoussaint.github.io/optimization-course/)
