#!/bin/bash
VALUES=($(bash -c "python3 ./sememestre_V/class_display.py"))
echo ${VALUES[0]}
