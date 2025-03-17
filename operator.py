'''This script starts the water flow, adjusts the valves (using valvsim.py), 
and closes the valves when off signal is received'''

import time
import valvesim as v

# TODO: Need to work out and include the logic for the case when one or the other
# valve is at max open and the other valve has to be adjusted to get to the
# desired temp.  Also, incorporate the total flow setting into the logic
# (case in which the user only wants 50% flow)  Totaal flow defined as 
# (cold_flow_% + hot_flow_%)/2

# Get desired Temp setting
# get desired water_flow setting ()

# heater_type = tank or tankless

# On Sequence
# Check water heater type (tank, tankless)

# If 'tank' open the hot valve to max
#   while get_output_temp() <= desired temp + 1:
#       time.sleep(2)

# while output_temp > desired_temp
#   cold_change(+1)
#   time.sleep(2)

# If 'tankless' open the hot valve to 10%
#   while get_output_temp() <= desired temp + 1:
#       time.sleep(0.5)

# while output_temp > desired_temp
#   cold_change(+1)
#   time.sleep(2)


# maintain_desired_temp()
# while total_flow <= 100:
#   if (hot_valve_setting < 100%) and (cold_flow_setting < 100%):
#       
