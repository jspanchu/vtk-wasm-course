# EXERCISE: Complete the CMakeLists.txt to build the FileViewer application
#           You will need to use the correct link flags to create a WebAssembly module.
#           Add link options for these features:
#           - Optimization level 2
#           - Debugging information at level 2 (to preserve function names in WASM)
#           - Embind support
#           - Modularization support
#           - Custom export name (createFileViewerModule)
#           - ES6 module support
#           - Allow memory growth
#           - Export malloc and free functions
#           - Export HEAPU8 runtime method
# 
# HINT: You may refer to the official Emscripten documentation for more details:
#       1. Emscripten compiler settings (the kind -s<FLAG>=<VALUE>): https://emscripten.org/docs/tools_reference/settings_reference.html
#       2. Emscripten compiler optimizations: https://emscripten.org/docs/tools_reference/emcc.html#arguments
cmake_minimum_required(VERSION 3.29)

project(FileViewer)

find_package(VTK REQUIRED
COMPONENTS
  CommonCore
  IOXML
  InteractionStyle
  RenderingCore
  RenderingOpenGL2
  RenderingUI
)

if (NOT VTK_FOUND)
  message(FATAL_ERROR  "VTK not found${VTK_NOT_FOUND_MESSAGE}")
endif ()

add_executable(FileViewer FileViewer.cpp)
target_link_libraries(FileViewer ${VTK_LIBRARIES})
target_link_options(FileViewer PRIVATE
# TODO: See the exercise description at the top of this file for the required link options
)
vtk_module_autoinit(
  TARGETS FileViewer
  MODULES ${VTK_LIBRARIES}
)
