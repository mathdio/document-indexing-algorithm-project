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
    files_list = exists_word(word, instance)

    for index in range(len(files_list)):
        for n in range(len(instance)):
            file = instance.search(n)
            if file["nome_do_arquivo"] == files_list[index]["arquivo"]:
                for i in range(len(files_list[index]["ocorrencias"])):
                    file_lines = file["linhas_do_arquivo"]
                    line_number = files_list[index]["ocorrencias"][i]["linha"]
                    conteudo = file_lines[line_number - 1]
                    files_list[index]["ocorrencias"][i]["conteudo"] = conteudo
    return files_list
