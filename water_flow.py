#  calculates and returns the height of a column of water from a tower height and a tank wall height


def water_column_height(tower_height, tank_height):
    column_height = tower_height + (3  * tank_height / 4)
    # h is height of the water column
    # t is the height of the tower
    # w is the height of the walls of the tank that is on top of the tower
    return column_height

def pressure_gain_from_water_height(height,gravity,density):
    # P is the pressure in kilopascals
    # ρ is the density of water 998.2 ( kilogram / meter3) *Just use # in your calculations
    # g is the acceleration from Earths gravity 9.80665 (meter / second2) *Just use # in your calculations
    # h is the height of the water column in meters
    pressure = (density* gravity *height) / 1000
    rounded = round(pressure,3)
    return pressure

def pressure_loss_from_pipe(pipe_diameter,pipe_length, friction_factor, fluid_velocity):
    # P is the lost pressure in kilopascals
    # f is the pipe’s friction factor
    # L is the length of the pipe in meters
    # ρ is the density of water 998.2 (kilogram / meter3) *Just use # in your calculations
    # v is the velocity of the water flowing through the pipe in meters / second
    # d is the diameter of the pipe in meters
    lost_pressure_from_pipe = (-friction_factor * pipe_length *998.2 *fluid_velocity**2) / (2000*pipe_diameter)
    rounded = round(lost_pressure_from_pipe,3)
    return rounded


def pressure_loss_from_fittings(fluid_velocity,quantity_fittings):
    # P is the lost pressure in kilopascals
    # ρ is the density of water (998.2 kilogram / meter3)
    # v is the velocity of the water flowing through the pipe in meters / second
    # n is the quantity of fittings
    lost_pressure_from_fitings = (-0.04 * 998.2 *fluid_velocity ** 2 * quantity_fittings) / 2000
    rounded = round(lost_pressure_from_fitings,3)
    return rounded

def reynolds_number(hydraulic_diameter, fluid_velocity, viscosity):
    # R is the Reynolds number
    # ρ is the density of water (998.2 kilogram / meter3)
    # d is the hydraulic diameter of a pipe in meters. For a round pipe, the hydraulic diameter is the same as the pipe’s inner diameter.
    # v is the velocity of the water flowing through the pipe in meters / second
    # μ is the dynamic viscosity of water (0.0010016 Pascal seconds)

    reynolds_number = (998.2*hydraulic_diameter*fluid_velocity) / viscosity
    rounded = round(reynolds_number,3)
    return rounded

def pressure_loss_from_pipe_reduction(larger_diameter,
        fluid_velocity, reynolds_number, smaller_diameter):
    
    # k is a constant computed by the first formula and used in the second formula
    # R is the Reynolds number that corresponds to the pipe with the larger diameter
    # D is the diameter of the larger pipe in meters
    # d is the diameter of the smaller pipe in meters
    # P is the lost pressure kilopascals
    # ρ is the density of water (998.2 kilogram / meter3)
    # v is the velocity of the water flowing through the larger diameter pipe in meters / second

    constant_k = (0.1 + (50/reynolds_number)) * ((((larger_diameter/smaller_diameter)**4))-1)

    lost_pressure = (-constant_k * 998.2 * fluid_velocity**2)/2000
    rounded = round(lost_pressure,3)
    return rounded

    

PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)
HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)
# Exceeding requirements
EARTH_ACCELERATION_OF_GRAVITY = 9.8066500  #(meter / second2)
WATER_DENSITY = 998.2                # kilogram / meter3)
WATER_DYNAMIC_VISCOSITY = 0.0010016

def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))
    water_height = water_column_height(tower_height, tank_height)
    gravity = EARTH_ACCELERATION_OF_GRAVITY
    density = WATER_DENSITY
    pressure = pressure_gain_from_water_height(water_height,gravity,density)
    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    viscosity = WATER_DYNAMIC_VISCOSITY
    reynolds = reynolds_number(diameter, velocity, viscosity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss
    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss
    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss
    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss
    print(f"Pressure at house: {pressure:.1f} kilopascals")
if __name__ == "__main__":
    main()




