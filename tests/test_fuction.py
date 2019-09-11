import pytest
from actions_demo.fibonacci import recur_fibo

def test_fib():
    assert recur_fibo(0) == 0
    assert recur_fibo(1) == 1
    assert recur_fibo(6) == 8