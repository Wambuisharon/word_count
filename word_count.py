def words(input):
	data = input.split()

	data_dict ={}

	unique_values = set(data)
	for word in unique_values:
	  count = 0
	  for real_word in data:
	    if real_word  == word:
	      count = count + 1
	      
	  data_dict[word] = count
	return data_dict



