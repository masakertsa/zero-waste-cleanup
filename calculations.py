import math

def calculate_capsule_triggers(target_depth_meters, membrane_thickness_mm, dissolution_rate_mm_per_hour):
    # Constants for marine water fysiikka
    GRAVITY = 9.81  # m/s^2
    SEA_WATER_DENSITY = 1025.0  # kg/m^3
    ATMOSPHERIC_PRESSURE = 101325.0  # Pascals (1 atm at surface)
    
    # 1. Depth and Hydrostatic Pressure Calculation (Pascal's Law)
    # Hydrostatic pressure: P = rho * g * h
    hydrostatic_pressure_pa = SEA_WATER_DENSITY * GRAVITY * target_depth_meters
    total_pressure_pa = hydrostatic_pressure_pa + ATMOSPHERIC_PRESSURE
    total_pressure_bar = total_pressure_pa / 100000.0
    
    # 2. Time-Based Dissolution Calculation
    # Time = Thickness / Dissolution Rate
    dissolution_time_hours = membrane_thickness_mm / dissolution_rate_mm_per_hour
    
    print(f"--- ZERO WASTE CLEANUP: CAPSULE TRIGGER MECHANISMS ---")
    print(f"Target Burst Depth: {target_depth_meters} meters")
    print(f"Membrane Thickness: {membrane_thickness_mm} mm")
    print(f"Material Dissolution Rate: {dissolution_rate_mm_per_hour} mm/hour")
    print(f"----------------------------------------------------")
    print(f"[DEPTH TRIGGER SPEKSIT]")
    print(f"✓ Hydrostatic Pressure at {target_depth_meters}m: {(hydrostatic_pressure_pa / 100000.0):.2f} bar")
    print(f"✓ Total Mechanical Pressure Required for Shell Burst: {total_pressure_bar:.2f} bar")
    print(f"----------------------------------------------------")
    print(f"[TIME TRIGGER SPEKSIT]")
    print(f"✓ Shell Degradation Windows: {dissolution_time_hours:.2f} hours until core release")
    print(f"----------------------------------------------------")
    print(f"Engineering Note: For a depth of {target_depth_meters}m, the biopolymer must withstand {total_pressure_bar:.2f} bar before structural failure.")

# Run calculations with optimized prototype parameters:
# Target depth 30 meters, 0.5 mm membrane, dissolving at 0.1 mm per hour
calculate_capsule_triggers(
    target_depth_meters=30.0, 
    membrane_thickness_mm=0.5, 
    dissolution_rate_mm_per_hour=0.1
)
