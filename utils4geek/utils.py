def convert_request_to_str(data):
    """
    Retorna el str de los parametros enviados desde
    la petición HTTP. admite string, int y listas de string o list.
    no admite jsons anidados.

    :param data: los datos del request
    :return: el string resultante
    """
    list_tuple = data.items()
    ordered_list_tuple = sorted(list_tuple, key=lambda x: x[0])
    final_list = []
    for key, value in ordered_list_tuple:
        if isinstance(value, list):
            result_list = sorted(map(str, value))
            value = ",".join(result_list)

        final_list.append("{0}={1}".format(key, value))
    str_final = "&".join(final_list)
    return str_final