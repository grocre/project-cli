import os
from argparse import ArgumentParser


parser = ArgumentParser()

parser.add_argument('projectName', help="Digite o nome do projeto")

parser.add_argument("--path", default="./".format(), help="Digite o caminho para a pasta que deseja que seja criada") # resolver isso


args = parser.parse_args()

if args.path == "./": 
    path = "{}{}".format(args.path, args.projectName)
else: 
    path = args.path

os.mkdir(path)

print("Projeto {} criado em {}".format(args.projectName, path))