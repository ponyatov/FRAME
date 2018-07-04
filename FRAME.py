## @file
## @brief Minsky FRAME system implementation in Python

import os, sys, pickle

## @defgroup world The WORLD where all objects lives
## @{

## image file name is this .py file + ``.image'`
IMAGEFILE = sys.argv[0] + '.image'

try:
    ## The WORLD where all objects lives
    WORLD = pickle.load(open(IMAGEFILE))
except IOError:
    WORLD = []

## @}
