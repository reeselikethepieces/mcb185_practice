# 2AEprecision.py is the redoing (Gregory-Leibniz series * 4) = pi but with some precision

# 1e-6 precision
appro_pi = 0
sign = 1
denom = 1
precision = 1e-6
while True:
	final_pi = appro_pi
	appro_pi += sign * (1 / denom)
	denom += 2
	sign *= -1
	
	if abs(appro_pi - final_pi) < precision:
		break
		
	print(4 * final_pi)