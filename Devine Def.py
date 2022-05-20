import random
import time
dico = {
"Achaler" : "Contrarier quelqu'un",
"Acrimonie" : "mecontentement, amertume",
"Acrostiche" : "petit poeme dont les premieres lettres de chaque vers forment un nom, une devise...",
"Admonestation" : "réprimande",
"Affiquet" : "petit bijou que l'on fixe a une robe ou dans les cheveux",
"Agnelage" : "mise bas chez les brebis",
"Agoraphobie" : "crainte des espaces ouverts, des places publiques",
"Agueusie" : "perte du sens du gout",
"Alacrité" : "gaïté",
"Ambages" : "franchement. parler sans ambages équivaut à parler franchement",
"Amentif�re" : "Qui porte des inflorescences en chatons !!!",
"Amok" : "crise de folie homicide dont sont parfois frappés certains opiomanes malais",
"Anachor�te" : "Asc�te qui vit seul",
"Anacoluthe" : "Rutpure dans la construction de la phrase",
"Anaphore" : "Repetition d'un mot ou d'un groupe de mot en debut de phrases successives",
"Androcéphale" : "qui a une t�te humaine",
"Antonomase" : "emploi d'un nom commun ou d'une périphrase à la place d'un nom propre, ou inversement",
"Apagogie" : "Démonstration par l'absurde",
"Apophtegme" : "Maxime mémorable d'un illustre personnage",
"Aplacophore" : "classe de mollusques primitifs marins qui vivent dans la vase",
"Aporie" : "difficulté logique sans issue",
"arachibutyrophobie" : "Phobie d'avoir du beurre de cacahu�te collé sur le palais",
"Atermoiement" : "action d'hésiter, de remettre à plus tard (s'utilise au pluriel)",
"Aubier" : "partie du tronc qui se situe sous l'ecorce. Ce sont les couches de l'arbre les plus récemment formées",
"Avers" : "face d'une pièce ou d'une médaille, opposée au revers",
"Avunculaire" : "Qui se rapporte à l'oncle ou à la tante",
"Babiller" : "bavarder beaucoup, inutilement",
"Balanoglosse" : "Ver des plages",
"Bamboche" : "faire la fête, guincher (vieux language familier). On dit 'faire bamboche'",
"Barbon" : "vieillard desagreable ou ennuyeux",
"Biaural" : "qui concerne l'audition par les 2 oreilles",
"Billevesée" : "propos frivole",
"Bimane" : "qui a deux mains (l'homme est un animal bimane)",
"Bome" : "espar horizontal sur lequel est enverguee une voile aurique, au tiers ou triangulaire",
"Bonzesse" : "religieuse bouddhiste",
"Boustrophedon" : "ecriture alternée de gauche à droite puis de droite à gauche",
"Cacochyme" : "D'une santé déficiente",
"Callipyge" : "Dont les fesses sont belles (une vénus callipyge)",
"Calter" : "s'enfuir rapidement",
"Campaniforme" : "qui à la forme d'une cloche",
"Capitation" : "Taxe par tête. Abolie en 1789 !",
"Cathartique" : "Qui purifie, qui permet de purger",
"Cénobite" : "qui vit en communauté",
"C�notaphe" : "Tombeau élevé à la mémoire d'un mort mais qui ne contient pas son corps",
"C�phalalgie" : "Mal de tête",
"Ch�lit" : "Cadre de lit en bois ou en métal",
"Chattemite" : "Personne qui affecte des manières douces et modestes pour tromper son entourage",
"Charbonette" : "Bois d'un diamètre inférieur à 7 cm"

}
"""
"D�bagouler" : Vomir"
"D�cadique" : Nombre ayant une infinité de chiffres avant la sortie, et une infinit� de chiffres apr�s la virgule D�calvant : Qui rend chauve"
"D�caniller" : S'enfuir"
"D�citex" : Poids d'un fil exprimé en gramme pour 10 000 mètres de fil"
"D�goiser" : D�biter des paroles"
"D�l�t�re" : Qui met la sant� en danger"
"D�pr�dation" : Vol et pillage suivi de d�gradation"
"D�r�liction" : Etat de l'homme qui se sent abandonné, isolé, privé de tout secours divin"
"Dessiccateur" : Appareil servant à déshydrater une substance ou à tenir divers produits à l'abri de l'humidité"
"Diaphane" : Qui laisse passer les rayons lumineux sans permettre de distinguer les formes (translucide)"
"Diaphor�se" : Transpiration abondante"
"Dispendieux" : Qui exige une grande dépense"
"Distal" : Qui est le plus �loign� d'un point de r�f�rence d'une structure"
"Diverticule" : Cavit� en forme de poche (en m�decine, mais pas uniquement comme le diverticule axial de Lascaux)"
"Doxa" : Ensemble des opinions communément admises dans une société donnée"
"Drolatique" : Qui est récréatif et pytoresque"
"Ductile" : Qui peut être étendu, allongé, sans se briser"
"Dynamogénie" : Accroissement de la fonction d'un organe sous l'action d'une excitation"


  5. E

"Ebaubi : Extr�mement �tonn�
"Ebaudir : Egayer, r�jouir
"Eburn� : Qui � la couleur et la consistance de l'ivoire
"Echolalie : R�p�tition automatique des paroles de l'interlocuteur
"Ecornifler : Se procurer �� et l� aux d�pens d'autrui
"Egrotant : Souffrant
"Electronarcose : Court sommeil provoqu� par le passage d'un l�ger courant �lectrique � travers le cerveau
"Emblavure : Terre ensemenc�e en c�r�ale comme le bl�
"Emmouscailler : Emmerder
"Empeigne : Dessus d'une chaussure, du cou-de-pied jusqu'� la pointe
"Encoubler : Importuner, g�ner
"Enervation : Affaiblissement
"Ensiforme : En forme d'�p�e
"Ent�l�chie : Etat de perfection, de parfait accomplissement de l'�tre
"Entropie : Mesure math�matique de la quantit� d'incertitude et d'al�a
"Entropion : Renversement des paupi�res en dedans
"Epacte : Nombre qui exprime l'�ge de la lune au 31 d�cembre de chaque ann�e et qui indique combien il faut ajouter de jours � l'ann�e lunaire pour qu'elle "soit �gale � l'ann�e solaire
"Epanadiplose : Qui termine comme cela a commenc� (comme beaucoup de livres de Stephen King)
"Epectase : D�c�s pendant l'orgasme
"Epenth�se : Apparition � l'int�rieur d'un mot d'un phon�me non �thymologique
"Epithalame : Po�me compos� � l'occasion d'un mariage, en l'honneur des jeunes mari�s
"Equanamit� : Egalit� d'�me, d'humeur
"Ereuthophobie : Crainte, peur de rougir
"Exonder : Sortir au-dessus de l?eau, en parlant d?une terre ou d'organismes aquatiques ou amphibies


  6. F

"Faix : Charge tr�s pesante
"Falarique : Arme de jet incendiaire
"Faquin : Individu sans valeur, plat et impertinent
"Fat : Qui montre sa pr�tention de fa�on d�plaisante et quelque peu ridicule
"Fatrasie : Po�me du Moyen Age, d'un caract�re incoh�rent ou absurde, form� de dictons, proverbes, etc... mis bout � bout et contenant des allusions "satiriques
"F�bricule : Petite fi�vre
"Fjeld : Plateau rocheux us� par un glacier continental
"Fjord : Ancienne vall�e glaciaire envahie par les eaux marines durant la d�glaciation
"Flagorner : Flatter bassement, servilement
"Floculation : Rassemblement, sous forme de petits flocons, des particules d'une suspension collo�dale
"Foirade : Le fait de foirer, de rater
"Fondouk : Dans les pays arabes, emplacement du march�, ou auberge
"Forclore : Exclure, se faire priver du b�n�fice d'une facult� ou d'un droit non exerc� dans les d�lais fix�s
"Formication : Fourmillement, agitation
"Foucade : Caprice, emportement passager
"Foutriquet : Personnage insignifiant et incapable
"Fraichin : Odeur de mar�e
"Frontispice : Fa�ade principale d'un grand �difice
"Fulguration : Lueur �lectrique qui se produit dans les hautes r�gions de l'atmosph�re sans qu'on entende le tonnerre
"Fustet : Sumac � houppes plumeuses, dont le bois fourni une mati�re tinctoriale jaune


  7. G

"Gabarre : Embarcation pour le transport de marchandise
"Gadjo : Homme qui n'appartient pas � la communaut� des Gitans
"Galapiat : Polisson
"Gal�jade : Histoire invent�e ou plaisanterie destin�e � mystifier
"Galimafr�e : Plat peu app�tissant
"Galimatias : Discours confus et embrouill�
"Gambit : Manoeuvre aux echecs consistant � sacrifier une pi�ce pour se donner un avantage
"Garrocher : Lancer
"Girie : Plainte affect�e
"Glabelle : Partie l�g�rement pro�minente situ�e entre les 2 sourcils
"Glairer : Frotter de blanc d'oeuf la couverture d'un livre pour lui donner du lustre
"Glose : Annotation en marge d'un texte pour expliquer un mot difficile
"Godailler : Faire des faux plis sur les v�tements
"Gone : Jeune enfant
"Gonochorisme : S�paration compl�te des sexes dans des individus distincts
"Grandelet : Qui commence � devenir grand
"Grigne : Fente du boulanger faite sur le pain


  8. H

"Halieutique : Qui concerne la p�che
"Hapax : Mot, forme, emploi dont on ne peut relever qu'un exemple (� une �poque donn�e ou dans un corpus donn�)
"Haplologie : Fait de n'�noncer que l'une de deux articulations semblables et successives. (ex : tragicomique au lieu de tragico-comique)
"Haret : Chat domestique retourn� � l'�tat sauvage et vit du gibier
"H�ve : Affaibli par la faim, la fatigue ou la souffrance
"H�bertisme : M�thode d'�ducation physique qui consiste en exercices effectu�s en plein air
"Heimatlos : Qui a perdu sa nationalit� d'origine sans en acqu�rir de nouvelle
"Hell�nisation : Fait de donner un caract�re Grec � quelque chose (un pays, un peuple, un texte...)
"Hendiadys : Figure de rh�torique qui consiste � dissocier en deux noms coordonn�s une expression unique
"Hercher : Pousser les wagonnets de minerai au fond d'une mine
"H�ta�re : Prostitu�e d'un rang social �lev�
"Holisme : Th�orie selon laquelle l'homme est un tout indivisible qui ne peut �tre expliqu� par ses diff�rentes composantes
"Homoncule : Petit �tre vivant � forme humaine que les alchimistes pr�tendaient fabriquer
"Hourvari : Cri des chasseurs pour rappeller les chiens perdus de vue. Synonyme de Tapage
"Huis : Porte (d'o� '� huis clos')
"Hypallage : Figure de style qui consiste � attribuer � certains mots d'une phrase ce qui convient � d'autres mots de la m�me phrase
"Hyphe : Filament du myc�lium des champignons sup�rieurs
"Hypocondriaque : D'humeur triste et capricieuse
"Hypotypose : Description anim�e et frappante


  9. I

"Ichtyo�de : Qui ressemble � un poisson
"Impavide : Qui n'�prouve ou ne montre aucune peur
"Imp�ritie : Manque d'aptitude, d'habilet� notamment dans l'exercice de sa fonction
"Implexe : Dont l'intrigue est compliqu�e
"Inanit� : Inutilit�
"Incipit : Premiers mots d'un manuscrit, d'un livre
"Incube : D�mon masculin cens� abuser d'une femme pendant son sommeil
"Incunable : Ouvrage imprim� avant 1500
"Indig�te : Propre � un lieu, � une famille
"Ineffable : Qui ne peut-�tre exprim� par des paroles
"Infixe : El�ment qui s'ins�re dans l'int�rieur d'un mot afin d'en modifier le sens
"Infundibuliforme : Qui a la forme d'un entonnoir
"Interdigital : Situ� entre deux doigts
"Intertidal : Zone d'oscillation de la mar�e
"Irr�fragable : Qu'on ne peut contredire


  10. J

"Jactance : Vanit�
"Jaculatoire : Pri�re courte et fervente
"Jambor�e : R�union Internationale de scouts
"Jangada : Radeau de bois tr�s l�ger portant une cabane d'habitation utilis� par les p�cheurs br�siliens
"Janotisme : Construction maladroite d'une phrase entrainant une mauvaise interpr�tation (ex : c'est la voiture de ma grand-m�re qui est morte)
"Jectisse : Qui peuvent se poser � la main
"Jobastre : Imb�cile un peu fou


  11. K

"Kaolin : Silicate d'alumine pur provenant de l'alt�ration des feldspaths, des granits, argile qui compose les p�tes c�ramiques
"Kaon : Particule �l�mentaire dont la masse est 970 fois plus grande que celle de l'�lectron
"K�nophobie : Peur du noir
"Kraken : Monstre marin fabuleux des l�gendes scandinaves


  12. L

"Labile ; Peu stable, qui tombe facilement
"Lacunaire : Qui pr�sente des lacunes
"Lacustre : Qui vit pr�s d'un lac
"La�usser : Discourir
"Lallation : Emission de sons plus ou moins articul�s par l'enfant, avant l'acquisition du langage
"Latitudinaire : Qui a une morale tr�s large, tr�s rel�ch�e
"Latrie : Forme la plus �lev�e d'adoration qui ne doit �tre accord�e qu'� Dieu seul
"Laudatif : Qui contient un �loge
"Lavure : Liquide qui a servi � laver quelque chose ou quelqu'un
"L�ge : Vide ou incompl�tement charg�
"L�nitif : Adoucissant, apaisant
"L�pipodendron : Grand lycopode fossile arborescent de l'�re primaire
"Lerche : Pas beaucoup, peu, b�sef
"Leucotomie : Lobotomie partielle
"Levrett� : Qui a la taille svelte, le ventre creus� du l�vrier
"Lex�me : Morph�me lexical libre
"Lexis : Enonc� consid�r� ind�pendamment de sa v�rit�
"Li : Mesure chinoise (environ 576 mètres)
"Libelle : Court �crit de caract�re satirique, pamphlet
"Liminal : Qui est au niveau du seuil de perception (par opposition � subliminal)
"Lin�ature : Nombre de ligne d'une image compl�te
"Linge : Femelle du Lynx
"Liponombre : Nombre qui lorsqu'il est �crit en toute lettre, ne contient pas de 'e'
"Lipopremier : Liponombre qui est premier
"Liteau : Lieu o� le loup se repose pendant le jour
"Lotier : Herbe des pr�s et des talus
"Lucaniste : Amateur de cerfs-volants
"Lucre : Profit plus ou moins licite dont on est avide
"Lunisolaire : Qui a rapport � la fois � la Lune et au Soleil
"Lutrin : Pupitre sur lequel on met les livres de chant


  13. M

"Macache : Pas du tout, rien du tout
"Machure : Parties o� le poil n'a pas �t� coup� net, a �t� �cras�
"Mafflu : Qui a de grosse joue
"Maganer : Fatiguer, affaiblir
"Magyar : Qui a rapport au peuple �tabli au IXe si�cle dans l'actuelle Hongrie
"Ma�euticien : Homme qui exerce la profession de sage-femme
"Makimono : Peinture japonaise sur soie ou papier, beaucoup plus large que haute
"Maltose : Diholoside obtenu par action de l'amylase sur l'amidon
"Malt�te : Imp�t extraordinaire
"Mamelouk : Cavalier des anciennes milices �gyptiennes, garde du corps du sultan
"Mandala : Repr�sentation g�om�trique et symbolique de l'univers, dans le brahmanisme et le bouddhisme
"Manducation : Acte de manger
"Manuterge : Linge dont se sert le c�l�brant pour s'essuyer les mains au moment du lavabo pendant la messe
"Maringouin : Insecte dipt�re tel que le moustique, le cousin
"Maritorne : Femme laide, malpropre et d�sagr�able
"Mas : Maison de campagne ou ferme de Provence de style traditionnel
"Matefaim : Galette, cr�pe �paisse
"Matras : Gros trait d'arbal�te termin� par une t�te cylindrique ou quadrangulaire
"Maub�che : B�casseau de grande taille du nord de l'Europe
"Mazagran : Caf� chaud ou froid servi dans un verre
"Mazd�isme : Religion zoroastrienne de l'Iran antique encore pratiqu�e par les Gu�bres et les Parsis
"M�andrine : Madr�pore comprenant des polypiers vermicul�s dispos�s en rang�es sinueuses
"M�dianoche : Repas pris peu apr�s minuit
"M�dicastre : Mauvais m�decin, charlatan
"M�diocratie : Gouvernement, domination des m�diocres
"Mennonite : Membre d'un mouvement anabaptiste dans la premi�re moiti� du XVIe si�cle, aujourd'hui implant� aux pays-bas et aux Etats-Unis
"Mentisme : Fuite des id�es
"Menuise : Petit plomb de chasse
"M�phistoph�lique : Qui semble appartenir au d�mon M�phistoph�l�s
"M�phitique : Dont l'exhalaison est toxique et puante
"M�rostomes : Classe d'arthropodes dont la bouche s'ouvre entre les pattes
"Merzlota : Couche du sol et du sous-sol qui ne d�g�le jamais
"Meson : Hadron form� d'un quark et d'un antiquark
"M�tonymie : Figure de style qui consiste � utiliser un mot pour exprimer une id�e ou un autre concept. Par exemple, "boire un verre" qui exprime boire le contenu
"M�zigue : Synonyme de "Moi"
"Micheton : Client d'un ou d'une prostitu�
"Mignoter : Traiter d�licatement, avec gentillesse
"Milliaire : Qui marque la distance d'un mille romain
"Mimivirus : Virus g�ant � ADN de la taille d'une petite bact�rie
"Mirliflore : Jeune pr�tentieux
"Misandre : Qui a de la haine ou du m�pris pour les hommes (oppos� de Misogyne)
"Misantrhope : Personne qui manifeste de l'aversion pour ses semblables
"Misogyne : Qui a de la haine et du m�pris pour les femmes (oppos� de Misandre)
"Miston : Gamin, gamine
"Mistoufle : M�chancet�, vilainie
"Mithridatiser : Immuniser en accoutumant � un poison
"Mod�nature : Profil des moulures en architecture
"Moere : Lagune d'eau douce combl�e, ass�ch�e puis mise en culture
"Monaural : Relatif � une seule oreille
"Monergol : Produit apte � la propulsion d'un moteur de fus�e
"Monition : Avertissement donn� par l'autorit� eccl�siastique avant d'adresser une censure
"Monoecie : Etat d'une plante mono�que
"Monstration : Action de montrer
"Monte-en-l'air : Voleur, cambrioleur
"Mornifle : Baffe, gifle
"Moujingue : Enfant plut�t difficile
"Muance : Dans la solmisation, substitution d'un hexacorde � un autre
"Musarder : Perdre son temps, fl�ner
"Mutule : Ornement d'un entablement dorique qui est plac� sous la larmier en face du triglyphe


  14. N

"Nadir : Point de la sph�re c�leste diam�tralement oppos� au z�nith et qui se trouve sur la verticale de l'observateur
"Naissain : Embryons ou larves des huitres et moules d'�levage
"Nanan : Bonbons, friandises. C'est du Nanan signifie que c'est tr�s facile
"Nasarde : Pichenette sur le nez
"N�oblaste : Cellule indiff�renci�e qui assure la reconstitution des parties accidentellement amput�es chez certains animaux
"Nervation : Disposition des nervures d'une feuille ou des ailes d'un insecte
"Nervi : Tueur, homme de main
"Nib : Synonyme de Rien
"Nicod�me : Nigaud
"Nif� : Noyau de la Terre qui serait consitu� de Nickel et de Fer
"Nitescence : Lueur, rayonnement
"Noctiluque : Qui peut �mettre une lueur dans l'obscurit�
"Notule : Petite annotation � un texte
"Nubile : Qui a atteint l'�ge de se marrier


  15. O

"Objectivation : Rendre objectif
"Objurgation : Reproche, r�primande
"Obvie : Evident, logique
"Oekoum�ne : Espace habitable de la surface terrestre
"Onagre : Ane sauvage de grande taille
"Onques : Jamais
"Onguicul� : Qui a un ongle � chaque doigt
"Onychophagie : Habitude de se ronger les ongles
"Ophiol�trie : Adoration du serpent
"Opimes : Riches d�pouilles ou riche profit
"Opprobre : Qui humilie, qui d�shonore
"Oraliser : Lire ou r�citer � haute voix un texte
"Orant : Personnage repr�sent� en pri�re, dans l'art chr�tien ancien
"Orbicole : Qui se trouve sur tous les points du globe
"Orbit�le : Araign�e qui tisse un toile polygonale � sym�trie centrale"
"Or�ade : Nymphe des montagnes et des bois
"Organsiner : Tordre les fils de soie pour en obtenir l'organsin
"Orillon : Partie d'un objet en forme de petite oreille
"Oronymie : Etude toponymique des noms des montagne
"Ouananich : Saumon d'eau douce p�ch� au Canada
"Oukase : D�cision arbitraire, historiquement, �dit promulgu� par le tsar
"Ovalie : Ensemble des r�gions du globe o� l'on joue au rugby


  16. P

"Pacage : Terrain o� vont pa�tre les bestiaux
"Pageot : Lit
"Pairle : Meuble en forme d'Y dontl es branches atteignent les angles sup�rieurs de l'�cu
"Palestre : Dans l'antiquit�, lieu public o� l'on s'exercait � la lutte et � la gymnastique
"Palisson : Instrument de fer qui sert � chamoiser
"Palsambleu : Juron utilis� au XVII
"Paltoquet : Homme insignifiant et pr�tentieux
"Palustre : Qui se rapporte au marais
"Pandiculation : Mouvement qui consiste � �tendre les bras et les jambes tout en se penchant en arri�re. Le fait de s'�tirer
"Panifiable : Qui peut servir comme mati�re premi�re dans la fabrication du pain
"Panspermie : Th�orie selon laquelle la vie sur Terre est issue de germes venus d'ailleurs...
"Parangon : Mod�le
"Paratexte : Ensemble form� par le p�ritexte et l'�pitexte
"Par�miologie : Etude des proverbes
"Paronyme : Se dit de mots presque homonymes et qui peuvent facilement �tre confondus
"Parturition : Accouchement
"Pasquin : Bouffon
"Patouillard : Navire lent, lourd et plut�t en mauvais �tat
"Pattinsonage : Mode de traitement des plombs argentif�res par cristallisation fractionn�e, pour s�parer l'argent du plomb
"P�dieux : Qui a rapport ou appartient au pied
"P�guer : Coller, enduire d'une substance visqueuse ou collante
"Pellucide : Zone translucide
"Pendeloque : Bijou suspendu � une boucle d'oreille
"P�ripat�ticien : Partisan de la doctrine d'Aristote
"P�rissodactyles : Ordre de mammif�res placentaires ongul�s qui comprend des animaux reposant sur le sol par un nombre impair de doigts dont le m�dian est le plus d�velopp�
"P�rissologie : Pl�onasme fautif (comme "descendre en bas")
"P�ronnelle : Jeune femme ou jeune fille sotte et bavarde
"Petiole : Nom de la tige reliant la feuille au rameau
"P�trarquiser : Aimer platoniquement, comme P�trarque aimait Laure
"P�tulance : Ardeur exub�rante, brusque et d�sordonn�e
"P�tuner : Fumer du tabac
"Phatique : Fonction du langage utilis� pour �tablir une communication sans apport d'information ("allo", "bonjour"...)
"Ph�nakistiscope : Appareil form� de deux disques qui donne l'illusion du mouvement par lapersistance des images r�tiniennes
"Photop�riode : R�partition dans la journ�e entre la dur�e de la phase diurne et celle de la phase obscure
"Phylarque : Pr�sident d'une tribu � Ath�nes
"Phyllotaxie : Positionnement des feuilles d'arbres sur un rameau
"Piaculaire : Relatif � une expiation
"Piauler : Crier en pleurnichant
"Pica : Go�t morbide pour des substances non comestibles
"Pi�taille : Petit, subalterne
"Pioupiou : Jeune fantassin
"Placoter : Bavarder
"Plurivoque : Qui a plusieurs valeurs
"Pollicitation : Offre exprim�e mais non encore accept�e
"Porchaison : Saison pendant laquelle le sanglier est le plus gras
:


  17. Q

:


  18. R

:


  19. S

"Satyriasis : Comportement de l'homme cherchant en permanence le plaisir sexuel. Equivalent � la nymphomanie chez la femme.
"Sphinge : Sphinx � buste de femme
"Succube : D�mon f�minin qui abuse d'un homme pendant son sommeil


  20. T

"Tautologie : Phrase toujours vraie, mais pr�sent�e de mani�re diff�rente
"T�traktys : 10 points rang�s en 4 rang�s (1 puis 2, puis 3, puis 4) repr�sentant un triangle, �galement appel� d�cade
"Triskaidekaphobie : Phobie du nombre 13, et en particulier du Vendredi 13
"Tuple : Enregistrement d'une base de donn�es
"Valetudinaire : Maladif, fébrile



"""
##CODE

