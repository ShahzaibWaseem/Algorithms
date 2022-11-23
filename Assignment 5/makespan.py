import numpy as np
import random

def GreedyBalance(jobs, m):
	M = [0] * m
	J = []

	for job in jobs:
		i = np.asarray(M).argmin()
		J.append(i)
		M[i] = M[i] + job

	return J, M

if __name__ == "__main__":
	jobs = random.sample(range(1, 50), 30)
	J, M = GreedyBalance(jobs=jobs, m=10)
	print("Initial Jobs\t\t{}".format(jobs))
	print("Jobs on each machine\t{}\nLoad on each machine\t{}".format(J, M))