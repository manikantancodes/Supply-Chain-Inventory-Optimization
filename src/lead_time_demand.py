import numpy as np

def calculate_lead_time_demand(lead_times, products_sold, stock_levels):
    """
    Calculate lead time demand.
    
    Parameters:
        lead_times (float or array-like): Lead times in days.
        products_sold (float or array-like): Number of products sold during the period.
        stock_levels (float or array-like): Current stock levels.

    Returns:
        float: Lead time demand.
    """
    try:
        lead_time_demand = (lead_times * products_sold) / stock_levels
        return lead_time_demand
    except Exception as e:
        raise ValueError(f"Error calculating lead time demand: {str(e)}")
