

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

def single_joint_torque_force(M, angul_acc, m, g, r, theta):
	#M is the scalar inertia of the link about the axis of rotation, m is mass of link, r is the distance from the axis to the center of mas of the link
	tau = M*angul_acc + m*g*r*cos(theta)
	return tau


class Forward_Kinematics():
	def position_end_effector(L1, L2, L3, joint_angle1, joint_angle2, joint_angle3):
		#position of end effector based on lengths of links and joint angles
		x = L1*cos(joint_angle1) + L2*cos(joint_angle1 + joint_angle2) + L3*cos(joint_angle1+joint_angle2+joint_angle3)
		y = L1*sin(joint_angle1) + L2*sin(joint_angle1 + joint_angle2) + L3*sin(joint_angle1+joint_angle2+joint_angle3)
		phi = joint_angle1 + joint_angle2 + joint_angle3

	def forward_kinematics_matrice(T01, T12, T23, T34):
		#returns the forward kinematics matrice by finding the product of four homogeneous transformation matrices
		T04 = T01*T12*T23*T34

	def 3r_planar_open_chain(L1, L2, L3, theta_1, theta_2, theta_3):
		#modeling a 3R open chain with only planar motion
		T01 = [cos(theta_1), -sin(theta_1), 0, 0; sin(theta_1), cos(theta1), 0, 0; 0, 0, 1, 0; 0, 0, 0, 1]

		return T04
fi = 1, 1, 1, 1
print(d_o_f(5, fi, 3))