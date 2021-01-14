Grace au fichier robots.txt on peut voir les fichiers cachés du site.
Celui qui nous intéresse c'est le fichier "whatever"
une fois dedans on recupere le fichier "htpasswd" qui a le contenu suivant :
"root:8621ffdbc5698829397d97767ac13db3"
En cherchant un peux on constate que le mot de pass est encrypter en md5.
Le résultat du pass décrypter est : "dragon"
On peut donc maintenant acceder à la partie Admin avec ces ids.

Il ne faut pas utilisé le fichiers robots.txt pour empecher l'acces au pages sensibles

flag : d19b4823e0d5600ceed56d5e896ef328d7a2b9e7ac7e80f4fcdb9b10bcb3e7ff
