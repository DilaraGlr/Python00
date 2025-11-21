def ft_filter(fonction, iterable):
    """Filtre les éléments de l'itérable pour lesquels la fonction
    retourne True."""
    return [element for element in iterable if fonction(element)]
