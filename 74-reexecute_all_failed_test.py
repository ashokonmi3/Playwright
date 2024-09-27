import pytest
import random


def test_normal_case():
    assert True  # This will always pass


def test_flaky_case():
    assert random.choice([True, False])  # This may fail randomly


def test_another_normal_case():
    assert 1 + 1 == 2  # This will always pass


if __name__ == "__main__":
    pytest.main()

# pytest - -reruns 3 --reruns-delay 2 .\74-reexecute_all_failed_test.py
