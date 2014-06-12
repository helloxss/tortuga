# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.8

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canoncical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# The program to use to edit the cache.
CMAKE_EDIT_COMMAND = /usr/bin/ccmake

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/tortuga/vehicle_refactor

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/tortuga/vehicle_refactor/build

# Include any dependencies generated for this target.
include packages/vision/CMakeFiles/SuitHistoCalculator.dir/depend.make

# Include the progress variables for this target.
include packages/vision/CMakeFiles/SuitHistoCalculator.dir/progress.make

# Include the compile flags for this target's objects.
include packages/vision/CMakeFiles/SuitHistoCalculator.dir/flags.make

packages/vision/CMakeFiles/SuitHistoCalculator.dir/test/src/SuitHistoCalculatorTest.cpp.o: packages/vision/CMakeFiles/SuitHistoCalculator.dir/flags.make
packages/vision/CMakeFiles/SuitHistoCalculator.dir/test/src/SuitHistoCalculatorTest.cpp.o: ../packages/vision/test/src/SuitHistoCalculatorTest.cpp
	$(CMAKE_COMMAND) -E cmake_progress_report /home/tortuga/vehicle_refactor/build/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object packages/vision/CMakeFiles/SuitHistoCalculator.dir/test/src/SuitHistoCalculatorTest.cpp.o"
	cd /home/tortuga/vehicle_refactor/build/packages/vision && /usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/SuitHistoCalculator.dir/test/src/SuitHistoCalculatorTest.cpp.o -c /home/tortuga/vehicle_refactor/packages/vision/test/src/SuitHistoCalculatorTest.cpp

packages/vision/CMakeFiles/SuitHistoCalculator.dir/test/src/SuitHistoCalculatorTest.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/SuitHistoCalculator.dir/test/src/SuitHistoCalculatorTest.cpp.i"
	cd /home/tortuga/vehicle_refactor/build/packages/vision && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /home/tortuga/vehicle_refactor/packages/vision/test/src/SuitHistoCalculatorTest.cpp > CMakeFiles/SuitHistoCalculator.dir/test/src/SuitHistoCalculatorTest.cpp.i

packages/vision/CMakeFiles/SuitHistoCalculator.dir/test/src/SuitHistoCalculatorTest.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/SuitHistoCalculator.dir/test/src/SuitHistoCalculatorTest.cpp.s"
	cd /home/tortuga/vehicle_refactor/build/packages/vision && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /home/tortuga/vehicle_refactor/packages/vision/test/src/SuitHistoCalculatorTest.cpp -o CMakeFiles/SuitHistoCalculator.dir/test/src/SuitHistoCalculatorTest.cpp.s

packages/vision/CMakeFiles/SuitHistoCalculator.dir/test/src/SuitHistoCalculatorTest.cpp.o.requires:
.PHONY : packages/vision/CMakeFiles/SuitHistoCalculator.dir/test/src/SuitHistoCalculatorTest.cpp.o.requires

packages/vision/CMakeFiles/SuitHistoCalculator.dir/test/src/SuitHistoCalculatorTest.cpp.o.provides: packages/vision/CMakeFiles/SuitHistoCalculator.dir/test/src/SuitHistoCalculatorTest.cpp.o.requires
	$(MAKE) -f packages/vision/CMakeFiles/SuitHistoCalculator.dir/build.make packages/vision/CMakeFiles/SuitHistoCalculator.dir/test/src/SuitHistoCalculatorTest.cpp.o.provides.build
.PHONY : packages/vision/CMakeFiles/SuitHistoCalculator.dir/test/src/SuitHistoCalculatorTest.cpp.o.provides

packages/vision/CMakeFiles/SuitHistoCalculator.dir/test/src/SuitHistoCalculatorTest.cpp.o.provides.build: packages/vision/CMakeFiles/SuitHistoCalculator.dir/test/src/SuitHistoCalculatorTest.cpp.o
.PHONY : packages/vision/CMakeFiles/SuitHistoCalculator.dir/test/src/SuitHistoCalculatorTest.cpp.o.provides.build

# Object files for target SuitHistoCalculator
SuitHistoCalculator_OBJECTS = \
"CMakeFiles/SuitHistoCalculator.dir/test/src/SuitHistoCalculatorTest.cpp.o"

# External object files for target SuitHistoCalculator
SuitHistoCalculator_EXTERNAL_OBJECTS =

