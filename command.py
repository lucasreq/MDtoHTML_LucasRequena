import argparse
import os
import re
from MDtoHTML import convert, Template

argpars = argparse.ArgumentParser()
parser.add_argument('-i', '--input-directory',
                    help='Chemin du dossier contenant les fichiers markdown (.md)')
parser.add_argument('-o', '--output-directory',
                    help="Chemin du dossier où seront mis les fichier générés pour le site statique (Si le dossier n'existe pas il sera généré automatiquement)\nPar défaut le dossier et celui ou se trouve le fichier markdown")
parser.add_argument('-t', '--template-directory',
                    help='Dossier contenant un template (fichier CSS)')
parser.add_argument('-v', '--version', action='version',
                    version='%(prog)s 1.0')
arg = parser.parse_args()
