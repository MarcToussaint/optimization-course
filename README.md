# Optimization Algorithms course

This repo is based on the RAI code, including its python bindings. See https://github.com/MarcToussaint/rai-python 

## Installation

Users should not need to compile code. Use the pip install below. If you want to compile the lib and python bindings yourself, look at the [rai-python README](https://github.com/MarcToussaint/rai-python)


* Some Ubuntu dependencies: (the pip package dynamically links to those)
```
sudo apt install liblapack3 freeglut3 libglew-dev python3 python3-pip
```
* pip-install robotic and dependencies (numpy, scipy)
```
python3 -m pip install robotic numpy scipy
```
* Test:
```
python3 -c 'from robotic import ry; ry.test.RndScene()'
```
If the `rai-robotModels` path fails, try one of the following:
```
cd $HOME && mkdir -p .local && cd $HOME/.local && ln -s /usr/local/rai-robotModels
#python3 -c 'from robotic import ry; ry.setRaiPath("/usr/local/rai-robotModels"); ry.test.RndScene()'
```
* Now you can test the example in this repo (clone parallel to the OA assignments repo)
```
git clone https://github.com/MarcToussaint/optimization-course.git
cd optimization-course/example
python3 main.py
```
