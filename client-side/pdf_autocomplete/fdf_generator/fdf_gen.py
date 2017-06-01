import os
import sys
import fdfgen
#Hard code or write code to retrieve fields names from Step 3 command
field_names = ["first name", "last name"] 
all_fields = []
#Prompt the user to provide values for the respective fields
for i in range(len(field_names)):
     field_value = raw_input(field_names[i] + ": ") 
     all_fields.append((field_names[i], field_value))
#Create FDF file with these fields
fdf_data = fdfgen.forge_fdf("", all_fields, [], [], [])
fdf_file = open("file_fdf.fdf","w") 
fdf_file.write(fdf_data) 
fdf_file.close()
#Run pdftk system command to populate the pdf file. The file "file_fdf.fdf" is pushed in to "input_pdf.pdf" thats generated as a new "output_pdf.pdf" file.
pdftk_cmd = "pdftk test_form.pdf fill_form file_fdf.fdf output output_pdf.pdf flatten"
os.system(pdftk_cmd)
#Remove the fdf file
##os.remove("file_fdf.fdf")
