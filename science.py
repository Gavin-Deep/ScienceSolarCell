import time
import datetime
import Adafruit_MCP3008
'''
# Software SPI configuration:
CLK  = 18
MISO = 23
MOSI = 24
CS   = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)
'''


for x in range (30): 
	filename = "test" + str(x) + ".csv"
	print(filename)
	csv = open(filename, "w")
	csv.write("Hello\n")
	csv.write("{}\n".format(datetime.datetime.now()))
	'''
	print('Reading MCP3008 values, press Ctrl-C to quit...')
	# Print nice channel column headers.
	print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*range(8)))
	print('-' * 57)
	# Main program loop.
	while True:
	    # Read alfl the ADC channel values in a list.
	    values = [0]*8
	    for i in range(8):
		# The read_adc function will get the value of the specified channel (0-7).
		values[i] = mcp.read_adc(i)
	    # Print the ADC values.
	    print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*values))
	    # Pause for half a second.
	    time.sleep(0.5)
	'''
	csv.close()
