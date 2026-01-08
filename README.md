# siemens-vplc-warehouse-cell

## Project Overview

## This project simulates a Siemens-style virtual PLC (VPLC) for warehouse automation using Python. It models conveyor cells, sensors, motor control logic, timers, and fault detection, along with a mock PLC DB to emulate Siemens memory. The simulation is modular and scalable, demonstrating core automation engineering skills suitable for portfolio or GitHub showcase.

**Key features:**
##
Multi-cell conveyor line simulation (2–4 cells, extendable)

PLC cyclic scan loop emulation

Timer (TON) and latch (SR) logic for motor control

Jam detection and fault signaling

Mock Siemens DB transport and IO mapping

Modular Python structure for easy expansion
##
git clone https://github.com/<your_username>/siemens-vplc-warehouse-cell.git
cd siemens-vplc-warehouse-cell

##
python -m venv .venv
.\.venv\Scripts\Activate.ps1

## Expected Output:
Cell1 MOTOR=True FAULT=False CODE=0
Cell2 MOTOR=True FAULT=False CODE=0
...
## The output updates each scan cycle, showing motor states and fault codes for each conveyor cell.

src/
├── main.py           # Entry point for VPLC simulation
├── vplc/
│   ├── __init__.py
│   ├── fb.py         # PLC function blocks (TON, SR)
│   └── scan.py       # VPLC scan loop
├── logic/
│   ├── __init__.py
│   └── cell.py       # Conveyor cell logic
├── comm/
│   ├── __init__.py
│   ├── plc_transport.py  # Mock PLC transport layer
│   └── s7_dbmap.py       # DB bit/word mapping
├── plant/
│   └── __init__.py
.venv/                 # Python virtual environment
README.md              # Project documentation

