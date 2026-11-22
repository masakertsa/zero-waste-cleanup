"""
Zero Waste Cleanup - Calculation Framework
Parametric physics, thermodynamics, and fluid dynamics model for the biodegradable
deep-water microplastic collection capsule (Alginate/PHA shell, Oleic-Fe3O4 bio-ferrofluid,
and exothermic CaCl2 osmotic burst core).
"""

import math


def calculate_rupture_depth(
    membrane_tensile_strength_pa: float = 22_000_000.0,
    capsule_radius_m: float = 0.035,
    pha_wall_thickness_m: float = 0.0012,
    seawater_density_kg_m3: float = 1025.0,
) -> float:
    """
    Calculates the target ocean depth (in meters) where hydrostatic pressure ruptures
    the rigid PHA inner shell (calibrated for 50-200 m / 5-20 bar activation).
    
    Thin-walled spherical shell burst pressure: P_burst = (2 * sigma * t) / r
    Hydrostatic depth: h = P_burst / (rho * g)
    """
    if capsule_radius_m <= 0 or pha_wall_thickness_m <= 0 or seawater_density_kg_m3 <= 0:
        return 0.0

    gravity = 9.81
    burst_pressure_pa = (2.0 * membrane_tensile_strength_pa * pha_wall_thickness_m) / capsule_radius_m
    rupture_depth_m = burst_pressure_pa / (seawater_density_kg_m3 * gravity)
    return round(rupture_depth_m, 1)


def model_osmotic_pump_flow_rate(
    cacl2_molarity_mol_l: float = 4.5,
    oleic_acid_viscosity_pa_s: float = 0.055,
    deep_water_temp_c: float = 3.0,
    membrane_area_m2: float = 0.015,
) -> float:
    """
    Models passive osmotic pressure (in bar) and seawater influx rate (in mL/min)
    driven by the CaCl2 core across the semi-permeable shell at deep-sea temperatures (+2 to +4 °C).
    
    Van 't Hoff equation: Pi = i * M * R * T
    """
    if cacl2_molarity_mol_l <= 0 or oleic_acid_viscosity_pa_s <= 0:
        return 0.0

    # Van 't Hoff factor i ~ 2.7 for dissociated CaCl2 in concentrated brine
    van_t_hoff_i = 2.7
    gas_constant_r = 8.314  # J / (mol * K)
    temp_kelvin = deep_water_temp_c + 273.15
    concentration_mol_m3 = cacl2_molarity_mol_l * 1000.0

    osmotic_pressure_pa = van_t_hoff_i * concentration_mol_m3 * gas_constant_r * temp_kelvin

    # Hydraulic permeability inversely scaled by cold bio-ferrofluid viscosity
    hydraulic_conductivity = 1.8e-12 / oleic_acid_viscosity_pa_s
    flow_rate_m3_s = hydraulic_conductivity * membrane_area_m2 * osmotic_pressure_pa
    flow_rate_ml_min = flow_rate_m3_s * 1_000_000.0 * 60.0
    return round(flow_rate_ml_min, 3)


def calculate_buoyancy_inversion(
    magnetite_fe3o4_mass_g: float = 4.5,
    remaining_cacl2_salt_g: float = 0.0,
    oleic_oil_mass_g: float = 85.0,
    trapped_microplastic_mass_g: float = 12.0,
    seawater_density_kg_m3: float = 1025.0,
) -> dict:
    """
    Models the buoyancy shift from negative (sinking) to positive (surface ascent).
    Once CaCl2 dissolves out, the low-density oleic acid (~895 kg/m3) + bound microplastics
    (~920 kg/m3) overcome the small Fe3O4 magnetite payload (~5170 kg/m3).
    """
    # Component densities (kg/m3)
    rho_fe3o4 = 5170.0
    rho_cacl2 = 2150.0
    rho_oil = 895.0
    rho_plastic = 920.0  # Typical PE/PP marine microplastic density

    total_mass_kg = (
        magnetite_fe3o4_mass_g + remaining_cacl2_salt_g + oleic_oil_mass_g + trapped_microplastic_mass_g
    ) / 1000.0

    total_volume_m3 = (
        (magnetite_fe3o4_mass_g / 1000.0) / rho_fe3o4
        + (remaining_cacl2_salt_g / 1000.0) / rho_cacl2
        + (oleic_oil_mass_g / 1000.0) / rho_oil
        + (trapped_microplastic_mass_g / 1000.0) / rho_plastic
    )

    effective_density_kg_m3 = total_mass_kg / total_volume_m3 if total_volume_m3 > 0 else 0.0
    net_buoyancy_force_n = (seawater_density_kg_m3 - effective_density_kg_m3) * total_volume_m3 * 9.81

    return {
        "positive_buoyancy": effective_density_kg_m3 < seawater_density_kg_m3,
        "cluster_density_kg_m3": round(effective_density_kg_m3, 1),
        "net_lift_force_mn": round(net_buoyancy_force_n * 1000.0, 2),
    }


def estimate_magnetic_retrieval_force(
    magnetite_mass_g: float = 4.5,
    electromagnet_tesla: float = 0.85,
    distance_m: float = 0.15,
) -> float:
    """
    Calculates magnetic attraction force (in milliNewtons) exerted by a downstream
    electromagnetic boom on an oleic-coated Fe3O4 nanoparticle cluster at distance r.
    """
    if magnetite_mass_g <= 0 or electromagnet_tesla <= 0 or distance_m <= 0:
        return 0.0

    # Mass susceptibility of superparamagnetic Fe3O4 nanoparticles (~0.085 m^3/kg)
    chi_mass = 0.085
    mu_0 = 4.0 * math.pi * 1e-7
    mass_kg = magnetite_mass_g / 1000.0

    # Near-field dipole gradient approximation: B(r) decays with distance from boom pole
    pole_radius_m = 0.08
    local_field_b = electromagnet_tesla * ((pole_radius_m / (pole_radius_m + distance_m)) ** 2)
    field_gradient = (2.0 * local_field_b) / (pole_radius_m + distance_m)

    force_newtons = (chi_mass * mass_kg * local_field_b * field_gradient) / mu_0
    return round(force_newtons * 1000.0, 2)


if __name__ == "__main__":
    print("--- Zero Waste Cleanup: Calculation Framework ---")

    depth = calculate_rupture_depth()
    print(f"1. Calibrated PHA Shell Rupture Depth: {depth} m (~{depth / 10.0:.1f} bar)")

    flow = model_osmotic_pump_flow_rate()
    print(f"2. Cold-Water (+3°C) CaCl2 Osmotic Influx: {flow} mL/min")

    buoyancy = calculate_buoyancy_inversion(remaining_cacl2_salt_g=0.0)
    print(
        f"3. Post-Burst Buoyancy Inversion: Ascent={buoyancy['positive_buoyancy']} | "
        f"Cluster Density: {buoyancy['cluster_density_kg_m3']} kg/m³ (Net Lift: +{buoyancy['net_lift_force_mn']} mN)"
    )

    mag_force = estimate_magnetic_retrieval_force(magnetite_mass_g=4.5, electromagnet_tesla=0.85, distance_m=0.15)
    print(f"4. Electromagnetic Boom Capture Force (at 15 cm): {mag_force} mN")
