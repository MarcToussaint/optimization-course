cmake_minimum_required(VERSION 3.4)

project(RaiOptimizationCourse)

set(CMAKE_CXX_STANDARD 14 CACHE STRING "C++ version selection")

option(USE_PYBIND "build python bindings" ON)
option(USE_BULLET "link to bullet" ON)
option(USE_OPENCV "link to opencv" OFF)
option(USE_REALSENSE "link to realsense2 driver library" OFF)
option(USE_LIBFRANKA "link to libfranka" OFF)

add_compile_options(
  -O3 -g -Wall -Wpedantic -fPIC -std=c++14 -Wno-terminate
  )

################################################################################

add_definitions(
  -DRAI_ROOT_PATH=\"${CMAKE_SOURCE_DIR}/rai\"
  -DRAI_X11 -DRAI_LAPACK -DRAI_EIGEN -DRAI_PTHREAD
  -DRAI_GL
  -DRAI_GLFW -DRAI_ANN -DRAI_QHULL -DRAI_ASSIMP -DNO_CYCLE_DETECTION -DRAI_PNG -DRAI_PLY
  -DRAI_GJK -DRAI_CCD -DRAI_FCL
  )

################################################################################

include_directories(
  rai/rai
  /usr/include/eigen3
  )

file(GLOB SRC_Core rai/rai/Core/unity.cxx)
file(GLOB SRC_Optim rai/rai/Optim/unity.cxx)
file(GLOB SRC_Geo rai/rai/Geo/unity.cxx)
file(GLOB SRC_GeoGJK rai/rai/Geo/GJK/*.c)
file(GLOB SRC_GeoPly rai/rai/Geo/ply/*.c)
file(GLOB SRC_GeoLewiner rai/rai/Geo/Lewiner/unity.cxx)
file(GLOB SRC_Algo rai/rai/Algo/unity.cxx)
file(GLOB SRC_Gui rai/rai/Gui/unity.cxx)
file(GLOB SRC_Kin rai/rai/Kin/unity.cxx)
file(GLOB SRC_KinSwift rai/rai/Kin/SWIFT/unity.cxx)
file(GLOB SRC_KOMO rai/rai/KOMO/unity.cxx)
file(GLOB SRC_Logic rai/rai/Logic/unity.cxx)
file(GLOB SRC_LGP rai/rai/LGP/unity.cxx)
file(GLOB SRC_Perception rai/rai/Perception/unity.cxx)
file(GLOB SRC_Control rai/rai/Control/unity.cxx)
file(GLOB SRC_ry rai/rai/ry/unity.cxx)

add_library(rai SHARED
  ${SRC_Core}
  ${SRC_Optim}
  ${SRC_Geo}
  ${SRC_GeoGJK}
  ${SRC_GeoPly}
  ${SRC_GeoLewiner}
  ${SRC_Algo}
  ${SRC_Gui}
  ${SRC_Kin}
  ${SRC_KOMO}
  ${SRC_Logic}
  )

target_link_libraries(rai
  jsoncpp lapack blas pthread rt X11
  assimp ann glfw GLEW glut GLU GL png qhull ccd fcl
#  portaudio
#  boost_system 
  )

################################################################################

find_package (Eigen3 3.3 REQUIRED NO_MODULE)
target_link_libraries (rai Eigen3::Eigen)

if(USE_BULLET)
  find_package(Bullet REQUIRED)
  add_definitions(-DRAI_BULLET)
  include_directories(${BULLET_INCLUDE_DIRS})
  target_link_libraries(rai ${BULLET_LIBRARIES})
  message(STATUS "[rai] using bullet libs:" ${BULLET_LIBRARIES})
endif()

if(USE_OPENCV)
  find_package(OpenCV REQUIRED)
  add_definitions(-DRAI_OPENCV)
  target_link_libraries(rai ${OpenCV_LIBS})
endif()

if(USE_REALSENSE)
  add_definitions(-DRAI_REALSENSE)
  target_link_libraries(rai realsense2)
endif()

if(USE_LIBFRANKA)
  add_definitions(-DRAI_FRANKA)
  target_link_libraries(rai franka)
endif()

################################################################################

if(USE_PYBIND)
  set(PYTHON_EXECUTABLE "python3")
  message(STATUS "[rai] using python executable " ${PYTHON_EXECUTABLE} )
  execute_process(
    COMMAND bash "-c" "${PYTHON_EXECUTABLE} -m pybind11 --cmakedir" 
    OUTPUT_STRIP_TRAILING_WHITESPACE OUTPUT_VARIABLE pybind11_DIR
  )
  message(STATUS "[rai] using pybind11_DIR " ${pybind11_DIR} )
  
  find_package(pybind11)
  add_definitions(-DRAI_PYBIND)

  pybind11_add_module(libry SHARED
    ${SRC_ry}
  )

  target_link_libraries(libry PRIVATE
    rai
  )
endif()

################################################################################

add_executable(kinEdit rai/bin/src_kinEdit/main.cpp)
target_link_libraries(kinEdit rai)

add_executable(testSim rai/test/Kin/simulation/main.cpp)
target_link_libraries(testSim rai)


