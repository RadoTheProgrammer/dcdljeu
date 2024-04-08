Un solveur du jeu Compte Est Bon et Mot Le Plus Long issu de Des Chiffres et Des Lettres.

Pour l'installer, exécutez simplement `pip install dcdljeu` sur le terminal

## Le Compte Est Bon

Le Compte Est Bon consiste à l'aide d'un tirage de nombres, d'essayer de reconstituer un nombre à chercher à l'aide d'opérations.

Pour utiliser le compte est bon, j'ai fait une fonction demo où vous n'aurez qu'à entrer le tirage de nombres et le nombre à rechercher (vous pouvez laisser vide pour le laisser générer un tirage):

```python

from dcdljeu import ceb
ceb.demo()
```

La fonction `ceb.generer()` permet de générer un tirage de nombres.

La fonction `ceb.solve` permet de résoudre le tirage, en affichant la progression, par example

```python

ceb.solve([9, 8, 25, 100, 5, 4],254)
```

retourne les solutions et les nombres trouvées.

## Le Mot le plus long

Cela consiste à trouver Le Mot Le Plus Long à partir de 10 lettres.

```python

from dcdljeu import mlpl
mlpl.demo()
```

## Projets sur scratch

Jetez aussi un coup d'oeil à mes projets scratch 

* jouer au [compte est bon](https://scratch.mit.edu/projects/529613029/)
* [au mot le plus long](https://scratch.mit.edu/projects/537035213/)
