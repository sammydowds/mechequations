

#Grubler's Formula: The number of degrees of freedom of a mechanism with links and joints
def d_o_f(N, joint_info, m):
	#N = number of links, count ground as one if necessary
	#m = 3 if planar, m = 6 if spatial
	#joint_info: list of degrees of freedom for each joint
	J = len(joint_info)
	A = 0
	for i in range(0, len(joint_info)):
		A = A + joint_info[i]
	
	dof = m*(N-1-J) + A

	return "This mechanism has: {} degree(s) of freedom".format(dof)

fi = 1, 1, 1, 1
print(d_o_f(5, fi, 3))