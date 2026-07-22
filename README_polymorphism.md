# Smart Traffic Management System

## About
This project was created as a case study activity for EL 162 — Object Oriented Programming at the University of Mines and Technology (UMaT), Tarkwa. It demonstrates polymorphism in Python through a smart traffic management system.

## Task Summary
A smart city uses intelligent traffic devices. Every device receives the same command activate() but each device performs a different task depending on its type.

## What the Code Does
- Creates a parent class TrafficDevice with an activate() method
- Creates child classes TrafficLight, SpeedCamera and PedestrianSignal that each override activate() differently
- Adds an EmergencySiren class without modifying the activation loop
- Stores all objects in a list and activates them without checking their types

## Concept Demonstrated
Polymorphism — same method name, different behaviour depending on the object

## How to Run
1. Open polymorphism_traffic_system.py in PyCharm
2. Run with Shift + F10
3. Each device will activate and print its unique response

## Author
Akyaa
EL 162 — Python and OOP
University of Mines and Technology (UMaT), Tarkwa