packages/vision/SuitHistoCalculator: packages/vision/CMakeFiles/SuitHistoCalculator.dir/test/src/SuitHistoCalculatorTest.cpp.o
packages/vision/SuitHistoCalculator: lib/libram_vision.so
packages/vision/SuitHistoCalculator: lib/libram_math.so
packages/vision/SuitHistoCalculator: lib/libram_core.so
packages/vision/SuitHistoCalculator: /opt/ram/local/lib/libboost_system.so
packages/vision/SuitHistoCalculator: /opt/ram/local/lib/libboost_filesystem.so
packages/vision/SuitHistoCalculator: /opt/ram/local/lib/libboost_date_time.so
packages/vision/SuitHistoCalculator: /opt/ram/local/lib/libboost_python.so
packages/vision/SuitHistoCalculator: /opt/ram/local/lib/libboost_signals.so
packages/vision/SuitHistoCalculator: /opt/ram/local/lib/liblog4cpp.so
packages/vision/SuitHistoCalculator: /usr/lib/libpython2.6.so
packages/vision/SuitHistoCalculator: /home/tortuga/opencv-2.4.5/build/lib/libopencv_calib3d.so
packages/vision/SuitHistoCalculator: /home/tortuga/opencv-2.4.5/build/lib/libopencv_contrib.so
packages/vision/SuitHistoCalculator: /home/tortuga/opencv-2.4.5/build/lib/libopencv_core.so
packages/vision/SuitHistoCalculator: /home/tortuga/opencv-2.4.5/build/lib/libopencv_features2d.so
packages/vision/SuitHistoCalculator: /home/tortuga/opencv-2.4.5/build/lib/libopencv_flann.so
packages/vision/SuitHistoCalculator: /home/tortuga/opencv-2.4.5/build/lib/libopencv_gpu.so
packages/vision/SuitHistoCalculator: /home/tortuga/opencv-2.4.5/build/lib/libopencv_highgui.so
packages/vision/SuitHistoCalculator: /home/tortuga/opencv-2.4.5/build/lib/libopencv_imgproc.so
packages/vision/SuitHistoCalculator: /home/tortuga/opencv-2.4.5/build/lib/libopencv_legacy.so
packages/vision/SuitHistoCalculator: /home/tortuga/opencv-2.4.5/build/lib/libopencv_ml.so
packages/vision/SuitHistoCalculator: /home/tortuga/opencv-2.4.5/build/lib/libopencv_nonfree.so
packages/vision/SuitHistoCalculator: /home/tortuga/opencv-2.4.5/build/lib/libopencv_objdetect.so
packages/vision/SuitHistoCalculator: /home/tortuga/opencv-2.4.5/build/lib/libopencv_photo.so
packages/vision/SuitHistoCalculator: /home/tortuga/opencv-2.4.5/build/lib/libopencv_stitching.so
packages/vision/SuitHistoCalculator: /home/tortuga/opencv-2.4.5/build/lib/libopencv_superres.so
packages/vision/SuitHistoCalculator: /home/tortuga/opencv-2.4.5/build/lib/libopencv_ts.so
packages/vision/SuitHistoCalculator: /home/tortuga/opencv-2.4.5/build/lib/libopencv_video.so
packages/vision/SuitHistoCalculator: /home/tortuga/opencv-2.4.5/build/lib/libopencv_videostab.so
packages/vision/SuitHistoCalculator: /opt/ram/local/lib/libboost_thread.so
packages/vision/SuitHistoCalculator: /opt/ram/local/lib/libboost_serialization.so
packages/vision/SuitHistoCalculator: /opt/ram/local/lib/libboost_regex.so
packages/vision/SuitHistoCalculator: /usr/lib/libdc1394.so
packages/vision/SuitHistoCalculator: /opt/ram/local/lib/libfann.so
packages/vision/SuitHistoCalculator: /opt/ram/local/lib/libfloatfann.so
packages/vision/SuitHistoCalculator: /usr/lib/libfftw3.so
packages/vision/SuitHistoCalculator: packages/vision/CMakeFiles/SuitHistoCalculator.dir/build.make
packages/vision/SuitHistoCalculator: packages/vision/CMakeFiles/SuitHistoCalculator.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX executable SuitHistoCalculator"
	cd /home/tortuga/vehicle_refactor/build/packages/vision && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/SuitHistoCalculator.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
packages/vision/CMakeFiles/SuitHistoCalculator.dir/build: packages/vision/SuitHistoCalculator
.PHONY : packages/vision/CMakeFiles/SuitHistoCalculator.dir/build

packages/vision/CMakeFiles/SuitHistoCalculator.dir/requires: packages/vision/CMakeFiles/SuitHistoCalculator.dir/test/src/SuitHistoCalculatorTest.cpp.o.requires
.PHONY : packages/vision/CMakeFiles/SuitHistoCalculator.dir/requires

packages/vision/CMakeFiles/SuitHistoCalculator.dir/clean:
	cd /home/tortuga/vehicle_refactor/build/packages/vision && $(CMAKE_COMMAND) -P CMakeFiles/SuitHistoCalculator.dir/cmake_clean.cmake
.PHONY : packages/vision/CMakeFiles/SuitHistoCalculator.dir/clean

packages/vision/CMakeFiles/SuitHistoCalculator.dir/depend:
	cd /home/tortuga/vehicle_refactor/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/tortuga/vehicle_refactor /home/tortuga/vehicle_refactor/packages/vision /home/tortuga/vehicle_refactor/build /home/tortuga/vehicle_refactor/build/packages/vision /home/tortuga/vehicle_refactor/build/packages/vision/CMakeFiles/SuitHistoCalculator.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : packages/vision/CMakeFiles/SuitHistoCalculator.dir/depend

