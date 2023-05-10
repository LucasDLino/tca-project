import os
import sys

# get the directory containing the script
script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

for file_name in os.listdir(script_dir):
    if file_name.endswith('.svg'):
        file_path = os.path.abspath(file_name)
        pdf_path = os.path.splitext(file_path)[0] + '.pdf'
        os.system(f'inkscape "{file_path}" --export-type=pdf --export-filename="{pdf_path}"')

        