wordList=[]
messageSasir="Saisir Votre réponse "
for key in dico:
    wordList.append(key)

##VISUEL

def AfficheMenu():

    print("------------------------------")
    print("|       BATAILLE NAVALE      |")
    print("------------------------------")
    print("\n\n")
    print("       -------------          ")
    print("       | solo -> 1 |          ")
    print("       -------------        \n")
    print("      ----------------         ")
    print("      |   multi -> 2 |         ")
    print("      ----------------        \n")
    print("      ----------------          ")
    print("      | quitter -> 0 |         ")
    print("      ----------------          \n")

def jeu():
    AfficheMenu()
    Menu()

def Menu():
    choix = 0
    while choix != -12:
        choix = int(input("--> " ))
        if choix == 1 : # Solo
            PlaySolo()
            AfficheMenu()

        elif choix == 2: # Multi
            PlayMulti()
            AfficheMenu()

        elif choix == 0: #quitter
            return "quitter"

def AfficheQuestion(nb,wordId,mot):
    NettoieEcran()
    print(wordList[wordId[mot]],':')
    for i in range(0,nb):
        print("\n            \033[1;30;40m"+str(i+1)+".",dico[wordList[wordId[i]]])
        #print(wordList[wordId[i]])
    print("")

def AfficheCorrection(nb,wordId,mot):
    NettoieEcran()
    print("\033[1;32;40m"+wordList[wordId[mot]]+':')
    for i in range(0,nb):
        if i == mot:
            print("\n            \033[1;32;40m"+str(i+1)+".\033[1;30;40m",dico[wordList[wordId[i]]],"-->\033[1;32;40m",wordList[wordId[i]],"\033[1;30;40m")
        else:
            print("\n            \033[1;30;40m"+str(i+1)+".",dico[wordList[wordId[i]]],"-->\033[1;31;40m",wordList[wordId[i]],"\033[1;30;40m")
    print("")
