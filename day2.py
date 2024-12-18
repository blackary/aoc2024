import marimo

__generated_with = "0.10.4"
app = marimo.App(width="medium", auto_download=["html"])


@app.cell
def _():
    import marimo as mo
    from pathlib import Path
    return Path, mo


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
