grâce au payload des failles sql précedente on peut lister ce tables :
ID: 1 UNION SELECT table_schema, table_name FROM information_schema.tables 
Title: db_default
Url : Member_Brute_Force

J'ai donc fais un script en python, a partir d'un dictionnaire de mdp.
Le script s'utilise en ligne, mais il est possible d'en faire un hors-ligne.
Dans mon cas le script aurait pu etre beaucoup plus court mais a cause de mon fournisseurs internet j'ai du prendre quelque precaution.

Pour eviter le bruteforce l'ideal serais d'encrypter les mdps avec une methode plus complexe (ici en md5),
mais aussi de demander a l'users des mdps plus complexe, et optionnelement rajouter un captcha a l'authentification pour eviter les gets via scripts

flag : B3A6E43DDF8B4BBB4125E5E7D23040433827759D4DE1C04EA63907479A80A6B2