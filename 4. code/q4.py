import random
import sys
import time
import numpy as np

def roll_dice(prob=.5):
	r = random.random()
	# print r, prob
	if r <= prob:
		return True
	return False

def create_sample():
	#clouds, sprinkler, rain, grass
	weighting = 1.0

	# since S and W are evidence, fix them to 1
	sprinkler = True
	grass = True

	clouds = roll_dice(.50)
	if clouds:
		weighting *= .1
		rain = roll_dice(.80)
	else:
		weighting *= .9
		rain = roll_dice(.20)

	if sprinkler and rain:
		weighting *= .99
	elif sprinkler and not rain:
		weighting *= .90
	elif rain and not sprinkler:
		weighting *= .90
	else:
		weighting *= 0

	return {"clouds": clouds, "sprinkler": sprinkler, "rain": rain, "grass":grass, "weighting":weighting}


def run(n_samples):
	positive = 0.0
	for blah in xrange(n_samples):
		x = create_sample()
		if x['clouds']:
			positive += x['weighting']
	return float(positive/n_samples)


if __name__ == "__main__":
	if len(sys.argv) < 2 or not sys.argv[1] or not sys.argv[2]:
		print "Usage: python q4.py <m_runs> <n_samples>"
		exit()

	sum_runs = []
	start = time.time()
	print "starting", sys.argv[1], "runs of", int(sys.argv[2]), "samples"
	for i in xrange(int(sys.argv[1])):
		sum_runs.append(run(int(sys.argv[2])))
	end = time.time()
	print
	print "computed in",round(end-start, 4)
	print "len:", len(sum_runs)
	print "avg:", np.mean(sum_runs)
	print "std:", np.mean(sum_runs)