##CODE
"""
    NB:
    wordId[i] -> ID du mot
    wordList[wordId[i]] -> Mot
    dico[wordList[wordId[i]]] -> Def du mot

"""


def PlaySolo():
    NettoieEcran()

def NettoieEcran():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\033[1;30;40m")




def PlayMulti():
    pass

def PlaySolo():
    nbGame=10
    for i in range (nbGame):
        Partie()

def Partie(difficulty=5):
    difficulty=4
    wordId=[]
    for i in range (difficulty):
        wordId.append(random.randint(0,len(dico)-1))
        #GENERER JUSQU'A QU'ILS SOIENT TOUS DIFFERENTS
    #print(wordId)
    idCorrect=random.randint(0,difficulty-1) # ID CORRECT DANS wordID !!
    #print(idCorrect)
    AfficheQuestion(difficulty,wordId,idCorrect)
    rep=PoseQuestion()
    if rep-1 == idCorrect:
        AfficheCorrection(difficulty,wordId,idCorrect)
        print(messageSasir+str(idCorrect+1))
        print("bien joué!")
    else:
        AfficheCorrection(difficulty,wordId,idCorrect)
        print(messageSasir+str(rep),"\033[1;31;40mX\033[1;30;40m")
        print("perdu! la bonne réponse était \033[1;32;40m",idCorrect+1)
    time.sleep(5)

def PoseQuestion():
    rep=''
    while rep == '':
        rep=int(input(messageSasir))
    return rep



#jeu()
PlaySolo()




