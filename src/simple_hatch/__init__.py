from pathlib import Path

def get_sample():
    file = Path(__file__).parent.joinpath("data/sample.csv")
    print("file", file)
    return file.exists()
