"""
Unit test of ScanPoint

Author: Shisato Yano
"""

import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pytest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).absolute().parent) + "/../src/components/sensors/lidar")
from scan_point import ScanPoint


# test instance
point = ScanPoint(1.0, 2.0, 3.0, 4.0)


def test_initialize():
    assert point.distance_m == 1.0
    assert point.angle_rad == 2.0
    assert point.point_array != None
    assert point.transformed_x == None
    assert point.transformed_y == None


def test_get_distance_m():
    assert point.get_distance_m() == 1.0


def test_draw():
    plt.clf()
    plt.close()
    
    figure = plt.figure(figsize=(8, 8))
    axes = figure.add_subplot(111)
    point.draw(axes, [])
