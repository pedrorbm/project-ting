import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for i in range(len(instance)):
        if path_file == instance.search(i)["nome_do_arquivo"]:
            return None

    file = txt_importer(path_file)
    result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file
    }

    sys.stdout.write(f"{result}")
    instance.enqueue(result)

    return result


def remove(instance):
    if len(instance) == 0:
        return sys.stdout.write("Não há elementos\n")

    removed = instance.dequeue()
    nome_arquivo = removed["nome_do_arquivo"]
    return sys.stdout.write(f"Arquivo {nome_arquivo} removido com sucesso\n")


def file_metadata(instance, position):
    if not (0 <= position < len(instance)):
        return sys.stderr.write("Posição inválida\n")

    search = instance.search(position)
    return sys.stdout.write(f"{search}")
