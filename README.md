# Beyond The Shadows

*Beyond the Shadows* est un jeu de plateau dans lequel le joueur incarne le fantôme d'un héros légendaire cherchant à retrouver son corps. Pour y parvenir, il doit affronter et vaincre des monstres qui menacent de le faire disparaitre à tout jamais. Développé en Python à l'aide du module *Pygame*, le jeu mêle exploration combats et quêtes, offrant ainsi une expérience immersive où le joueur devra naviguer à travers le monde et surmonter divers obstacles avec l'aide de différents personnages pour accomplir son objectif.

## Fonctionnalités
- **Carte du monde** : Le jeu se déroule dans un monde composé de plusieurs régions à explorer
- **Personnages** : Plusieurs personnages non-jouables avec lesquels intéragir
- **Trésors** : Plusieurs objets à retrouver pour progresser 
- **Progression du joueur** : Parlez à la bonne personne pour améliorer votre équipement 
- **Monstres** : Survivez face aux différents monstres qui habitent les différentes régions

## :white_check_mark: Installation

Pour démarrer avec *Beyond the Shadows*, suivez les étapes suivantes :

- Décompresser le fichier `Beyond_the_Shadows.zip`

- Installer les dépendances :
```bash
pip install -r requirements.txt
```

- Lancer le jeu :

```bash
python Beyond_the_Shadows/code/main.py
```



## Structure du projet
```bash
beyond_the_shadows/
├── code/               #Dossier qui contient tout les codes pythons dont main.py
│   ├── main.py         #code python qui lance le jeu
└── media/              #Dossier qui contient tout le pixel art du jeu
    ├── Armes/   
    ├── font/
    ├── items/
    ├── Joueur_Animations/
    ├── map/            #les tiles de la map
    ├── menu/           #le menu au début du jeu
    ├── monstres/       #entités
    ├── npc/            #les personnages non jouables
    ├── objets/         #coffres, pierres
    ├── Particules/     #magie
    ├── son/            #musique, sons
    └── UI/             #inventaire, barre de vie / mana

```


## Comment jouer ?

- :runner: **Mouvements :** Utilisez les flèches :arrow_left:, :arrow_right:, :arrow_up:, :arrow_down: ou `W`,`A`,`S`,`D` pour déplacer le personnage.
- :anger: **Combat :** `Espace` pour attaquer, `Q` pour changer d'arme
- **Interactions :** Appuyez sur `E` pour interagir avec un personnage ou un objet.


## Crédits

- :space_invader: **Développement du jeu** : Lino Cupaiolo, Michel El Beik, Ange Pham, Matteo Zins
- :tv: **Ressources graphiques** : [Zaebucca](https://zaebucca.itch.io/adventure-begins)
- :sound: **Son/Musique** :musical_keyboard: : Ange Pham, Lino Cupaiolo

## Licence

*Beyond the Shadows* est open source et disponible sous la GPL v3.
Ce projet est sous licence libre. Vous êtes libre de le modifier et de le partager tout en mentionnant les auteurs d'origine.

