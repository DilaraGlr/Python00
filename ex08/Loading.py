import time
import os
import sys


def ft_tqdm(lst: range):
    """
    Simule la fonctionnalité d'une barre de progression (tqdm)
    utilisant un générateur (yield).
    """
    # 1. INITIALISATION
    total = len(lst)
    t_start = time.time()
    width = os.get_terminal_size().columns
    BAR_WIDTH = width - 20

    # 2. STRUCTURE DU GÉNÉRATEUR
    for i, elem in enumerate(lst):
        # 3a. Pourcentage
        p = ((i + 1) / total) * 100
        # 3b. Longueur de la barre
        filled_length = int(BAR_WIDTH * p / 100)
        filled_bar = ('=' * (filled_length - 1)) + '>'
        empty_bar = ' ' * (BAR_WIDTH - filled_length)
        bar_string = '[' + filled_bar + empty_bar + ']'

        # 3c. Temps écoulé et taux
        t_elapsed = time.time() - t_start
        # Gère le cas où t_elapsed serait 0 pour éviter la division par zéro.
        if t_elapsed == 0:
            rate = 0.0
            eta = 0.0
        else:
            rate = (i + 1) / t_elapsed
            eta = t_elapsed * ((total - (i + 1)) / (i + 1))

        # 4. AFFICHAGE DYNAMIQUE
        # Formatage des temps en minutes/secondes
        display_string = (
                    f"{p:5.1f}%|{bar_string}| {(i + 1)}/{total} "
                    f"[{int(t_elapsed)}s<{int(eta)}s, {rate:.2f}it/s]")
        # Le '\r' ramène le curseur au début de la ligne,
        # end='' empêche le saut de ligne.
        sys.stdout.write('\r' + display_string)
        sys.stdout.flush()

        # 5. GÉNÉRATION
        yield elem

    # 6. FINALISATION
    # Assurez-vous d'imprimer une dernière barre à 100% propre
    # Puis, sauter une ligne pour laisser le prompt du terminal revenir.
    final_string = (
        f"100.0%|{bar_string}| {total}/{total} "
        f"[{int(t_elapsed)}s<{int(eta)}s, {rate:.2f}it/s]"
    )
    sys.stdout.write('\r' + final_string + '\n')
    sys.stdout.flush()
