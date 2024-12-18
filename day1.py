import marimo

__generated_with = "0.10.4"
app = marimo.App(width="medium", auto_download=["html"])


@app.cell
def _():
    import marimo as mo
    from pathlib import Path
    import numpy as np
    return Path, mo, np


@app.cell
def _(mo):
    mo.md("""# Part 1""")
    return


@app.cell
def _(Path, np):
    raw_input = Path("inputs/input01a.txt").read_text()

    input1: list[int] = []
    input2: list[int] = []

    for row in raw_input.splitlines():
        a, b = row.split()
        input1.append(int(a))
        input2.append(int(b))

    input1_np = np.array(input1)
    input2_np = np.array(input2)
    return a, b, input1, input1_np, input2, input2_np, raw_input, row


@app.cell
def _(input1_np, input2_np):
    input1_np[:10], input2_np[:10]
    return


@app.cell
def _(input1_np, input2_np):
    input1_np.sort()
    input2_np.sort()
    return


@app.cell
def _(mo):
    mo.md(r"""## Part 1 answer""")
    return


@app.cell
def _(input1_np, input2_np):
    sum(abs(input2_np - input1_np))
    return


@app.cell
def _(mo):
    mo.md(r"""# Part 2""")
    return


@app.cell
def _(mo):
    mo.md(r"""Part 2 answer:""")
    return


@app.cell
def _(input1, input2):
    similarity = 0
    for item in input1:
        similarity += item * input2.count(item)

    similarity
    return item, similarity


if __name__ == "__main__":
    app.run()
