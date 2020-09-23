string1 = 'asdfghj'

print('Number of characters in the string:', len(string1))

p_cen = int(len(string1) / 2)
p_ini = p_cen - 1
p_end = p_cen + 1

print('Extraction: ', string1[p_ini:p_end])
