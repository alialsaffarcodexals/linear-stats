# Linear Stats

This repository contains a simple program that performs two statistical
calculations on a sequence of numbers read from a text file:

1. **Linear regression line** – the best‑fit line of the form `y = mx + b` that
   minimises the squared error between the indices of the data and the values.
2. **Pearson correlation coefficient** – a measure of how strongly and in what
   direction the input sequence correlates with its indices.

## How it works

The program uses the zero‑based index of each value as the independent
variable (x) and the value itself as the dependent variable (y). It reads one
floating‑point number per line from a file and computes both the slope (`m`)
and intercept (`b`) of the linear regression line using closed‑form formulae.
The Pearson correlation coefficient is calculated using the standard
definition and printed with ten decimal places, as specified in the
project instructions【384274288764166†L34-L45】.

## Usage

```
python3 linear_stats.py path/to/data.txt
```

The script will output two lines:

```
Linear Regression Line: y = <slope>x + <intercept>
Pearson Correlation Coefficient: <correlation>
```

The slope and intercept are formatted to six decimal places, and the
Pearson correlation coefficient is printed with ten decimal places, as
required by the specification【384274288764166†L34-L45】.

If the input file cannot be read or contains no valid numbers, the program
will print an error message to `stderr`.

## Testing with the auditor script

The official project audit suggests downloading the provided binary
package from
[`stat-bin-dockerized.zip`](https://assets.01-edu.org/stats-projects/stat-bin-dockerized.zip)
and running the auditor’s script to generate random data sets and
compare results【119916386454298†L0-L19】. After downloading and extracting
the archive, make the scripts executable (e.g. `chmod +x ./bin/*`) and run

```
./bin/linear-stats
```

This will produce a `data.txt` file alongside the binary. You can then run

```
python3 linear_stats.py data.txt
```

and compare the output of this program with that of the auditor’s to
ensure correctness.

## License

This project is distributed under the terms of the MIT license. See
[`LICENSE`](LICENSE) for details.
