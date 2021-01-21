Pour cette faille il faut utiliser l'outil inspecter -> Applications (de google chrome dans mon cas)
On peut voir qu'il y à un cookie de sessions nommée : I_am_admin
ça valeur correspond à false hasher en md5
Je hash donc "true" en md5 -> b326b5062b2f0e69046810717534cb09
et je change sa valeur!
Une fois la page actualiser on obtiens le flag

L'idéal pour le cookie admin sérait de le rendre plus "random" et d'utiliser une methode hashage plus complexe

flag : df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3