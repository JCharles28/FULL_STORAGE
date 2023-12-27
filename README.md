# Vehicle Detection and Counting System on Streamlit

![Demo image](Resources/demo.jpg)

## Introduction

This project is used to count and detect vehicle on the highway. It can detect 4 types of vehicles: car, motorcycle, bus, truck.
I run this project on Python 3.9.7.
### Cas : présence de voitures sur 1 route /4 
- Passer au vert dans la rue en question
### Cas : présence de voitures sur 2 routes /4 
- Facteur de priorité **1** : la rue qui a le plus de voiture
- Facteur de priorité **2** : durée du fert vert précédent plus court
- Facteur de priorité **3** : véhicules prioritaires (les bus)
### Cas : présence de voitures sur 3 routes /4 
- Facteur de priorité **1** : la rue qui a le plus de voiture
- Facteur de priorité **2** : durée du fert vert précédent plus court
- Facteur de priorité **3** : véhicules prioritaires (les bus)
### Cas : présence de voitures sur 4 routes /4  
- Facteur de priorité **1** : la rue qui a le plus de voiture
- Facteur de priorité **2** : durée du fert vert précédent plus court
- Facteur de priorité **3** : véhicules prioritaires (les bus)

#

- [YOLOv5](https://github.com/ultralytics/yolov5/releases) to detect objects on each of the video frames.

- [Deep SORT](https://github.com/nwojke/deep_sort) to track those objects over different frames and help counting.

- [Streamlit](https://github.com/streamlit/streamlit) to build a simple web.

## Installation

- Install essential libraries and packages:

```python
pip install -r requirements.txt
```

- Run demo:

```python
streamlit run demo.py --server.maxUploadSize=500
```

**NOTE**: If the web keeps showing "Please wait...", try to install streamlit version 1.11.0

```python
pip install streamlit==1.11.0
```

If the web shows error "no module easydict"

```python
pip install easydict
```

# DEMO

## Steps:

1. Click `Browse files` to input video

2. Setting _Custom classes_, _Confidence_ and _Line position_

![Settings](Resources/setting.jpg)

- Custom classes: choose classes you want to detect

- Confidence: the probability that one object belongs to one class

- Line position: the position of green line, any vehicle have coordinate below the line will be counted

3. Click `START`

## Result

![demo](Resources/new_demo.gif)


## Modules

- `track`: Ce module contient des fonctions et des classes liées au suivi d'objets à l'aide de l'algorithme Deep SORT.
- `tempfile`: Ce module fournit des fonctions pour travailler avec des fichiers et des répertoires temporaires.
- `cv2`: OpenCV (Open Source Computer Vision Library) est une bibliothèque de fonctions de programmation principalement destinée à la vision par ordinateur en temps réel.
- `torch`: PyTorch est une bibliothèque d'apprentissage automatique open-source basée sur la bibliothèque Torch, utilisée pour des applications telles que la vision par ordinateur et le traitement du langage naturel.
- `streamlit`: Streamlit est une bibliothèque Python open-source qui facilite la création et le partage d'applications web personnalisées pour l'apprentissage automatique et la science des données.
- `os`: Ce module fournit un moyen d'utiliser des fonctionnalités dépendantes du système d'exploitation.
