import os
from argparse import ArgumentParser

parser = ArgumentParser()

# Argumento Nome do projeto 
parser.add_argument('projectName', help="Digite o nome do projeto")

# Argumento path que recebe como parãmetro default a pasta em que o programa está sendo executado
parser.add_argument("--path", default="./".format(), help="Digite o caminho para a pasta que deseja que seja criada") 

#atribuição do objeto para a variável
args = parser.parse_args()

if args.path == "./": 
    path = "{}{}".format(args.path, args.projectName)
else: 
    path = args.path

os.mkdir(path) #criação da pasta

os.chdir(path) #muda o diretòrio
os.system("git init") #executa o git init

print("Projeto {} criado em {}".format(args.projectName, path))