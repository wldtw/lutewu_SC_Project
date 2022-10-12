import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
EXIT = -1
SIZE = 4


def main():
	boggle_dict = {}
	read_dict = {}
	print('Time to play boggle!')
	while True:
		for i in range(SIZE):
			line = input(f'{i+1} row of letters: ')
			temp = line.split()
			# to check enter two keys or letters more than 4
			switch = False
			if len(temp) == SIZE:
				for j in range(SIZE):
					s = ''
					s += temp[j]
					if len(s) > 1:
						switch = True
					if s.isalpha():
						boggle_dict[i, j] = s
						if s in read_dict:
							read_dict[s] += 1
						else:
							read_dict[s] = 1
					else:
						switch = True
			else:
				print(f'Please enter {SIZE} letters in a row')
				break
			if switch:
				print('Illegal input. Please enter four single alphabet in a row.')
				break
		print(f'We have found {len(find_boggle(boggle_dict, read_dictionary(read_dict), 0, 0, [], ""))} words. ')

	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_boggle(boggle_dict, d, x, y, position_used, s):
	ans_lst = []

	for ele in boggle_dict:
		x = ele[0]
		y = ele[1]
		s = ''
		s += boggle_dict[ele]

		find_boggle_helper(boggle_dict, d, x, y, [ele], s, ans_lst)
	return ans_lst


def find_boggle_helper(boggle_dict, d, x, y, position_used, s, ans_lst):
	# base case
	if len(s) >= SIZE:
		if s in d and s not in ans_lst:
			ans_lst.append(s)
			print(f'Found: {s}')

	# choose
	for i in range(-1, 2):
		for j in range(-1, 2):
			new_x = x + i
			new_y = y + j
			position = (new_x, new_y)

			if position in boggle_dict and position not in position_used:
				position_used.append(position)
				s += boggle_dict[position]
				if has_prefix(s, d):

					find_boggle_helper(boggle_dict, d, new_x, new_y, position_used, s, ans_lst)

				# unchoose
				position_used.pop()
				s = s[:-1]


def read_dictionary(read_dict):
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r')as f:
		lst = []
		for line in f:
			d = {}
			line = line.strip()
			if len(line) >= 4:
				for ch in line:
					if ch in d:
						d[ch] += 1
					else:
						d[ch] = 1

				check_num = 0
				for ch, count in d.items():
					if ch in read_dict and count <= read_dict[ch]:
						count = 0
					check_num += count
				if check_num == 0:
					lst.append(line)
		return lst


def has_prefix(sub_s, d):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for ele in d:
		if ele.startswith(sub_s):
			return True

	return False


if __name__ == '__main__':
	main()
