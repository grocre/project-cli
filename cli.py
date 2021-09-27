from argparse import ArgumentParser



parse = ArgumentParser()

parse.add_argument('projectName', help="Digite o nome do projeto")

args = parse.parse_args()


print("Projeto {} criado".format(args.projectName))