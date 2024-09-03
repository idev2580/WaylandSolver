import sys
from wayland_solver.application import Application

if __name__ == '__main__':
    app = Application(application_id="work.idev2580dev.waylandsolver")
    app.run(sys.argv)
