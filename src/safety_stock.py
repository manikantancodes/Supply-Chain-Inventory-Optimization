import numpy as np

def calculate_safety_stock(lead_time_std, demand_std, service_level=1.65):
    """
    Calculate safety stock based on the standard deviation of lead time and demand.
    
    Parameters:
        lead_time_std (float): Standard deviation of lead time.
        demand_std (float): Standard deviation of demand.
        service_level (float): Z-value for the service level (default is 1.65 for 95%).
    
    Returns:
        float: Safety stock.
    """
    try:
        safety_stock = service_level * np.sqrt(lead_time_std ** 2 + demand_std ** 2)
        return safety_stock
    except Exception as e:
        raise ValueError(f"Error calculating safety stock: {str(e)}")
