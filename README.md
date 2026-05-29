Student Burnout Risk

A Python-based tool that asses the risk of academic burnout through the use of a structured survey. 
The calculator combines multiple question classes, each with specific scoring behavior to produce a meaningful score.

Motivation

I started this project because burnout is something I have personally struggled with.
I want to build something that is actually useful to me and other students who have struggled with the same issue.
It uses real, research-backed questions and logic to give the most accurate and meaningful assessment as possible.

Current Status

It is in active development. Not fully functional yet.
The questions.py module is complete, and the scoring.py and main.py modules are in progress.

Module Overview

- questions.py: Defines all three question classes and stores the full bank of questions for each. 3 question types - Numeric, Likert, Reverse-Likert
- scoring.py: Handles user input collection and scoring logic (IN PORGRESS)
- main.py: Orchestrates the entire program and displays results to the user (IN PROGRESS)

Planned Features

- Research backed scoring thresholds for all numeric questions
- Likert questions grounded in academic research about student burnout
- Final burnout risk will be a total percentage and also provide a meaningful label with insight
- Streamlit interface for a clean user experience (this will take place once the entire program is complete and tested with a few small samples)
- CSV based data logging (this will allow the project to become a useful research tool later on)

Research Basis

Most of the questions are based on my own research I have done with this project.
Currently there are some placeholder questions and logic while more research is done.
Sources will be included in any final interations.
