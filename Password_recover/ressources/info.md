Pour cette faille il faut aller dans la partie "recover password",
puis inspecter l'élément sur le bouton submit, on voit qu'il y a une adresse écrit en brut dans value de la balise input. Il faut changer cette adresse email par une autre puis cliquer sur submit.

Il faudrait ne pas mettre d'adresse mail en front et laisser une textbox pour rentrer son adress email et ajouter des sécurité en back si nécessaire.

flag : 1D4855F7337C0C14B6F44946872C4EB33853F40B2D54393FBE94F49F1E19BBB0