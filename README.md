# AI Optimized Polarization

A machine-learning and reinforcement-learning project for automatically controlling a complex experimental system.

## Overview

This project investigates whether a reinforcement-learning agent can automatically adjust experimental controls to maintain a photon beam at a desired energy.

The system is challenging because small changes in the experimental controls can affect the resulting photon-beam energy in nonlinear and coupled ways. The goal is to maintain the beam energy within **1% of its target value**.

## Machine Learning Approach

The project combines:

* **Simulation modeling** of the experimental system
* **Reinforcement learning** for automated control
* **Time-series and system-dynamics analysis**
* **Optimization of experimental control parameters**
* **Validation against experimental behavior**

A simulation environment is used to model how changes in the electron-beam and experimental control parameters affect the resulting photon beam. This provides a controlled environment in which reinforcement-learning approaches can be developed and evaluated before being applied to the physical system.

## Technical Problem

The photon beam is produced when an electron beam interacts with a diamond target mounted on a goniometer. The goniometer allows millidegree-scale adjustments to the target's pitch, roll, and yaw.

The ML challenge is to learn how these control parameters affect the resulting beam energy and determine adjustments that keep the system near its desired operating point.

## Goal

Maintain photon-beam energy within **1% of the desired target** while minimizing unnecessary control adjustments.

## Skills Demonstrated

* Python
* Machine learning
* Reinforcement learning
* Simulation
* Numerical modeling
* Optimization
* Experimental data analysis
* Control systems
* Model validation

## Project Status

This repository contains the development work for the AI Optimized Polarization project. The project represents approximately 4.5 months of development work.
