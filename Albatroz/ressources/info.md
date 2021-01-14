Pour cette faille il faut inspecter l'élément sur la page "BornToSec" (avec la photo de l'albatros)
On pourra trouver plusieurs indices dans les commentaires de la page.
Après quelques recherche on en viens a une commande dans cette esprit :
curl -s -A 'ft_bornToSec' --referer "https://www.nsa.gov/" "http://192.168.1.97/?page=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c" | grep flag



flag : f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188