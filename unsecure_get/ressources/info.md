Pour cette faille il faut exploiter la méthode GET utilisé par le site pour
ce déplacer de page en page
exemple sur la page survey : http://192.168.1.97/index.php?page=survey
c'est la partie après le "page=" qui nous intéresse, car c'est ici que l'on vas pouvoir naviguer dans les fichiers avec ce payload :
"../../../../../../../../../../../etc/passwd"
cette faille nous permet ici d'exploiter le fichier /etc/passwd mais il serais possible d'acceder a d'autre fichier important.

Pour corriger cette faille il faudrait verifier si les fichiers que l'ont essayer d'acceder sont bien limité à un dossiers (celui du site par exemple)

flag : b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0 