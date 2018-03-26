import os.path, subprocess

def run_corels (fname):
	fargs = fname + ".out " + fname + ".label "
	fminor = fname + ".minor"
	if (os.path.isfile(fminor)):
		fargs += " " + fminor
	command = "../src/corels -c 2 -p 1 -r 0.01 -v progress,log -j 6144 -n 1000000000 " + fargs
	return subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True).communicate()

def main ():
	for fname in ["../data/CrossValidation/mushroom_" + str(x) + "_train" for x in range(10)]:
		basename = fname[fname.rfind('/')+1:]
		try:
			f = open("../results/" + basename + ".txt", "w")
			f.write(run_corels(fname))
		finally:
			f.close()

main()
