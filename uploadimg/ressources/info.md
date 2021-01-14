Cette faille repose sur l'upload d'image, il suffit de créer un script en php, de l'uploader,
puis avec le logiciel burpsuite en mode intercept il faut changer le MIME type du fichier en "image/jpeg"
Il serais donc possible d'executer n'importe qu'elle script par la suite.

Pour corriger cette faille il faudrait verifier la validiter de l'image via sa taille, ou un package d'un langage prevue à cette effet.

flag : 46910D9CE35B385885A9F7E2B336249D622F29B267A1771FBACF52133BEDDBA8