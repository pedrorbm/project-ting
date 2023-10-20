def exists_word(word, instance):
    result = []

    for i in range(len(instance)):
        archive = instance.search(i)
        word_true = []

        for index, search_word in enumerate(archive["linhas_do_arquivo"], 1):
            word_lower = word.lower()
            search_word_lower = search_word.lower()

            if word_lower in search_word_lower:
                word_true.append({"linha": index})

        if len(word_true) > 0:
            result.append(
                {
                    "palavra": word,
                    "arquivo": archive["nome_do_arquivo"],
                    "ocorrencias": word_true,
                }
            )
        else:
            return []

    return result


def search_by_word(word, instance):
    result = []

    for i in range(len(instance)):
        archive = instance.search(i)
        word_true = []

        for index, search_word in enumerate(archive["linhas_do_arquivo"], 1):
            word_lower = word.lower()
            search_word_lower = search_word.lower()

            if word_lower in search_word_lower:
                word_true.append({"linha": index, "conteudo": search_word})

        if len(word_true) > 0:
            result.append(
                {
                    "palavra": word,
                    "arquivo": archive["nome_do_arquivo"],
                    "ocorrencias": word_true,
                }
            )
        else:
            return []

    return result
