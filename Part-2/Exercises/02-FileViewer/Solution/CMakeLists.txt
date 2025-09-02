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
  -O2
  -g2
  -lembind
  -sMODULARIZE=1
  -sEXPORT_NAME=createFileViewerModule
  -sEXPORT_ES6=1
  -sALLOW_MEMORY_GROWTH=1
  "-sEXPORTED_FUNCTIONS=['_malloc', '_free']"
  "-sEXPORTED_RUNTIME_METHODS=['HEAPU8']"
)
vtk_module_autoinit(
  TARGETS FileViewer
  MODULES ${VTK_LIBRARIES}
)
