Pour cette faille il suffit d'inspecter l'élément dans la page survey.
La faille ce situe dans les values des "option" de "select".
Il faut modifier une des value avec l'int max (2147483647) puis ensuite 
selectionner l'option qui correspond a celle qu'on a modifier.

Une sécurité dans le backend pourrais corriger cette faille


flag : 03A944B434D5BAFF05F46C4BEDE5792551A2595574BCAFC9A6E25F67C382CCAA