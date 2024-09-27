import pytest
import random


@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_random_failure():
    # This test will randomly fail
    assert random.choice([True, False])


def test_success():
    # This test will randomly fail
    assert random.choice([True, False])


if __name__ == "__main__":
    pytest.main()

# pip install pytest-rerunfailures
