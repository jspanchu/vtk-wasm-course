# Homework Instructions

1. **Download Source Code**
	- Download the zip file from: [VTK Emscripten Examples](https://gitlab.kitware.com/vtk/vtk/-/archive/master/vtk-master.zip?path=Examples/Emscripten/Cxx).

2. **Extract and Copy Files**
	- Unzip the archive.
	- Copy all contents from:
	  `vtk-master-Examples-Emscripten-Cxx/Examples/Emscripten/Cxx/*`
	  into this directory.

3. **Build and Run Each Example**
	- Each subdirectory contains:
	  - `README.md`
	  - C++ source file
	  - `CMakeLists.txt`
	  - HTML/JS/CSS files
	- Open the `README.md` in each subdirectory.
	- Run the emcmake command (using `docker` and the `vtk-wasm-sdk` image) to build the project.
	- Run the resulting code in your browser and verify it works.
	- Repeat for every subdirectory.
