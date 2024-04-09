"""
extended_kalman_filter_localization.py

Author: Shisato Yano
"""

# import path setting
import sys
from pathlib import Path

abs_dir_path = str(Path(__file__).absolute().parent)
relative_path = "/../../../components/"

sys.path.append(abs_dir_path + relative_path + "visualization")
sys.path.append(abs_dir_path + relative_path + "state")
sys.path.append(abs_dir_path + relative_path + "vehicle")
sys.path.append(abs_dir_path + relative_path + "course/sin_curve_course")
sys.path.append(abs_dir_path + relative_path + "control/pure_pursuit")
sys.path.append(abs_dir_path + relative_path + "sensors")
sys.path.append(abs_dir_path + relative_path + "sensors/gnss")
sys.path.append(abs_dir_path + relative_path + "localization/kalman_filter")


# import component modules
from global_xy_visualizer import GlobalXYVisualizer
from min_max import MinMax
from time_parameters import TimeParameters
from vehicle_specification import VehicleSpecification
from state import State
from four_wheels_vehicle import FourWheelsVehicle
from sin_curve_course import SinCurveCourse
from pure_pursuit_controller import PurePursuitController
from sensors import Sensors
from gnss import Gnss
from extended_kalman_filter_localizer import ExtendedKalmanFilterLocalizer


# flag to show plot figure
# when executed as unit test, this flag is set as false
show_plot = True


def main():
    """
    Main process function
    """
    
    # set simulation parameters
    x_lim, y_lim = MinMax(-5, 55), MinMax(-20, 25)
    vis = GlobalXYVisualizer(x_lim, y_lim, TimeParameters(span_sec=30))

    # create course data instance
    course = SinCurveCourse(0, 50, 0.5, 20, color='k')
    vis.add_object(course)

    # create vehicle's spec instance
    spec = VehicleSpecification(area_size=20.0)
    
    # create vehicle's state instance
    state = State(color='b')
    
    # create controller instance
    pure_pursuit = PurePursuitController(spec, course, color='m')

    # create vehicle instance
    # set state, spec, controller, sensors and localizer instances as arguments
    gnss = Sensors(gnss=Gnss(x_noise_std=1.0, y_noise_std=1.0))
    ekf = ExtendedKalmanFilterLocalizer()
    vehicle = FourWheelsVehicle(state, spec, controller=pure_pursuit, sensors=gnss, localizer=ekf)
    vis.add_object(vehicle)

    # plot figure is not shown when executed as unit test
    if not show_plot: vis.not_show_plot()

    # show plot figure
    vis.draw()


# execute main process
if __name__ == "__main__":
    main()
