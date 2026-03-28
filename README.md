# SynthGrasp

## The Problem
Training robot manipulation policies requires thousands of teleoperation demonstrations — a human physically guiding a robot arm through every grasp, on every object, in every environment. This is expensive three ways: collection requires physical robots and operators, demonstration data (multi-camera video + sensor streams) scales to petabytes quickly, and data collected in one environment generalizes poorly to others.

## What SynthGrasp Does
SynthGrasp generates manipulation training data synthetically from a single screenshot in under a minute.
Given an image, SynthGrasp:

Detects and identifies all objects in the scene
Reconstructs the environment and loads it into a physics simulation
Generates grasp trajectories and evaluates liftability programmatically
Flags low-confidence outputs for review, prioritizing label accuracy

The result: training data without a robot farm, without operator time, and with built-in diversity through scene randomization.