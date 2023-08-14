"""
File: weather_master.py
Name: Lu-Te, Wu
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
"""
EXIT = -100


def main():
	print('Welcome \"Weather Master 4.0\"!')
	n = int(input('First Temperature: ? (or ' + str(EXIT) + ' to quit)'))
	min_num = n
	max_num = n
	input_num = n
	input_times = 0
	while True:
		n = int(input('Next Temperature: ? (or ' + str(EXIT) + ' to quit)'))
		if n != EXIT:
			if n > max_num:
				max_num = n
			elif n < min_num:
				min_num = n
			input_num += n
			input_times += 1
		else:
			break
	print(f'Minimum number : {min_num}')
	print(f'Maximum number : {max_num}')
	print(f'Average number : {input_num / input_times}')


if __name__ == "__main__":
	main()
