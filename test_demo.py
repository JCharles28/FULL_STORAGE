# Importation des modules nécessaires
from track import *
import tempfile
import cv2
import torch
import streamlit as st
import os

# Vérification de l'execution du script
if __name__ == '__main__':
    # Script CSS
    css = """
    <style>
  @import url('https://fonts.googleapis.com/css2?family=Quicksand&display=swap');
    
    * {
        font-family: 'Quicksand', sans-serif;
    }
    
    .animation:hover {
        font-weight: 800;
        transition: font-weight 1s;
    }
    
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)
    # Titre de l'application
    st.title('Smart Traffic')
    st.markdown('<h3 style="color: red">Powered by Evolukid & Orange </h3', unsafe_allow_html=True)

    # Téléchargement de la vidéo
    video = st.sidebar.file_uploader("Télécharger une vidéo de traffic routier au choix !", type=['mp4', 'mov', 'avi'])

    if video:
        st.sidebar.text('Vidéo d\'entrée')
        st.sidebar.video(video)
        # Sauvegarde de la vidéo
        with open(os.path.join('videos', video.name), 'wb') as fichier:
            fichier.write(video.getbuffer())

    st.sidebar.markdown('---')
    st.sidebar.title('Paramètres')
    # Classe personnalisée
    classe_perso = st.sidebar.checkbox('Classes personnalisées')
    id_classe = [0, 1, 2, 3]
    noms = ['voiture', 'moto', 'camion', 'bus']

    if classe_perso:
        id_classe = []
        selection = st.sidebar.multiselect('Sélectionner les classes personnalisées', list(noms))
        for elem in selection:
            id_classe.append(noms.index(elem))
    
    # Réglage des hyperparamètres
    confiance = st.sidebar.slider('Taux de confiance', min_value=0.1, max_value=1.0, value=0.5)
    ligne = st.sidebar.number_input('Position de la ligne', min_value=0.0, max_value=1.0, value=0.6, step=0.1)
    st.sidebar.markdown('---')

    # État et vidéo
    etat = st.empty()
    cadre = st.empty()
    if video is None:
        etat.markdown('<font size= "4"> **État:** En attente d\'entrée </font>', unsafe_allow_html=True)
    else:
        etat.markdown('<font size= "4"> **État:** Prêt </font>', unsafe_allow_html=True)

    # Compteurs
    voiture, bus, camion, moto = st.columns(4)
    with voiture:
        st.markdown('<span class="animation">**Voiture**</span>', unsafe_allow_html=True)
        texte_voiture = st.markdown('__')
    
    with bus:
        st.markdown('**Bus**')
        texte_bus = st.markdown('__')

    with camion:
        st.markdown('**Camion**')
        texte_camion = st.markdown('__')
    
    with moto:
        st.markdown('**Moto**')
        texte_moto = st.markdown('__')

    # FPS
    fps_col, _,  _, _  = st.columns(4)
    with fps_col:
        st.markdown('**FPS**')
        texte_fps = st.markdown('__')

    # Bouton de suivi
    bouton_suivi = st.sidebar.button('DÉMARRER')
    if bouton_suivi:
        reset()
        opt = parse_opt()
        opt.conf_thres = confiance
        opt.source = f'videos/{video.name}'

        etat.markdown('<font size= "4"> **État:** En cours d\'exécution... </font>', unsafe_allow_html=True)
        with torch.no_grad():
            detect(opt, cadre, texte_voiture, texte_bus, texte_camion, texte_moto, ligne, texte_fps, id_classe)
        etat.markdown('<font size= "4"> **État:** Terminé ! </font>', unsafe_allow_html=True)
