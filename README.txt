# MapReduce Student Grades Analysis

## Overview
This project uses **MapReduce** with Python's `mrjob` to analyze student grade data. It processes a dataset (`coursegrades.txt`) containing student grades and calculates:
1. **Task 1:** Average grade per course.
2. **Task 2:** Average grade per university.
3. **Task 3:** Top 3 highest grades per year.

## Prerequisites
Before running the scripts, you need to:
- Install Python (>=3.7)
- Set up a virtual environment
- Install the required dependencies

## Setup Guide
Follow these steps to set up and run the project:

### 2️⃣ **Create and Activate Virtual Environment**
#### **On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```
#### **On Windows (CMD or PowerShell):**
```powershell
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ **Install Required Libraries**
#### **For macOS/Linux Users:**
Run the installation script:
```bash
bash setup_env.sh
```
OR, manually install:
```bash
pip install -r requirements.txt
```

#### **For Windows Users:**
Run the installation script:
```powershell
setup_env.bat
```
OR, manually install:
```powershell
pip install -r requirements.txt
```

## Running the MapReduce Scripts
After setting up the environment, run the scripts as follows:

### **Task 1: Compute the Average Grade Per Course**
```bash
python Task1.py coursegrades.txt > output_task1.txt
```

### **Task 2: Compute the Average Grade Per University**
```bash
python Task2.py coursegrades.txt > output_task2.txt
```

### **Task 3: Identify the Top 3 Highest Grades Per Year**
```bash
python Task3.py coursegrades.txt > output_task3.txt
```

## Expected Output Files
| Task | Output File |
|------|------------|
| Task 1 | `output_task1.txt` |
| Task 2 | `output_task2.txt` |
| Task 3 | `output_task3.txt` |

## Deactivating Virtual Environment
After running the scripts, deactivate the virtual environment:
```bash
deactivate
```

## Notes
- Ensure `coursegrades.txt` is present in the same directory before running the scripts.
- Run the scripts from the **same directory** where `coursegrades.txt` is located.
- If an error occurs, ensure the **virtual environment is activated** and dependencies are installed.