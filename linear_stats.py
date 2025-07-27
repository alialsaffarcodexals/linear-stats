#!/usr/bin/env python3
"""
linear_stats.py
================

This script reads a plain‑text data file containing one numeric value per line and
computes two statistics about the resulting sequence:

* **Linear regression line** – the best‑fit line ``y = mx + b`` that minimises
  squared error between the data points ``(x_i, y_i)`` and the fitted line, where
  ``x_i`` is simply the zero‑based index of each value in the input file and
  ``y_i`` is the numeric value on that line.
* **Pearson correlation coefficient** – a normalised measure of the strength
  and direction of the linear relationship between ``x`` and ``y``.

Both statistics are printed to stdout in the exact format required by the
``linear‑stats`` project specification. Values in the linear regression line
have six decimal places, while the Pearson correlation coefficient is printed
with ten decimal places.

Usage::

    python3 linear_stats.py path/to/data.txt

The script expects a single argument: the path to the data file. If the
argument is missing or the file cannot be read, the script prints an error
message and exits with a non‑zero status code.

This program does not depend on any third‑party libraries; it relies solely on
Python’s standard library. It is therefore portable across environments where
Python 3 is available.
"""

import math
import sys
from typing import List, Tuple


def parse_file(path: str) -> List[float]:
    """Read a file containing one numeric value per line.

    Args:
        path: Path to the input file.

    Returns:
        A list of floating‑point numbers.

    Raises:
        ValueError: If any line cannot be parsed as a float.
        IOError: If the file cannot be opened.
    """
    values: List[float] = []
    with open(path, "r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            stripped = line.strip()
            if not stripped:
                # Skip empty lines gracefully
                continue
            try:
                values.append(float(stripped))
            except ValueError as err:
                raise ValueError(f"Unable to parse line {line_no}: '{stripped}'") from err
    return values


def linear_regression(x: List[float], y: List[float]) -> Tuple[float, float]:
    """Compute the slope and intercept of the linear regression line.

    Using the standard formulae for simple linear regression,
    ``m = (n Σxy − Σx Σy) / (n Σx² − (Σx)²)`` and
    ``b = (Σy − m Σx) / n``.

    Args:
        x: Independent variable values.
        y: Dependent variable values.

    Returns:
        A tuple ``(m, b)`` where ``m`` is the slope and ``b`` is the intercept.

    Raises:
        ValueError: If the computation involves division by zero (e.g. constant
        x values).
    """
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(x_i * y_i for x_i, y_i in zip(x, y))
    sum_x2 = sum(x_i ** 2 for x_i in x)
    denominator = n * sum_x2 - sum_x ** 2
    if denominator == 0:
        raise ValueError("Cannot compute linear regression: denominator is zero")
    m = (n * sum_xy - sum_x * sum_y) / denominator
    b = (sum_y - m * sum_x) / n
    return m, b


def pearson_correlation(x: List[float], y: List[float]) -> float:
    """Compute the Pearson correlation coefficient between two sequences.

    The coefficient is given by::

        r = (n Σxy − Σx Σy) / sqrt[(n Σx² − (Σx)²)(n Σy² − (Σy)²)]

    Args:
        x: First sequence of values.
        y: Second sequence of values.

    Returns:
        The Pearson correlation coefficient (float).

    Raises:
        ValueError: If the denominator evaluates to zero (e.g. constant x or y).
    """
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(x_i * y_i for x_i, y_i in zip(x, y))
    sum_x2 = sum(x_i ** 2 for x_i in x)
    sum_y2 = sum(y_i ** 2 for y_i in y)
    numerator = n * sum_xy - sum_x * sum_y
    denominator = math.sqrt((n * sum_x2 - sum_x ** 2) * (n * sum_y2 - sum_y ** 2))
    if denominator == 0:
        raise ValueError("Cannot compute Pearson correlation: denominator is zero")
    return numerator / denominator


def main(argv: List[str]) -> int:
    if len(argv) != 2:
        print(f"Usage: {argv[0]} <data_file>", file=sys.stderr)
        return 1
    data_file = argv[1]
    try:
        y_values = parse_file(data_file)
    except Exception as e:
        print(f"Error reading file: {e}", file=sys.stderr)
        return 1
    if not y_values:
        print("Error: No data found in file", file=sys.stderr)
        return 1
    # Create x values as zero‑based indices
    x_values = list(range(len(y_values)))
    try:
        m, b = linear_regression(x_values, y_values)
        r = pearson_correlation(x_values, y_values)
    except ValueError as e:
        print(f"Error computing statistics: {e}", file=sys.stderr)
        return 1
    print(f"Linear Regression Line: y = {m:.6f}x + {b:.6f}")
    print(f"Pearson Correlation Coefficient: {r:.10f}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))    
