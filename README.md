## WORK

### Git tasks

- Create your personal fork of [this repo](https://github.com/sirmbom/genai-python-journey-task-31-08)
- Clone your fork to your local machine
- Create a new branch and switch to it. Make all changes on your feature branch.

### Environment Tasks

- Initialize a Python project and create a virtual environment (recommended: `python -m venv .venv`).
- Create a `.env` file in the repository root (see `.env.example`).
- Install the `python-dotenv` dependency.

### Test Tasks

This assignment keeps most work for students. 

### Test Tasks (practice)

Complete a set of test tasks and then use that knowledge to complete the main task. All test tasks live in `test_tasks/`:

- `test_tasks/test_strings.py` — string methods and simple inspections
- `test_tasks/test_functions.py` — small functions and simple computations
- `test_tasks/test_conditions.py` — thresholds, grade mapping, and leap-year check
- `test_tasks/test_loops.py` — loops including nested loops

Each test script is a short linear script. Students should open a file, find the comments labeled `# TODO: fill this line` and one final small block (one to three lines) to complete.

Run each script from the repository root, for example:

```
python -m test_tasks.test_strings
```

### Main task (password analyzer)

Create a `main_task.py` and an environment variable named `PASSWORD` and give it your value (create your own `.env` file). Evaluates the password strength. The script should print a short summary of checks and a final strength rating.

You would score and check the PASSWORD as follows:

- +1 point: length >= 8
- +1 point: contains uppercase
- +1 point: contains lowercase
- +1 point: contains digit
- +1 point: contains special character
- Rating: 0-2 -> Weak, 3-4 -> Moderate, 5 -> Strong

**TIPS**:

- Basic string operations: trimming, length (`len()`), case conversion (`.lower()`, `.upper()`), character checks (`.isalpha()`, `.isdigit()`, `.islower()`, `.isupper()`).
- Character classification: test for presence of at least one uppercase, lowercase, digit, and special character (choose a set like `!@#$%^&*`).
- Loops and counting: iterate characters to count categories (use `for` loop, optionally `any()` or generator expressions).
- Conditionals: map checks/score to a human-friendly rating (e.g., Weak / Moderate / Strong) using `if`/`elif`/`else`.
- Output: print a concise summary (which checks passed, computed score, and rating).



