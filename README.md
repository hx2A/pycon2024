# PyCon 2024 Presentation Materials

This repo contains the presentation materials for the PyCon 2024 talk "Creative Coding with py5, the Python version of Processing," delivered on May 18, 2024.

You'll need to install py5 to run the example code.

Your best bet is to follow the [Install py5](https://py5coding.org/content/install.html) documentation on the [py5coding.org](https://py5coding.org) website, as that documentation provides the most complete setup instructions.

Several of the notebooks use the py5 or py5bot Jupyter Notebook kernels. The [Install py5](https://py5coding.org/content/install.html) documentation will tell you how to install that. One of the notebooks uses opencv, which you can install with `pip install opencv-python`.

## Attention, MacOS Users!

**As of the day of the PyCon presentation there is an open bug in ipykernel affecting other libraries running on MacOS computers with M1, M2, and M3 CPUs.** This bug affects matplotlib and py5, among others. You can read the [py5 dicussion of the problem here](https://github.com/py5coding/py5generator/issues/456). The issue is [ipython/ipykernel#1124](https://github.com/ipython/ipykernel/issues/1124) and there is an open PR to fix it. Users with MacOS computers may want to export the notebooks to `*.py` files. When doing so, please remove the `%gui osx` code before executing.

Note that getting py5 to run well on MacOS has been a major development challenge. Please read [Special Notes for macOS Users](https://py5coding.org/content/macos_users.html) for more information. Discussion or PRs for how to improve py5 for MacOS users is most welcome!
