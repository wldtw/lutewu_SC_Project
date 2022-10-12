"""
File: anagram.py
Name: Lu Te, Wu
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 23

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    print('Welcome to "Anagram Generator" (or -1 to quit)')
    while True:
        word = input('Find anagrams for: ')
        if word == EXIT:
            break

        start = time.time()
        anagram_lst = find_anagrams(word)
        end = time.time()

        if anagram_lst:
            print('{} anagrams found: {}'.format(len(anagram_lst), anagram_lst))
        else:
            print('None anagram found.')
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end - start} seconds.')
    print('----------------------------------')


def read_dictionary():
    dictionary_words = []
    with open(FILE, 'r') as f:
        for line in f:
            dictionary_words += line.split()
        return dictionary_words


def read_dictionary_2(word):
    dictionary_words = []
    d_dict = {}
    '''
    word =apple
    d_dict = {['a':1]....}
    '''
    for ch in word:
        if ch in d_dict:
            d_dict[ch] += 1
        else:
            d_dict.update({ch: 1})

    with open(FILE, 'r') as f:
        for line in f:
            line = line.strip()
            if len(line) == len(word):
                ch_dict = {}
                for ch in line:
                    if ch in ch_dict:
                        ch_dict[ch] += 1
                    else:
                        ch_dict.update({ch: 1})
                num_ch = 0
                for ch in ch_dict:
                    '''
                    a p l e
                    V V V X
                    '''
                    if ch not in d_dict:
                        break
                    else:
                        if ch_dict[ch] != d_dict[ch]:
                            break
                        else:
                            num_ch += 1
                        if num_ch == len(d_dict):
                            dictionary_words.append(line)
        return dictionary_words


def find_anagrams(s):
    hope_can_help_lst = ''
    dictionary = read_dictionary_2(s)
    lst = []
    w_dict = {}
    for ch in s:
        if ch in w_dict:
            w_dict[ch] += 1
        else:
            w_dict.update({ch: 1})
    find_anagrams_helper(w_dict, hope_can_help_lst, lst, dictionary, s)
    return lst


def find_anagrams_helper(w_dict, ans, lst, d, o_word):
    if len(ans) == len(o_word):
        if ans in d and ans not in lst:
            lst.append(ans)
            print('Searching...')
            print('Found: {}'.format(ans))

    for ch in o_word:
        if w_dict[ch] == 0:
            pass
        else:
            w_dict[ch] -= 1
            if has_prefix(ans+ch, d):
                find_anagrams_helper(w_dict, ans+ch, lst, d, o_word)
            w_dict[ch] += 1


def has_prefix(sub_s, d):
    for ele in d:
        if ele.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
