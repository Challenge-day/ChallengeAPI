from datetime import datetime, timedelta

def calculate_earned_chl(
        start_time: datetime, 
        current_time: datetime, 
        last_checked: datetime, 
        start_speed=2.5
    ) -> float:
    """
    Calculates the amount of CHL earned based on the given start time, current time, and last checked time.
    
    The CHL is earned in cycles, with each cycle having a different speed. The cycles are defined as:
    - 0 to 4 hours: 2.5 CHL/hour
    - 4 to 8 hours: 3.125 CHL/hour
    - 8 to 12 hours: 3.90625 CHL/hour
    
    If the user has been mining for more than 12 hours, the last cycle (1 CHL/hour) is used for the remaining time.
    
    Args:
        start_time (datetime): The start time of the mining session.
        current_time (datetime): The current time.
        last_checked (datetime): The last time the CHL was checked.
        start_speed (float, optional): The initial CHL speed, defaults to 2.5 CHL/hour.
    
    Returns:
        float: The amount of CHL earned.
    """
    cycles = [
        (0, 4, 2.5),
        (4, 8, 3.125),
        (8, 12, 3.90625)
    ]
    earned_chl = 0.0
    elapsed_time = (current_time - start_time).total_seconds() / 3600.0
    
    for start, end, speed in cycles:
        if elapsed_time > end:
            cycle_time = end - start
        elif elapsed_time > start:
            cycle_time = elapsed_time - start
        else:
            cycle_time = 0.0

        earned_chl += cycle_time * speed
        if elapsed_time < end:
            break
        
    # Use the last cycle if the user has been mining for more than 12 hours
    if elapsed_time > 12:
        earned_chl += (elapsed_time - 12) * 1.0

    return earned_chl

def calculate_earned_chl_since_last_check(
        start_time: datetime,
        current_time: datetime,
        last_checked: datetime,
        start_speed=2.5
    ) -> float:
    """
    Calculates the amount of CHL earned since the last checked time.
    
    Args:
        start_time (datetime): The start time of the mining session.
        current_time (datetime): The current time.
        last_checked (datetime): The last time the CHL was checked.
        start_speed (float, optional): The initial CHL speed, defaults to 2.5 CHL/hour.
    
    Returns:
        float: The amount of CHL earned since the last checked time.
    """
    total_earned_chl = calculate_earned_chl(start_time, current_time, last_checked, start_speed)
    previously_earned_chl = calculate_earned_chl(start_time, last_checked, last_checked, start_speed)
    return total_earned_chl - previously_earned_chl