Dans le champs de texte name de la page feedback le texte n'est pas échappé, il est donc possible
de faire une attaque XSS

exemple : <script>alert(1)</script>
(dans ce cas précis "script" suffira à dévoilé la faille)

Pour éviter cette faille il suffirais de vérifié le text avant de l'afficher et de le nettoyer.

flag : 0FBB54BBF7D099713CA4BE297E1BC7DA0173D8B3C21C1811B916A3A86652724E