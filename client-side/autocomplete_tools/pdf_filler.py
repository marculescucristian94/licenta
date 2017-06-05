import os, sys
import fdfgen

FDF_FILENAME = 'autocomplete_tools/fields.fdf'

# converts the data string to pair list 
def to_pair_list(data):
    pair_list = []
    pairs = data.split('|')
    for pair in pairs:
        if len(pair.split(':')) == 2:
		name, value = pair.split(':')
        	pair_list.append((name, value))
    return pair_list

def autocomplete_pdf(data, filepath):
	pair_list = to_pair_list(data)
	fdf_data = fdfgen.forge_fdf("", pair_list, [], [], [])
	fdf_file = open(FDF_FILENAME, "w")
	fdf_file.write(fdf_data)
	fdf_file.close()
	destination = '/'.join(str(filepath).split('/')[:-1]) + '/completed.pdf'
	print destination
	pdftk_cmd = "pdftk %s fill_form %s output %s flatten" % (filepath, FDF_FILENAME, destination)
	os.system(pdftk_cmd)
	os.remove(FDF_FILENAME)

