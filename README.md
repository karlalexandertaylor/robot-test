============
============
Robot-Test
============
============

The purpose of this application is to build a small robot application which calculates the distance from the start point and whether the robot has moved in a circle.

============
Getting Started
============

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

=============
Prerequisites
=============

The applications are written in python.

They were executed and tested against python 3.8.

A copy of python should be sufficient to run the application.  However other supporting tools you might consider:

    - Autopep8 for formatting
    - Sphinx for documentation

===========
Application
===========

This application has two code files:

    - oprog1.py (calculates distance robot travelled)
    - oprog2.py (calculates if robot went in a circle)
    
The structure to run the run the program is:

    python oprog1.py ./tests/test1.dir

or

    python oprog2.py ./tests/test1.dir

if you want to run the program in debug mode use this run command:

    python oprog1.py ./tests/test1.dir 1

or

    python oprog2.py ./tests/test1.dir 1

========================
Structure of input files
========================

The program looks for one of three values on a single line 

    F (move forward one space)
    R (rotate right)
    L (rotate left)

Example

R
F
L
F

The program will ignore the line if it does not comply with the rules above

==========
Test Files
==========

There are a number of test files to use with the programs and these exist in the tests directory

=================
Structure of Code
=================

.. image:: https://www.yworks.com/yed-live/?file=https://gist.githubusercontent.com/karlalexandertaylor/d2b83950471a8ca20375eccaf8399976/raw/oprog1

=======
Authors
=======

Karl Taylor
See also the list of contributors who participated in this project.

=======
License
=======

This project is licensed under the GNU License - see the LICENSE.md file for details

