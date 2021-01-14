Pour cette faille il faut exploiter la redirection vers les réseaux sociaux qui ce fait via la méthode GET.
Il faut donc copier le lien http://192.168.1.97/index.php?page=redirect&site=twitter
Et replacer le contenue du "site=" par un autre site voulu.
On pourrais donc exploiter cette faille pour rediriger vers un site de fishing qui copierais le vrai
site et qui serais accessible par le lien du site officiel.

Pour corriger ceci il faudrait verifier la requète GET.

flag : B9E775A0291FED784A2D9680FCFAD7EDD6B8CDF87648DA647AAF4BBA288BCAB3
