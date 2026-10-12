# AGV Project Collection

**Autonomous Navigation | Pathfinding | Robotics | Reinforcement Learning**

A collection of Python projects focused on learning and implementing the fundamental concepts behind Automated Guided Vehicles (AGVs), Autonomous Mobile Robots (AMRs), and autonomous navigation systems.

The project follows a progressive, challenge-based development approach. Each stage introduces a new problem, building upon previously implemented algorithms and systems.

The long-term goal is to progress from basic 2D pathfinding to multi-agent coordination, intelligent decision-making, and eventually 3D robotics simulation.

**Current Status:** Level 1 implemented | Level 2 in development

---

## Project Objectives

The primary goal is to gain practical experience in autonomous navigation, simulation, and robotics software development.

Rather than relying entirely on existing pathfinding libraries, the core algorithms and decision-making logic are implemented from scratch.

The projects explore:

- Graph search and pathfinding algorithms
- Autonomous navigation in partially observable environments
- Persistent mapping and environment exploration
- Dynamic obstacle avoidance and path replanning
- Task allocation and route optimization
- Multi-agent pathfinding and fleet coordination
- Reinforcement Learning for autonomous decision-making
- Robotics simulation and sensor processing

## Project Structure

**First_robot/** — Level 1: Basic Pathfinding

The first project introduces fundamental autonomous navigation using a fully observable 2D grid environment.

**Second_robot/** — Level 2: Mapping and Limited Visibility

The second project introduces limited sensor visibility, persistent internal mapping, and navigation through partially explored environments.

**README.md** — Project documentation, development progress, and roadmap.

---

## Level 1 — BFS Pathfinder

**Status: Implemented**

The first challenge focuses on navigating a single robot through a static environment using Breadth-First Search (BFS).

The robot has access to the complete observable environment and must independently calculate a route from its starting position to a target.

### Implemented features

- Node-based search tree
- Breadth-First Search (BFS)
- Obstacle and boundary validation
- Visited-state tracking
- Parent-based path reconstruction
- Conversion of paths into movement actions
- Integration with the POGEMA simulation environment

### Learning outcomes

This stage introduces graph traversal, search trees, queues, coordinate systems, and fundamental pathfinding concepts.

BFS also provides a baseline for comparing more advanced navigation algorithms in later stages.

## Level 2 — Persistent Mapping and Exploration

**Status: In Development**

The second challenge removes access to the complete map.

Instead, the robot receives a limited 11×11 local observation and must gradually construct its own internal representation of the environment.

The factory layout remains static while the robot receives multiple navigation targets.

### Implemented / current development

- Local observation processing
- Dynamically expanding 2D NumPy map
- Internal coordinate system and offset management
- Tracking of previously visited robot positions
- Matplotlib visualization of the internal map

### Planned features

- Updating previously unknown cells using new observations
- Persistent environmental knowledge across tasks
- Goal-directed exploration of unknown areas
- Selection of reachable exploration frontiers
- Path planning using previously discovered areas
- Reusing the internal map for subsequent navigation tasks

### Mapping representation

The internal map distinguishes between:

- **-1:** Unknown environment
- **0:** Free space
- **1:** Obstacle

Robot position is additionally highlighted during visualization.

The goal is to make the robot progressively more knowledgeable about its environment rather than starting from scratch for every navigation task.

---

## Development Roadmap

| Level | Topic | Status |
|---|---|---|
| 1 | BFS Pathfinding | Implemented |
| 2 | Persistent Mapping and Limited Visibility | In progress |
| 3 | A* Pathfinding and Heuristics | Planned |
| 4 | Dijkstra and Weighted Path Planning | Planned |
| 5 | Dynamic Obstacles and Replanning | Planned |
| 6 | Pickup and Delivery Tasks | Planned |
| 7 | Multiple Orders and Task Selection | Planned |
| 8 | Task Scheduling and Route Optimization | Planned |
| 9–12 | Multi-Agent Navigation and Traffic Management | Planned |
| 13–14 | Fleet Optimization and Battery Management | Planned |
| 15 | Reinforcement Learning | Planned |
| 16 | Performance Benchmarking | Planned |
| 17–18 | Continuous Movement and Sensor Processing | Planned |
| 19–20 | ROS 2, Webots and 3D Autonomous Warehouse | Planned |

Each level is designed to introduce new concepts without requiring a complete redevelopment of previous algorithms.

## Technologies

- **Python** — Core programming language
- **NumPy** — Grid representations and numerical operations
- **Pandas** — Structured environment data
- **Matplotlib** — Map visualization and debugging
- **POGEMA** — 2D navigation and multi-agent simulation
- **Gymnasium-compatible environments** — Agent-environment interaction

### Future Technologies

- C++ for robotics-oriented software development
- PyTorch and Stable-Baselines3 for Reinforcement Learning
- ROS 2 for robotics software integration
- Webots for 3D robotics simulation
- Nav2 for autonomous navigation

## Getting Started

Install the main Python dependencies:

`pip install pogema numpy pandas matplotlib`

To run the Level 1 experiment from the repository root:

`python First_robot/main.py`

The Level 2 project is currently under active development.

Additional setup instructions and dependency management will be added as the repository evolves.

---

## Evaluation and Benchmarking

Future versions will introduce standardized testing and performance evaluation.

Planned metrics include:

- Navigation success rate
- Path length and path efficiency
- Nodes explored during pathfinding
- Planning and execution time
- Collision count
- Task completion rate
- Environment coverage
- Multi-agent throughput

The intention is to compare different planning and decision-making approaches under consistent simulation conditions.

## Long-Term Vision

The ultimate objective is to develop a simulated autonomous warehouse system where multiple robots can independently navigate, accept transportation orders, coordinate movements, avoid conflicts, and optimize operational efficiency.

The project will gradually transition from grid-based navigation toward more realistic robotics systems involving continuous movement, sensor data, localization, mapping, and autonomous control.

## Author

**Elias Stålhjärta**

Data Scientist Student — EC Utbildning, Gothenburg, Sweden

Interested in Artificial Intelligence, Reinforcement Learning, Industrial Automation, Robotics, and Autonomous Systems.

This repository is a personal learning and portfolio project, developed to explore the intersection of AI, software engineering, and industrial robotics.
