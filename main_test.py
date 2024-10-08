import subprocess


def test_extract():
    """Test extract()"""
    result = subprocess.run(
        ["python", "python_main.py", "extract"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Extracting data..." in result.stdout


def test_load():
    """Test transform_load()"""
    result = subprocess.run(
        ["python", "python_main.py", "transform_load"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Transforming data..." in result.stdout

if __name__ == "__main__":
    test_extract()
    test_load()