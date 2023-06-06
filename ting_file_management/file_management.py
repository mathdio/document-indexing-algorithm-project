import sys


def txt_importer(path_file):
    if not path_file.endswith('.txt'):
        return print('Formato inválido', file=sys.stderr)

    else:
        try:
            with open(path_file, 'r') as file:
                return [line[:-1]
                        if line.endswith('\n')
                        else line
                        for line in file]

        except FileNotFoundError:
            print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
