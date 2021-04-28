"""
    Fichier : gestion_genres_wtf_forms.py
    Auteur : OM 2021.03.22
    Gestion des formulaires avec WTF
"""
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SubmitField
from wtforms.validators import Length
from wtforms.validators import Regexp


class FormWTFAjouterCollaborateur(FlaskForm):
    """
        Dans le formulaire "genres_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_utilisateur_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    nom_utilisateur_wtf = StringField("Clavioter le nom utilisateur ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                   Regexp(nom_utilisateur_regexp,
                                                                          message="Pas de chiffres, de caractères "
                                                                                  "spéciaux, "
                                                                                  "d'espace à double, de double "
                                                                                  "apostrophe, de double trait union")
                                                                   ])
    courriel_regexp = "^\ b [ A - Z 0 - 9 ._% + - ]+ @ [ A - Z 0 - 9 . - ] + \. [ A - Z ] {2,4} \ b"
    courriel_wtf = StringField("Taper l'adresse email ",
                             validators=[Length(min=2, max=20, message="min 2 max 20"),
                                         Regexp(courriel_regexp,
                                                message="Pas de chiffres, de caractères "
                                                        "spéciaux, "
                                                        "d'espace à double, de double "
                                                        "apostrophe, de double trait union")
                                         ])
    submit = SubmitField("Enregistrer identification")


class FormWTFUpdateIdentification(FlaskForm):
    """
        Dans le formulaire "genre_update_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_utilisateur_identification_update_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    nom_utilisateur_identification_update_wtf = StringField("Nom d'utilisateur ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                          Regexp(nom_utilisateur_identification_update_regexp,
                                                                                 message="Pas de chiffres, de "
                                                                                         "caractères "
                                                                                         "spéciaux, "
                                                                                         "d'espace à double, de double "
                                                                                         "apostrophe, de double trait "
                                                                                         "union")
                                                                          ])
    courriel_identification_update_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    courriel_identification_update_wtf = StringField("Courriel ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                          Regexp(courriel_identification_update_regexp,
                                                                                 message="Pas de chiffres, de "
                                                                                         "caractères "
                                                                                         "spéciaux, "
                                                                                         "d'espace à double, de double "
                                                                                         "apostrophe, de double trait "
                                                                                         "union")
                                                                          ])
    submit = SubmitField("Update genre")


class FormWTFDeleteGenre(FlaskForm):
    """
        Dans le formulaire "genre_delete_wtf.html"

        nom_collaborateur_delete_wtf : Champ qui reçoit la valeur du genre, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "genre".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_genre".
    """
    nom_collaborateur_delete_wtf = StringField("Effacer ce collaborateur")
    prenom_collaborateur_delete_wtf = StringField("")
    submit_btn_del = SubmitField("Effacer genre")
    submit_btn_conf_del = SubmitField("Etes-vous sur d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")
