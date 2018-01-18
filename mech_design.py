


def design_factor(loss_of_function_par, maximum_allowable_par):
	#Mechanical Engineering Design by Shigleys 8th edition page 27. The parameters below could be load, stress, deflection etc.
	nd = loss_of_function_par/maximum_allowable_par

	#Example: Max load known within +- 20%, load that causes failure is known within +- 15%. Load causing failure is nominally 2000lbf
	#load that causes failure --> (worst case) = 1/0.85.. more than we think, and max load that causes failure: 1/1.2 (assume its less than what we think)
	#Design factor (nd) = (1/0.85)/(1/1.2) = 1.4
	#Therefore max load can be re-calculated with this design factor: Max load allowable = 2000lbf/1.4 = 1400lbf allowed

	return nd

