import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import pytest
from datetime import datetime, timedelta
from src.services.mining_service import calculate_earned_chl, calculate_earned_chl_since_last_check

def test_calculate_earned_chl_first_cycle():
    start_time = datetime.utcnow() - timedelta(hours=2)
    current_time = datetime.utcnow()
    last_checked = start_time
    earned_chl = calculate_earned_chl(start_time, current_time, last_checked)
    expected_chl = 2 * 2.5
    assert earned_chl == pytest.approx(2 * 2.5, rel=1e-5), f"Expected {expected_chl}, got {earned_chl}"

def test_calculate_earned_chl_second_cycle():
    start_time = datetime.utcnow() - timedelta(hours=6)
    current_time = datetime.utcnow()
    last_checked = start_time
    earned_chl = calculate_earned_chl(start_time, current_time, last_checked)
    expected_chl = (4 * 2.5) + (2 * 3.125)
    assert earned_chl == pytest.approx(expected_chl, rel=1e-5), f"Expected {expected_chl}, got {earned_chl}"

def test_calculate_earned_chl_thrid_cycle():
    start_time = datetime.utcnow() - timedelta(hours=10)
    current_time = datetime.utcnow()
    last_checked = start_time
    earned_chl = calculate_earned_chl(start_time, current_time, last_checked)
    expected_chl = (4 * 2.5) + (4 * 3.125) + (2 * 3.90625)
    assert earned_chl == pytest.approx(expected_chl, rel=1e-5), f"Expected {expected_chl}, got {earned_chl}"

def test_calculate_earned_chl_fourth_cycle():
    start_time = datetime.utcnow() - timedelta(hours=14)
    current_time = datetime.utcnow()
    last_checked = start_time
    earned_chl = calculate_earned_chl(start_time, current_time, last_checked)
    expected_chl = (4 * 2.5) + (4 * 3.125) + (4 * 3.90625) + (2 * 1.0)
    assert earned_chl == pytest.approx(expected_chl, rel=1e-5), f"Expected {expected_chl}, got {earned_chl}"

def test_calculate_earned_chl_multiple_checks():
    start_time = datetime.utcnow() - timedelta(hours=5)
    current_time = datetime.utcnow()
    last_checked = datetime.utcnow() - timedelta(hours=1)
    earned_chl = calculate_earned_chl_since_last_check(start_time, current_time, last_checked)
    expected_chl = 1 * 3.125
    assert earned_chl == pytest.approx(expected_chl, rel=1e-5), f"Expected {expected_chl}, got {earned_chl}"
