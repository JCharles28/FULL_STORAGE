# Importation des modules nécessaires
from track import *
import tempfile
import cv2
import torch
import streamlit as st
import os

# Vérification de l'execution du script
if __name__ == '__main__':
    # Titre de l'application
    st.title('Smart Traffic')
    st.markdown('<h3 style="color: red"> powered by Evolukid & Orange </h3', unsafe_allow_html=True)

    # Téléchargement de la vidéo
    video_file_buffer = st.sidebar.file_uploader("Télécharger une vidéo de traffic routier au choix", type=['mp4', 'mov', 'avi'])

    if video_file_buffer:
        st.sidebar.text('Vidéo d\'entrée')
        st.sidebar.video(video_file_buffer)
        # Sauvegarde de la vidéo dans le dossier "videos" pour une détection future
        with open(os.path.join('videos', video_file_buffer.name), 'wb') as f:
            f.write(video_file_buffer.getbuffer())

    st.sidebar.markdown('---')
    st.sidebar.title('Paramètres')
    # Classe personnalisée
    custom_class = st.sidebar.checkbox('Classes personnalisées')
    assigned_class_id = [0, 1, 2, 3]
    names = ['voiture', 'moto', 'camion', 'bus']

    if custom_class:
        assigned_class_id = []
        assigned_class = st.sidebar.multiselect('Sélectionner les classes personnalisées', list(names))
        for each in assigned_class:
            assigned_class_id.append(names.index(each))
    
    # st.write(assigned_class_id)

    # Réglage des hyperparamètres
    confidence = st.sidebar.slider('Confiance', min_value=0.0, max_value=1.0, value=0.5)
    line = st.sidebar.number_input('Position de la ligne', min_value=0.0, max_value=1.0, value=0.6, step=0.1)
    st.sidebar.markdown('---')

    # Affichage de l'état et de la vidéo
    status = st.empty()
    stframe = st.empty()
    if video_file_buffer is None:
        status.markdown('<font size= "4"> **État:** En attente d\'entrée </font>', unsafe_allow_html=True)
    else:
        status.markdown('<font size= "4"> **État:** Prêt </font>', unsafe_allow_html=True)

    # Affichage des compteurs pour chaque type de véhicule
    car, bus, truck, motor = st.columns(4)
    with car:
        st.markdown('**Voiture**')
        car_text = st.markdown('__')
    
    with bus:
        st.markdown('**Bus**')
        bus_text = st.markdown('__')

    with truck:
        st.markdown('**Camion**')
        truck_text = st.markdown('__')
    
    with motor:
        st.markdown('**Moto**')
        motor_text = st.markdown('__')

    # Affichage du FPS
    fps, _,  _, _  = st.columns(4)
    with fps:
        st.markdown('**FPS**')
        fps_text = st.markdown('__')

    # Bouton de suivi
    track_button = st.sidebar.button('DÉMARRER')
    # reset_button = st.sidebar.button('RÉINITIALISER ID')
    if track_button:
        # Réinitialisation de l'ID et du compteur à 0
        reset()
        opt = parse_opt()
        opt.conf_thres = confidence
        opt.source = f'videos/{video_file_buffer.name}'

        status.markdown('<font size= "4"> **État:** En cours d\'exécution... </font>', unsafe_allow_html=True)
        with torch.no_grad():
            detect(opt, stframe, car_text, bus_text, truck_text, motor_text, line, fps_text, assigned_class_id)
        status.markdown('<font size= "4"> **État:** Terminé ! </font>', unsafe_allow_html=True)
        # end_noti = st.markdown('<center style="color: blue"> FINISH </center>',  unsafe_allow_html=True)
