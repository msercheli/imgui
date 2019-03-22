# -*- coding: utf-8 -*-

name = 'imgui'

version = '1.70'

description = \
    """
    Bloat-free Immediate Mode Graphical User interface for C++ with minimal dependencies
    """
authors = ['Omar Ocurnut']

def commands():
    #env.PYTHONPATH.append("{root}/python")
    #env.PATH.append("{root}/bin/{system.platform}")
    env.REZ_IMGUI_INCLUDE_PATH = "{root}/include"

uuid = 'repository.imgui'

