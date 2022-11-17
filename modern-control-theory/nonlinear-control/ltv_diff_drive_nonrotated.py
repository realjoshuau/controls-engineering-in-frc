#!/usr/bin/env python3

"""
Simulates LTV differential drive controller with RK4 integration in field
coordinate frame.
"""

import csv
import sys

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

from bookutil import latex
from bookutil.drivetrain import get_diff_vels
from bookutil.systems import LTVDifferentialDrive

if "--noninteractive" in sys.argv:
    mpl.use("svg")


class DifferentialDrive(LTVDifferentialDrive):
    """An frccontrol system for a differential drive."""

    def __init__(self, dt, states):
        """Differential drive subsystem.

        Keyword arguments:
        dt -- time between model/controller updates
        states -- state vector around which to linearize model
        """
        LTVDifferentialDrive.__init__(self, dt, states)

    # pragma pylint: disable=signature-differs
    def update_controller(self, next_r):
        self.design_controller_observer()

        u = self.K @ (self.r - self.x_hat)
        rdot = (next_r - self.r) / self.dt
        uff = self.Kff @ (rdot - self.f(self.x_hat, np.zeros(self.u.shape)))
        self.r = next_r
        self.u = u + uff

        u_cap = np.max(np.abs(self.u))
        if u_cap > 12.0:
            self.u = self.u / u_cap * 12.0


def main():
    """Entry point."""
    ts = []
    refs = []

    # Radius of robot in meters
    rb = 0.59055 / 2.0

    with open("ramsete_traj.csv", "r", encoding="utf-8") as trajectory_file:
        reader = csv.reader(trajectory_file, delimiter=",")
        trajectory_file.readline()
        for row in reader:
            ts.append(float(row[0]))
            x = float(row[1])
            y = float(row[2])
            theta = float(row[3])
            vl, vr = get_diff_vels(float(row[4]), float(row[5]), rb * 2.0)
            ref = np.array([[x], [y], [theta], [vl], [vr]])
            refs.append(ref)

    dt = 0.02
    x = np.array([[refs[0][0, 0] + 0.5], [refs[0][1, 0] + 0.5], [np.pi / 2], [0], [0]])
    diff_drive = DifferentialDrive(dt, x)

    state_rec, ref_rec, u_rec, y_rec = diff_drive.generate_time_responses(refs)

    plt.figure(1)
    x_rec = np.squeeze(state_rec[0:1, :])
    y_rec = np.squeeze(state_rec[1:2, :])
    plt.plot(x_rec, y_rec, label="LTV controller")
    plt.plot(ref_rec[0, :], ref_rec[1, :], label="Reference trajectory")
    plt.xlabel("x (m)")
    plt.ylabel("y (m)")
    plt.legend()

    plt.gca().set_aspect(1.0)
    plt.gca().set_box_aspect(1.0)

    if "--noninteractive" in sys.argv:
        latex.savefig("ltv_diff_drive_nonrotated_xy")

    diff_drive.plot_time_responses(ts, state_rec, ref_rec, u_rec)

    if "--noninteractive" in sys.argv:
        latex.savefig("ltv_diff_drive_nonrotated_response")
    else:
        plt.show()


if __name__ == "__main__":
    main()