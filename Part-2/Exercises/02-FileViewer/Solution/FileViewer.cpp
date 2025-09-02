#include <vtkActor.h>
#include <vtkInteractorStyleTrackballCamera.h>
#include <vtkNew.h>
#include <vtkPolyDataMapper.h>
#include <vtkRenderWindow.h>
#include <vtkRenderWindowInteractor.h>
#include <vtkRenderer.h>
#include <vtkXMLPolyDataReader.h>

#include <vtksys/SystemTools.hxx>

#include <emscripten.h>
#include <emscripten/bind.h>

#include <fstream>
#include <iostream>

class FileViewer {
  vtkNew<vtkRenderWindowInteractor> m_renderWindowInteractor;

public:
  FileViewer() {
    vtkRenderWindowInteractor::InteractorManagesTheEventLoop = false;
  }

  ~FileViewer() = default;

  /**
   * Write data from a memory buffer to a file in the virtual filesystem.
   * @param filename The name of the file to write to
   * @param buffer A pointer to the memory buffer containing the data
   * @param nbytes The number of bytes to write from the buffer
   */
  void WriteDataFileToVirtualFS(const std::string &filename,
                                std::uintptr_t buffer, std::size_t nbytes) {
    using systools = vtksys::SystemTools;
    const auto parentDir = systools::GetParentDirectory(filename);
    if (!parentDir.empty()) {
      if (!systools::MakeDirectory(parentDir).IsSuccess()) {
        std::cerr << "ERROR: Failed to create parent directory for file = "
                  << filename << '\n';
      }
    }
    std::ofstream ofs(filename, std::ios::binary);
    ofs.write(reinterpret_cast<char *>(buffer), nbytes);
    std::cout << "Wrote " << nbytes << " bytes into " << filename << '\n';
  }

  /**
   * Load and visualize a VTK XML PolyData file (e.g., .vtp)
   * @param filename The name of the file to load
   * @return 1 on success, 0 on failure
   */
  int ShowFile(const std::string &filename) {
    // Verify input arguments
    if (filename.empty()) {
      std::cerr << "ERROR: No input filename specified.\n";
      return 0;
    }

    std::cout << "Reading file: " << filename << std::endl;

    // Read the file
    vtkNew<vtkXMLPolyDataReader> reader;
    reader->SetFileName(filename.c_str());

    // Create a mapper and actor
    vtkNew<vtkPolyDataMapper> mapper;
    mapper->SetInputConnection(reader->GetOutputPort());

    vtkNew<vtkActor> actor;
    actor->SetMapper(mapper);

    // Create a renderer, render window, and interactor
    vtkNew<vtkRenderer> renderer;
    vtkNew<vtkRenderWindow> renderWindow;
    renderWindow->AddRenderer(renderer);
    this->m_renderWindowInteractor->SetRenderWindow(renderWindow);

    // Add the actor to the scene
    renderer->AddActor(actor);

    // Render and interact
    renderWindow->Render();

    vtkNew<vtkInteractorStyleTrackballCamera> style;
    this->m_renderWindowInteractor->SetInteractorStyle(style);
    this->m_renderWindowInteractor->Start();

    return 1;
  }
};

/**
 * Bindings for the FileViewer class
 */
EMSCRIPTEN_BINDINGS(FileViewerModule) {
  emscripten::class_<FileViewer>("FileViewer")
      .constructor()
      .function("WriteDataFileToVirtualFS",
                &FileViewer::WriteDataFileToVirtualFS)
      .function("ShowFile", &FileViewer::ShowFile);
}
