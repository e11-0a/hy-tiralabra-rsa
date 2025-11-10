#!/bin/bash
coverage run tests.py
coverage html
xdg-open htmlcov/index.html