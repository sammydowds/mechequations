


def design_factor(loss_of_function_par, maximum_allowable_par):
	#Mechanical Engineering Design by Shigleys 8th edition page 27. The parameters below could be load, stress, deflection etc.
	nd = loss_of_function_par/maximum_allowable_par

	#Example: Max load known within +- 20%, load that causes failure is known within +- 15%. Load causing failure is nominally 2000lbf
	#load that causes failure --> (worst case) = 1/0.85.. more than we think, and max load that causes failure: 1/1.2 (assume its less than what we think)
	#Design factor (nd) = (1/0.85)/(1/1.2) = 1.4
	#Therefore max load can be re-calculated with this design factor: Max load allowable = 2000lbf/1.4 = 1400lbf allowed

	return nd


def axial_stress(F, A):
	#F = axial force, A = cross-sectional area
	a_s = F/A

	return a_s

def axial_strain(change_in_length, original_length):
	a_strain = change_in_length/orginial_length
	return a_strain

def UNS_carbon_steels(look_up):
	UNS_CS = {'G10': 'Plain Carbon', 'G11': 'Free-cutting carbon steel with more sulfur or phosphorus', 'G13': 'Manganese', 'G23': 'Nickel', 'G25': 'Nickel', 'G31': 'Nickel-chromium', 'G33': 'Nickel-chromium', 'G40': 'Molybdenum', 'G41': 'Chromium-molybdenum', 'G43': 'Nickel-chromium-molybdenum', 'G46': 'Nickel-molybdenum', 'G48': 'Nickel-molybdenum', 'G50': 'Chromium', 'G51': 'Chromium', 'G52': 'Chromium', 'G61': 'Chromium-vanadium', 'G86': 'Chromium-nickel-molybdenum', 'G87': 'Chromium-nickel-molybdenum', 'G92': 'Manganese-silicon', 'G94': 'Nickel-chromium-molybdenum'}
	UNS_desc = UNS_CS[look_up]
	print(UNS_CS[look_up])
	return UNS_desc

class Ball_Screws():
	#class for calculating life of a ball screw in revolutions

	def Life_expectancy(Ca, Fm, fw):
		"""LIfe in revolutions
		Ca = Basic dynamic load rating
		Fm = equivalent axial load (N)
		fw = fatigue facture
		"""

		L = ((Ca/(Fm*fw))**3)*10**6

		return L
	#life expectancy
	

UNS_carbon_steels('G10')