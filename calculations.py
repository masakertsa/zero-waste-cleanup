import math

def calculate_time_based_dissolution(membrane_thickness_mm, dissolution_rate_mm_per_hour, material_name="Starch-based Biopolymer"):
    """
    Calculates the exact lifespan of the capsule based on chemical dissolution time.
    Optimized for biodegradable materials like Starch or Alginate.
    """
    if dissolution_rate_mm_per_hour <= 0:
        return 0
    
    time_hours = membrane_thickness_mm / dissolution_rate_mm_per_hour
    time_minutes = time_hours * 60
    
    print(f"--- TRIGGER TYPE A: TIME-BASED DISSOLUTION ---")
    print(f"✓ Selected Material: {material_name}")
    print(f"✓ Membrane Thickness: {membrane_thickness_mm} mm")
    print(f"✓ Dissolution Rate in Seawater: {dissolution_rate_mm_per_hour} mm/hour")
    print(f"✓ Total Active Deployment Window: {time_hours:.2f} hours ({time_minutes:.1f} minutes)")
    print(f"✓ Mechanical Status: Shell dissolves completely, releasing the core automatically.")
    print(f"-----------------------------------------------\n")
    return time_hours

def calculate_depth_based_pressure(target_depth_meters, material_name="Sodium Alginate (Cross-linked)"):
    """
    Calculates the exact hydrostatic pressure the shell must withstand before bursting at a specific depth.
    Uses Pascal's Law: P = rho * g * h
    """
    GRAVITY = 9.81              # m/s^2
    SEA_WATER_DENSITY = 1025.0  # kg/m^3 (Average marine water salinity)
    ATMOSPHERIC_PRESSURE = 101325.0  # Pascals (1 atm at sea level surface)
    
    # Calculate hydrostatic and total pressure
    hydrostatic_pressure_pa = SEA_WATER_DENSITY * GRAVITY * target_depth_meters
    total_pressure_pa = hydrostatic_pressure_pa + ATMOSPHERIC_PRESSURE
    
    # Convert to bars for industrial standard reading
    hydrostatic_bar = hydrostatic_pressure_pa / 100000.0
    total_bar = total_pressure_pa / 100000.0
    
    print(f"--- TRIGGER TYPE B: DEPTH-RESPONSIVE PRESSURE ---")
    print(f"✓ Selected Material: {material_name}")
    print(f"✓ Target Activation Depth: {target_depth_meters} meters")
    print(f"✓ Hydrostatic Pressure: {hydrostatic_bar:.2f} bar")
    print(f"✓ Total Mechanical Pressure (inc. 1 atm air): {total_bar:.2f} bar")
    print(f"✓ Mechanical Status: Membrane must be engineered to burst precisely at {total_bar:.2f} bar.")
    print(f"-----------------------------------------------\n")
    return total_bar

# ==========================================================
# RUN SIMULATION WITH ECO-FRIENDLY POLYMERS
# ==========================================================
print("=== ZERO WASTE CLEANUP: MEMBRANE KINETICS MODEL ===\n")
print("Material Database: [Sodium Alginate, Starch Polymer, Chitin/Chitosan]\n")

# Scenario 1: Time-based shell configuration (e.g., starch) - calibrated for a 5-hour degradation window
calculate_time_based_dissolution(
    membrane_thickness_mm=0.5, 
    dissolution_rate_mm_per_hour=0.1,
    material_name="Starch-based Biopolymer (Predictable Degradation)"
)

# Scenario 2: Depth-responsive shell configuration (e.g., seaweed extract) - calibrated to burst at 30 meters
calculate_depth_based_pressure(
    target_depth_meters=30.0,
    material_name="Sodium Alginate / Seaweed Extract (Pressure-Resistant, Sharp Failure)"
)
