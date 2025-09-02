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

    if file_name.endswith(".vtm"):
        reader = vtkXMLMultiBlockDataReader(file_name=file_name)
        reader.Update()
        mbdset = reader.GetOutput()
        for i in range(mbdset.GetNumberOfBlocks()):
            block = mbdset.GetBlock(i)
            mapper = vtkPolyDataMapper(scalar_visibility=False)
            mapper.SetInputDataObject(0, block)
            actor = vtkActor()
            actor.SetMapper(mapper)
            renderer.AddActor(actor)
    elif file_name.endswith(".vtp"):
        reader = vtkXMLPolyDataReader(file_name=file_name)
        mapper = vtkPolyDataMapper(scalar_visibility=False)
        mapper.SetInputConnection(reader.GetOutputPort())
        actor = vtkActor()
        actor.SetMapper(mapper)
        renderer.AddActor(actor)
    else:
        raise ValueError(f"Unsupported file type: {file_name}")

    renderer.SetBackground(0.1, 0.2, 0.4)
    renderer.ResetCamera()

    return renderWindow


# -----------------------------------------------------------------------------
# GUI
# -----------------------------------------------------------------------------


class DemoApp(TrameApp):
    def __init__(self, server=None):
        super().__init__(server, client_type=CLIENT_TYPE)
        self.server.cli.add_argument("-f", "--filename", required=True)
        args, _ = self.server.cli.parse_known_args()
        file_name = args.filename

        self.render_window = create_vtk_pipeline(file_name)
        self._build_ui()

    def _build_ui(self):
        with DivLayout(self.server) as self.ui:
            client.Style("body { margin: 0; }")
            with html.Div(
                style="position: absolute; left: 0; top: 0; width: 100vw; height: 100vh;"
            ):
                self.html_view = vtklocal.LocalView(
                    self.render_window,
                    throttle_rate=20,
                )

# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    app = DemoApp()
    app.server.start()
