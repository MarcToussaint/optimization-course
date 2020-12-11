# Optimization Algorithms course

This repo is based on the RAI code, including its python bindings. See https://github.com/MarcToussaint/rai for a README of the RAI code.



## Compile directly on Ubuntu

This assumes a standard Ubuntu 20.04 machine.

* The following assumes $HOME/git as your git path, and $HOME/opt
to install 3rd-party libs -- please stick to this (no system-wide installs)

* Install basics
```
sudo apt-get update
sudo apt-get install git sudo build-essential cmake
```

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
pip3 install --user pybind11 jupyter matplotlib
```

* Test
```
cd $HOME/git/optimization-course
jupyter-notebook tutorials/how_to_query_an_NLP.ipynb
```

* When pulling updates for the repo, don't forget to also update the submodules:
```
git pull
git submodule update
```

## Use Docker on Ubuntu

* Install docker engine for Ubuntu as described [here](https://docs.docker.com/engine/install/ubuntu/), namely:
```
sudo apt-get update
sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
```

* Add your user to the docker user group (otherwise use *sudo* in front of all docker commands below)
```
sudo usermod -aG docker ${USER}
```
Log out and in again!

* Download [this docker](https://hub.docker.com/r/marctoussaint/rai-optim20) from docker hub:
```
docker pull marctoussaint/rai-optim20
```

* Run the docker, mounting your $HOME directory as ~/home
```
xhost +local:root
docker run -it \
       --volume="$HOME/:/root/home" \
       --env="DISPLAY" \
       --network host \
       --device /dev/input \
       rai-optim20 /bin/bash
```

* When running the docker you should get a *** Welcome *** message. You can now run the jupyter server within the docker:
```
jupyter-notebook optimization-course/tutorials --ip 0.0.0.0 --no-browser --allow-root &
```
This starts a jupyter server without browser. You can now open your normal Ubuntu browser and access the Jupyter server at
http://localhost:8888/?token=... as displayed on the console.

* Whenever you close the docker, the jupyter server and local changes in optimization-course/tutorials get lost. To prevent this, create notbooks in your ~/home directory, which mounts your actual Ubuntu $HOME. (Or mount other paths, as you like.)

* Side note: [This is how the docker was created](https://github.com/MarcToussaint/rai-maintenance/tree/master/docker/optim20)

## Compile on Windows within Ubuntu WSL

* From the Microsoft Store, install the 'Ubuntu 20.04 LTS' (which I think is a [WSL Ubuntu](https://ubuntu.com/wsl))

* When you launch it, you get some error on 'component is not enabled'. Follow the https://aka.ms/wslinstall instructions (including reboot)

* Launch the ubuntu

* Install basics
```
sudo apt-get update
sudo apt-get install git sudo build-essential cmake libjsoncpp-dev --fix-missing
```
* Follow the 'Compile directly on Ubuntu' instructions

* When launching jupyter, use --no-browser and direct your browser to the link displayed

* Installing X - I wasn't successful

<!---
[this X-server](https://sourceforge.net/projects/vcxsrv)

* call Xlaunch and choose 'disable access control' on the last option page

* call `export DISPLAY=0:0` before  launching jupyter
--->


## Use Docker on Windows

* Install Docker Desktop for Windows

* In a console, pull and run the docker:
```
docker pull marctoussaint/rai-optim20
docker run -it -p 8888:888 rai-optim20 /bin/bash
```

* Within the docker run jupyter
```
jupyter-notebook optimization-course/tutorials --ip 0.0.0.0 --allow-root
```





<!---
# Documentation
* [Sphinx documentation (preliminary)](https://marctoussaint.github.io/optimization-course/)
--->
