# test2.py
import subprocess
import sys # args

f = open("result.po", 'r')
f2 = open("result3.po", 'w')

def usage():
	print("""
Usage : python %s [-g graph_type] [-rw Read or Write] [-t time] [-y y-axis] [-l legend] [-o output]
* graph_type : f(Cumulative Bar Plot-file_type)/ b(Cumulative Bar Plot-block_type)/ t(time_plot+simple bar plot)/ all
* Read or Write : r(read)/ w(write)/ rw(both read and write) 1. time_plot(graph) only 2. rw is default
* time : sec(start):sec(end) # default - whole of the <result.po> data
* y-axis - t(time plot) : s(sector size)/ n(sector number)/ all(default) 
	 - b(block type)/f(file type) : s(I/O Size)/ c(I/O Count)/ all(default)
* legend : f(file_type)/ b(block_type) # time_plot(graph) only, not implemented.
* output # 1. name and location of the graph 2. file extension together
""" % (sys.argv[0]))

def parse1(data, data2):
        order = 0
        for i in data2:
                data[order] = i#.strip()
                order += 1
        if not data[8]:
                data[8] ="file-NONE"

        data[6] = data[6].replace("#","")
	return data

# show the script option
if sys.argv.count('-h') == 1:
	usage()
	sys.exit()

# set the time option
if sys.argv.count('-t') == 1:
	ind = sys.argv.index('-t') + 1
	time = sys.argv[ind].split(":")
	start = float(time[0])
	end = float(time[1])
	flag = True
else:
	flag = False

# set the rw option
if sys.argv.count('-rw') == 1:
	ind = sys.argv.index('-rw') + 1
	if sys.argv[ind] == 'rw':
		opt = 0
	elif sys.argv[ind] == 'r':
		opt = 1
	elif sys.argv[ind] == 'w':
		opt = 2
	else:
		print('Error!! : Invalid argvs(-rw)....')
                sys.exit()
else:
	opt = 0

while 1:
	line = f.readline().replace("\n", "")
	data = [0 for _ in range(10)]
	data2 = line.split("\t")
	if not line : break

	data = parse1(data, data2)
	tmp = ''
	if flag :
		if float(data[0]) > start and float(data[0]) < end:
			if data[1] == 'C':
				tmp = data[0]+'\t'+data[1]+'\t'+data[2]+'\t'+data[3]+'\t'+data[4]+'\t'+data[5]+'\t'+data[6]+'\t'+data[7]+'\t'+data[8]+'\n'
				#f2.write(data[0]+'\t'+data[1]+'\t'+data[2]+'\t'+data[3]+'\t'+data[4]+'\t'+data[5]+'\t'+data[6]+'\t'+data[7]+'\t'+data[8]+'\n')
		elif float(data[0]) > end:
				break
	else :
		if data[1] == 'C':
			#f2.write(data[0]+'\t'+data[1]+'\t'+data[2]+'\t'+data[3]+'\t'+data[4]+'\t'+data[5]+'\t'+data[6]+'\t'+data[7]+'\t'+data[8]+'\n')
			tmp = data[0]+'\t'+data[1]+'\t'+data[2]+'\t'+data[3]+'\t'+data[4]+'\t'+data[5]+'\t'+data[6]+'\t'+data[7]+'\t'+data[8]+'\n'
	
	#print("tmp : "+tmp)
	#print(opt)
	# Read or Write option
	if not tmp == '':
		if opt == 0 or (opt == 1 and data[2].count('R') > 0) or (opt == 2 and data[2].count('W') > 0):
			f2.write(tmp)
			
f.close()
f2.close()

flag2 = False
# set the graph_type option.
if sys.argv.count('-g') == 1:
	ind = sys.argv.index('-g') + 1
	if sys.argv[ind] == 'f':
		exe = 'python test3.py'
		# set the Y-axis Option
		if sys.argv.count('-y') == 1:
                        ind2 = sys.argv.index('-y') + 1
                        if sys.argv[ind2] == 's' or sys.argv[ind2] == 'c' or sys.argv[ind2] == 'all':
                                exe = exe + ' -y ' + sys.argv[ind2]
                        else:
                                print('Error!! : Invalid argvs(-y)....')
				sys.exit()
	elif sys.argv[ind] == 'b':
		exe = 'python test.py'
		# set the Y-axis Option
		if sys.argv.count('-y') == 1:
			ind2 = sys.argv.index('-y') + 1
			if sys.argv[ind2] == 's' or sys.argv[ind2] == 'c' or sys.argv[ind2] == 'all':
				exe = exe + ' -y ' + sys.argv[ind2]
			else:
				print('Error!! : Invalid argvs(-y)....')
				sys.exit()
	elif sys.argv[ind] == 't':
		exe = 'Rscript rscript2.r'
		# set the Y-axis Option
		if sys.argv.count('-y') == 1:
			ind2 = sys.argv.index('-y') + 1
			if sys.argv[ind2] == 's' or sys.argv[ind2] == 'n' or sys.argv[ind2] == 'all':
				exe = exe +' -y '+ sys.argv[ind2]
			else:
				print('Error!! : Invalid argvs(-y)....')
                                sys.exit()
	elif sys.argv[ind] == 'all':
		exe1 = 'python test.py' # 'b(block)
		exe2 = 'Rscript rscript2.r' # t(time)
		exe3 = 'python test3.py' # f(file)
		flag2 = True
	else:
		print('Error!! : Invalid argvs(-g)....')
		sys.exit()
else: # all is default
	exe1 = 'python test.py' # 'b(block)
        exe2 = 'Rscript rscript2.r' # t(time)
        exe3 = 'python test3.py' # f(file)
        flag2 = True

# set the Output file option
if sys.argv.count('-o') == 1:
        ind = sys.argv.index('-o') + 1
	if not sys.argv[ind].count('.') == 1:
		print('Error!! : Cannot find file_extension....')
		sys.exit()
	#else:
	#	out = sys.argv[ind].split('.')
	#	subprocess.call('Rscript output.r -o '+sys.argv[ind]+' '+out[1], shell=True) # out[1] : file_extension
	else:
		out = sys.argv[ind].split('.')
                exe = exe +' -o '+ sys.argv[ind] +' ' + out[1] # out[1] : file_extension
	
subprocess.call('rm -rf save/*', shell = True) # Delete the Previous Graph File.
#print(exe)
if flag2 == False: # b, f, t
	subprocess.call(exe, shell = True)
else: # all
	subprocess.call(exe1, shell = True)
	subprocess.call(exe2, shell = True)
	subprocess.call(exe3, shell = True)

#subprocess.call('R CMD BATCH rscript2.r', shell=True)

