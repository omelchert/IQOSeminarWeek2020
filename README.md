# IQOSeminarWeek2020 

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

The scripts provided in this repository accompany the scientific short cours

``A brief guide to publication-ready scientific figures using Python’s matplotlib''

held during the 2020 seminar week of the Ultrafast Laser Laboratory at
Institute of Quantum Optics at Leibniz University Hannover.

The short course aimed at reproducing the two figures contained in the research article

    Interaction of "Solitons" in a Collisionless Plasma and the Recurrence of Initial States,
    N. J. Zabusky and M. D. Kruskal,
    Phys. Rev. Lett. 15, 240 (1965)


[DOI: https://doi.org/10.1103/PhysRevLett.15.240](https://doi.org/10.1103/PhysRevLett.15.240) pointing out various rules and best practices.

## Results of the reproduction task

The results of the reproduction task, i.e. two figures accompanied by suitable captions, are shown below.

![](https://github.com/omelchert/IQOSeminarWeek2020/blob/master/fig01.png)
*Fig. 1: Temporal development of the real-vauled field u(x,t) at times t=0 (short
dashed line; labeled A), t=tB (dashed line; labeled B), and t=3.6 tB (solid
line; labeled C).  Numbers 1 through 8 enumerate the solitons exhibited by
u(x,t=3.6 tB) in order of decreasing amplitude. Dash-dotted lines are included
to demonstrate the linear variation of their amplitudes.*

![](https://github.com/omelchert/IQOSeminarWeek2020/blob/master/fig02.png)
*Fig. 2: (a) Evolution of the real-valued field u(x,t) in the range t/TR =
0.1-0.6.  Numbers 1 through 9 enumerate the solitons featured for t/TR>0.1 in
order of decreasing amplitude.  White dots trace the amplitude peak of soliton
no. 1. In the vincinity of multiple similar amplitude solitons crossing, the
tracing procedure is notoriously inaccurate (see dashed circles).  (b) Temporal
variation of the peak amplitude AS1(t) of soliton no. 1.*

## Prerequisites

To work as intended, the provided scripts are expected to be run via Python3 in
conjunction with

* numpy
* scipy
* matplotlib

## Included materials

The repository contains:

```
./IQOSeminarWeek2020/
├── LICENSE.md
├── README.md
├── KdV_raw_data.npz
├── fig01.png
├── fig02.png
├── main_KdV_generate_data.py
├── pp_figure_01.py
└── pp_figure_02.py
```

* `LICENSE`, a license file
* `Readme.md`, this file
* `KdV_raw_data.npz`, raw data file using numpys custom npz format
* `fig01.png`, reproduction of Fig. 1 of [this reference](https://doi.org/10.1103/PhysRevLett.15.240)
* `fig02.png`, reproduction of Fig. 2 of [this reference](https://doi.org/10.1103/PhysRevLett.15.240)
* `main_KdV_generate_data.py`, python script that reproduces the raw data on which the conclusions of [this reference](https://doi.org/10.1103/PhysRevLett.15.240) was based
* `pp_figure_01.py`, python module providing functions to reproduce Fig. 1 of [this reference](https://doi.org/10.1103/PhysRevLett.15.240)
* `pp_figure_02.py`, python module providing functions to reproduce Fig. 1 of [this reference](https://doi.org/10.1103/PhysRevLett.15.240)


## Availability of the software

You can obtain a local [clone](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository) of this repository, e.g. via

``$ git clone https://github.com/omelchert/IQOSeminarWeek2020``

## License

The provided scripts are licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

This work received funding from the Deutsche Forschungsgemeinschaft  (DFG)
under Germany’s Excellence Strategy within the Cluster of Excellence PhoenixD
(Photonics, Optics, and Engineering – Innovation Across Disciplines) (EXC 2122,
projectID 390833453).
