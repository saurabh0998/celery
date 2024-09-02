# Celery Assignment: Auto MPG Data Analysis

This project demonstrates the use of Celery for parallel processing tasks in Python. The goal is to calculate the power-to-weight ratio for each car in the Auto MPG dataset using Celery to handle parallel processing.

## Table of Contents

- [Celery Assignment: Auto MPG Data Analysis](#celery-assignment-auto-mpg-data-analysis)
  - [Table of Contents](#table-of-contents)
  - [Project Overview](#project-overview)
  - [Setup and Installation](#setup-and-installation)
    - [1. Prerequisites](#1-prerequisites)
    - [2. Clone the Repository](#2-clone-the-repository)
    - [3. Create and Activate Virtual Environment](#3-create-and-activate-virtual-environment)
    - [4. Install Required Packages](#4-install-required-packages)
    - [5. Start Redis Server](#5-start-redis-server)
    - [6. Configure Celery](#6-configure-celery)
  - [Usage](#usage)
    - [1. Start Celery Worker](#1-start-celery-worker)
    - [2. Run Data Processing Script](#2-run-data-processing-script)
  - [Project Structure](#project-structure)
  - [Thought Process](#thought-process)
  - [Result](#result)

## Project Overview

- **Objective**: Calculate the power-to-weight ratio for each car in the Auto MPG dataset using Celery for parallel processing.
- **Dataset**: Auto MPG dataset from the UCI Machine Learning Repository.

## Setup and Installation

### 1. Prerequisites

- Python 3.x
- Redis server
- Virtual environment

### 2. Clone the Repository

Clone the repository to your local machine using:

```bash
git clone https://github.com/saurabh0998/celery
cd celery-assignment
```

### 3. Create and Activate Virtual Environment

Create a virtual environment to isolate project dependencies:

```
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Required Packages

Install the required Python packages listed in requirements.txt:

```
pip install -r requirements.txt
```

### 5. Start Redis Server

Make sure you have Redis installed and running locally. You can start it using:

```
redis-server
```

### 6. Configure Celery

Update the broker URL if needed:

```
# Example Celery configuration in tasks.py
from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')
```

## Usage

### 1. Start Celery Worker

Open a terminal, navigate to the project directory, and start the Celery worker:

```
celery -A tasks worker --loglevel=info
```

### 2. Run Data Processing Script

In another terminal, run the data processing script to load the data, perform calculations, and output results:

```
python scripts/process_data.py
```
This script will load the Auto MPG dataset, use Celery to calculate the power-to-weight ratio in parallel, and update the dataset with these results.

## Project Structure
The project's file structure is organized as follows:

```
celery-assignment/
│
├── data/
│   └── auto-mpg.data            # Auto MPG dataset
│
├── scripts/
│   ├── __init__.py              # Init file for Python package
│   ├── process_data.py          # Script call Celery tasks
│    ├── load_data.py             # Script to load data and call Celery tasks
│
├── venv/                        # Virtual environment directory
│
├── tasks.py                     # Celery tasks for processing
│
├── requirements.txt             # Python package dependencies
├── README.md                    # Project documentation
└── .gitignore                   # Git ignore file
```

## Thought Process

1. **Environment Setup**: Create a virtual environment and install necessary packages to ensure dependencies are isolated and managed.
2. **Data Loading**: Use pandas to load the Auto MPG dataset. Preprocess the data to ensure it's in the correct format for analysis.
3. **Task Distribution**: Use Celery to distribute the computation of the power-to-weight ratio across multiple workers. This allows for parallel processing, reducing the time required for the calculations.
4. **Result Collection**: Collect the results of the calculations using Celery’s AsyncResult feature and update the dataset.

## Result

Once the script `scripts/process_data.py` runs, you can see the results in `data/processed_data.csv`.