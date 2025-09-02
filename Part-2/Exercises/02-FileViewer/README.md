# Project Overview

This project demonstrates a web-based VTK file viewer using WebAssembly (WASM) and Emscripten. It allows users to load and visualize VTK XML PolyData files (.vtp) directly in the browser. Open each file and read the exercises description at the top and complete the implementation. You may check your code with the files in the "Solution" directory.

## File Descriptions

1. **CMakeLists.txt**
    - CMake build configuration for compiling the C++ source to WebAssembly using Emscripten.
    - Finds required VTK modules and sets up the build for the `FileViewer` executable.
    - Specifies Emscripten-specific linker options for modularization, ES6 export, memory growth, and runtime method exports.
2. **FileViewer.cpp**
    - Main C++ source file implementing the `FileViewer` class.
    - Provides two main methods:
        - `WriteDataFileToVirtualFS`: Writes a file from a memory buffer into the WASM virtual filesystem.
        - `ShowFile`: Loads and visualizes a .vtp file using VTK, rendering it in the browser.
    - Uses Emscripten bindings to expose the class and its methods to JavaScript.
3. **index.html**
    - The main HTML page for the viewer.
    - Contains a `<canvas>` element for rendering the VTK scene.
    - Loads the main JavaScript module (`index.js`).
4. **index.js**
    - Main JavaScript entry point.
    - Loads the WASM module and creates a `FileViewer` instance.
    - Downloads a file from a URL, copies it into the WASM virtual filesystem, and visualizes it.
    - Uses helper functions for file download and wasm memory transfer.
5. **utilities/download.js**
    - Utility function to download a file from a URL.
    - Extracts the filename from the HTTP content-disposition header if available.
    - Returns a Blob and the filename.
6. **utilities/writeFileToWasmMemory.js**
    - Utility for writing a file (Blob) into WASM memory.
    - Handles chunking of large files and memory allocation in the WASM heap.
    - Exports a function to copy file data into WASM memory and return a pointer.

## How It Works
1. The user provides a file URL (via the `fileUrl` query parameter, ex: http://localhost:8080?fileUrl=https://....).
2. The JavaScript code downloads the file and copies it into the WASM virtual filesystem.
3. The C++ FileViewer class loads and visualizes the file using VTK, rendering the result in the browser canvas.

# Build

1. Configure the project
   
    ```sh
    docker run --rm -it -v"$PWD":/work kitware/vtk-wasm-sdk:latest emcmake cmake -GNinja -S /work -B /work/build -DVTK_DIR=/VTK-install/Release/wasm32/lib/cmake/vtk
    ```
2. Compile


    ```sh
    docker run --rm -it -v"$PWD":/work kitware/vtk-wasm-sdk:latest cmake --build /work/build
    ```

# Serve and test generated code

```
cd build
python3 -m http.server 8000
```

Open your browser to http://localhost:8000/?fileUrl=https://data.kitware.com/api/v1/file/6285865d4acac99f429d979b/download

