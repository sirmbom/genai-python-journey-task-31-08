"""Linear script with conditional tasks.

There are seven tasks: first six are single-line replacements and the final
block (1-3 lines) implements grading and leap-year checks.
"""

# Threshold constants (six single-line TODOs below)
# TODO: set thresholds and sample values
A = 90  # TODO: set to 90
B = 80  # TODO: set to 80
C = 70  # TODO: set to 70
D = 60  # TODO: set to 60
score = 72  # TODO: set a sample score, e.g. 72
year = 2026  # TODO: set a sample year, e.g. 2024

# : A: 100-90, B: 89-80, C: 79-70, D: 69-60,

if score >= A:
    letter = 'A'
elif score >= B:
    letter = 'B'
elif score >= C:
    letter = 'C'
elif score >= D:
    letter = 'D'
else:
    letter = 'E'

# Final block (1-3 lines): compute grade with a single expression,
# compute leap-year boolean, and print results. Replace the placeholders.
# TODO: complete the block below (max 3 lines)
if year%4 == 0 and year%100 != 0:
    leap_condition = True
elif year%400 == 0 and year%100 == 0:
    leap_condition = True
else:
    leap_condition = False

grade = letter  # TODO: set to a chained conditional expression mapping score->grade
is_leap = leap_condition  # TODO: set to leap-year boolean expression
print(f"score={score} -> grade={grade}; year={year} leap={is_leap}")
