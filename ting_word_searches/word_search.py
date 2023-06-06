def exists_word(word, instance):
    files_list = []

    for index in range(len(instance)):
        file = instance.search(index)
        file_dict = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": [],
        }

        for n in range(len(file["linhas_do_arquivo"])):
            if file["linhas_do_arquivo"][n].lower().find(word.lower()) > -1:
                file_dict["ocorrencias"].append({"linha": n + 1})

        if len(file_dict["ocorrencias"]) > 0:
            files_list.append(file_dict)

    return files_list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""


print("teste".find("a"))
