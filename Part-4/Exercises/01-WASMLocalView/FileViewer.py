# EXERCISE: Create a file viewer using vtklocal widget. The file name should be provided as a command line argument.
#           The file will be opened using vtkXMLPolyDataReader or vtkXMLMultiBlockDataReader depending on the extension.
#           Supported extensions are .vtm and .vtp. The create_vtk_pipeline function is provided to create the VTK pipeline.
#           You need to:
#           1) Get the filename from server command line arguments in DemoApp.__init__
#           2) Initialize the VTK pipeline using create_vtk_pipeline and store the render window in self.render_window
#           3) Call self._build_ui() at the end of DemoApp.__init
#           4) Add a vtklocal.LocalView in DemoApp._build_ui to display the render window
# The LocalView should fill the entire browser window.
#
# HINT: See the documentation for vtklocal.LocalView constructor: https://trame.readthedocs.io/en/latest/trame.widgets.vtklocal.html#trame.widgets.vtklocal.LocalView
#
# RUNNING: python FileViewer.py -f <path_to_vtm_or_vtp_file>
#
# Refer to FileViewer-Solution.py for the solution if you get stuck.
from trame.app import TrameApp
from trame.ui.html import DivLayout
from trame.widgets import html, client
from trame_vtklocal.widgets import vtklocal
from trame.decorators import trigger

from vtkmodules.vtkIOXML import vtkXMLPolyDataReader, vtkXMLMultiBlockDataReader
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
)

# Required for vtk factory
import vtkmodules.vtkRenderingOpenGL2  # noqa
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleSwitch  # noqa

CLIENT_TYPE = "vue3"

# -----------------------------------------------------------------------------
# VTK pipeline
# -----------------------------------------------------------------------------


def create_vtk_pipeline(file_name):
    renderer = vtkRenderer()
    renderWindow = vtkRenderWindow()
    renderWindow.AddRenderer(renderer)

    renderWindowInteractor = vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)
    renderWindowInteractor.GetInteractorStyle().SetCurrentStyleToTrackballCamera()

    renderer.SetBackground(0.1, 0.2, 0.4)
    renderer.ResetCamera()

    # TODO: Create VTK pipeline using vtkXMLPolyDataReader or vtkXMLMultiBlockDataReader, based on file extension

    return renderWindow


# -----------------------------------------------------------------------------
# GUI
# -----------------------------------------------------------------------------


class DemoApp(TrameApp):
    def __init__(self, server=None):
        super().__init__(server, client_type=CLIENT_TYPE)
        # TODO: Get filename from server arguments, initialize VTK pipeline with create_vtk_pipeline and call _build_ui

    def _build_ui(self):
        with DivLayout(self.server) as self.ui:
            client.Style("body { margin: 0; }")
            with html.Div(
                style="position: absolute; left: 0; top: 0; width: 100vw; height: 100vh;"
            ):
                pass
                # TODO: Add vtklocal.LocalView here.

# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    app = DemoApp()
    app.server.start()
