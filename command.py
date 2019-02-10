import argparse
import os
import re
from MDtoHTML import convert, addTemplate

argpars = argparse.ArgumentParser()
argpars.add_argument('-i', '--input-directory',
                    help='Chemin du dossier contenant les fichiers markdown (.md)')
argpars.add_argument('-o', '--output-directory',
                    help="Chemin du dossier où seront mis les fichier générés")
argpars.add_argument('-t', '--template-directory',
                    help='Dossier contenant un template')
argpars.add_argument('-v', '--version', action='version',
                    version='%(prog)s 1.0')
arg = argpars.parse_args()

path = os.getcwd()
output = path
template = path

if argpars.output_directory:
    output = output + "\\" + argpars.output_directory

if argpars.template_directory:
    template = template + '\\' + argpars.template_directory
    addTemplate(template, output)
else:
    template = None

if argpars.input_directory:
    path = path + "\\" + argpars.input_directory

if not os.path.exists(output):
    os.makedirs(output)
    print('The directory {} has been created.'.format(args.output_directory))

try:
    file = os.listdir(path)
    for filename in file:
        if len(re.findall(r'.*\.md', filename)) > 0:
            convert(path, filename, output)
except:
    print("The directory '{}' doesn't exist.".format(args.input_directory))