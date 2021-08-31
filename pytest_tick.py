import pathlib

from playsound import playsound


def pytest_runtest_setup(item) -> None:
    path = pathlib.Path(__file__).parent.resolve() / "default.mp3"
    playsound(str(path), block=False)

