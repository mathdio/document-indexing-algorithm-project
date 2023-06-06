from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    lines_file = txt_importer(path_file)

    for n in range(len(instance)):
        if instance.search(n)['nome_do_arquivo'] == path_file:
            return None

    dict_file = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines_file),
        "linhas_do_arquivo": lines_file,
    }

    instance.enqueue(dict_file)
    print(dict_file, file=sys.stdout)


def remove(instance):
    if len(instance) == 0:
        print('Não há elementos', file=sys.stdout)
    else:
        removed_dict = instance.dequeue()
        print((f"Arquivo {removed_dict['nome_do_arquivo']} "
               "removido com sucesso"), file=sys.stdout)


def file_metadata(instance, position):
    if not 0 <= position < len(instance):
        print('Posição inválida', file=sys.stderr)
    else:
        sys.stdout.write(f"{instance.search(position)}")
