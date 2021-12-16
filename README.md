<!-- Titre -->
<br />
<p align="center">
  <h3 align="center">La Nuit De L'Info 2021</h3>
</p>

![1er](https://github.com/RobinHCK/LaNuitDeLInfo2021/blob/main/media/1er.png)

<!-- Sommaire -->
## Sommaire

* [Contexte](#contexte)
  * [La nuit de l'info](#la-nuit-de-l-info)
  * [Le défi de la nuit](#le-defi-de-la-nuit)
  * [Le défi de l'AFIA](#le-defi-de-l-AFIA)
  * [L'équipe](#l-equipe)
* [Solution mise en oeuvre](#solution-mise-en-oeuvre)
  * [Prérequis](#prerequis)
  * [Technos](#technos)
  * [Réalisations](#realisations)
* [Résultat](#resultat)
* [Contacts](#contacts)

<!-- Contexte -->
## Contexte

### La nuit de l'info

*"La Nuit de l’Info (https://www.nuitdelinfo.com/) est une compétition nationale qui réunit étudiants, enseignants et entreprises pour travailler ensemble sur le développement d’une application web.
La Nuit se déroule tous les ans, du premier jeudi du mois de décembre, coucher du soleil, jusqu'au lever du soleil le lendemain matin.
Les participants ont la durée d'une nuit pour proposer, implémenter et packager une application Web 2.0."*, Extrait du site officiel.

### Le défi de la nuit

L’objectif de cette manifestation est de faire travailler ensemble les étudiants voulant participer à un défi informatique national : [Sujet 2021](https://github.com/RobinHCK/LaNuitDeLInfo2021/blob/main/media/sujet.pdf).

### Le défi de l'AFIA

*"Durant cette nuit, des partenaires lancent des défis (par exemple : interface web la plus ergonomique, meilleure architecture du système, meilleure collaboration etc) aux équipes participantes, et proposent des prix pour les équipes ayant le mieux réussi."*, Extrait du site officiel.

L’Association Française pour l’Intelligence Artificielle (AFIA http://www.afia.asso.fr) est la société savante consacrée à l'IA, qui fédère la communauté de l'IA francophone.

Son défi : *"Vous mettez en œuvre une ou plusieurs méthodes d'Intelligence Artificielle (IA) dans votre projet et vous indiquez en quoi ces méthodes rendent votre réalisation plus performante ou pertinente."*

### L'équipe

"Les Dodos Insomniaques" est constitué de Baptiste Lafabregue, Gautier Pialla et Robin Heckenauer.

<!-- Solution mise en oeuvre -->
## Solution mise en oeuvre

### Prérequis

Voir [requirements.txt](https://github.com/RobinHCK/LaNuitDeLInfo2021/blob/main/requirements.txt).

### Technos

- Le site est réalisé en Python à l'aide du framework Django (https://www.djangoproject.com/).
- La méthode proposée utilise Tesseract-OCR (https://github.com/tesseract-ocr/tesseract) et OpenCV (https://github.com/opencv/opencv).

### Réalisations

Le site web propose une interface qui permet :
- De déposer les documents tels que des photos (journaux, poèmes, archives etc).
- D’extraire le texte contenu dans les images déposées grâce à une méthode basée sur des transformations morphologiques et de l’OCR (Optical character recognition).
- D’afficher le document d'origine et le texte extrait.

<!-- Résultat -->
## Résultat

![classement](https://github.com/RobinHCK/LaNuitDeLInfo2021/blob/main/media/classement.png)

Extrait du compte-rendu du défi disponible dans le rapport de l'AFIA de Janvier 2022 (https://afia.asso.fr/les-bulletins/) : 

*"La première place a été attribuée à l’équipe "Les Dodos Insomniaques" qui se démarque clairement de toutes les soumissions au défi.

La solution proposée est parfaitement alignée sur les objectifs du sujet national (aider à la mise en ligne de contenu sur le site à partir de documents historiques orginaux).
L’équipe a proposé d’utiliser une technique d’IA pleinement appropriée (reconnaissance de caractères avec Tesseract) sur des documents réels récupérés sur le site de l’association à l’origine du sujet.
Les explications incluent les essais réalisés avec différents algorithmes et analysent les forces et faiblesses de leur solution, ainsi que les pré-traitements nécessaires, le code est fourni.

Le jury a considéré que cette soumission est exemplaire de l’objectif du défi."*

<!-- Contacts -->
## Contacts

Robin Heckenauer - robin.heckenauer@gmail.com
