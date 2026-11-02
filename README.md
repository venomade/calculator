# Calculator
A simple calculator application for the Terminal, built step by step in SCCM4910.
It will run on `Python 3` via the `calculator.py` script.

## What It Will Do
Add, subtract, multiply and divide two numbers; display the result.

## How to Run It
Run: `./run.sh`

## Usage
- First enter a number
- Then enter an operator (`+`,`-`,`*` or `/`)
- Lastly enter a second number
- Read the result, printed as `Result: ` followed by the answer.
- When done stop with `Ctrl+c`

## Testing
- Enter a `venv` and install `pytest`:
```sh
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements-dev.txt
python3 -m pytest --version
```
- Run: `./test.sh`
- All tests should return `PASSED` and the return code of `test.sh` should be `1`.

