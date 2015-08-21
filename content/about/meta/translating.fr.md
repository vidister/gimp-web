Title: Translations (i18n)
Date: 2015-08-21T11:45:47-05:00
Author: Pat David
lang: fr 

Pelican avait déjà une belle simple support pour la traduction des pages et des articles.

Pour faire une traduction, il suffit de créer un autre fichier avec le fichier de base. Tant que le *slug* serait le même, un fichier serait considérée comme une traduction de l'autre. Définition de l'attribut `lang` dans les métadonnées du fichier signalerait ce type de fichier, il est.
<small>
La limace est actuellement généré à partir du titre de la page dans les métadonnées.
</small>

A titre d'exemple, ce fichier est:

    content/about/meta/translating.md

Et les métadonnées au sommet de ce fichier ressemble à ceci:

    Title: Translations (i18n)
    Date: 2015-08-21T11:45:47-05:00
    Author: Pat David
    lang: en

Pour créer une version traduite de cette page, nous aimerions créer un nouveau fichier:

    content/about/meta/translating.fr.md

Les métadonnées serait un peu différente, en ce que l'attribut `lang` serait différent maintenant:


    Title: Translations (i18n)
    Date: 2015-08-21T11:45:47-05:00
    Author: Pat David
    lang: fr

Sinon tout le reste pourrait rester le même.

En faisant cela, Pelican va maintenant automatiquement la liste de la traduction (s) étant disponible (par défaut il est répertorié juste sous le titre). Il serait généralement ressembler à ceci (pour une traduction française étant disponibles):

    Translations: fr


## i18n_subsites

Avec la mise en œuvre de i18n_subsites, le comportement est essentiellement le même.

La différence est maintenant que d'un sous-site entièrement nouveau est construit. Le site avec les anciennes traductions servirait une page traduite, mais ce serait une page statique simple.

Cela signifie que tous les liens hors de la page à d'autres contenus souhaitez-vous apporter à la langue par défaut (en) à nouveau. Si cette page avait une traduction, et que vous vouliez le voir, vous devez cliquer sur l'option de traduction appropriée nouveau.

L'option de traduction d'une seule page ne dispose d'aucun mécanisme pour traduire les modèles aussi bien (juste le contenu de la page).

Mise en œuvre du plugin i18n_subsites permet désormais un sous-ensemble du site qui sera construit sur la base de l'option de langue. Donc, en cliquant sur une traduction de langue pour une page va maintenant mettre l'utilisateur au sous-site correspondant.

Ce sont les sous-sites qui se créés par exemple:

    gimp.org/fr/about/...
    gimp.org/de/about/...

Et ainsi de suite pour chaque traduction.


### Fallback

Une fonctionnalité intéressante du plugin i18n_subsites est que les pages qui sont liées, mais le manque d'une traduction, seront toujours montrer la version **en** comme solution de repli.
