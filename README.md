# 🎥 YouTube Auto Quiz Generator

Générez automatiquement des quiz à partir de vidéos YouTube avec sous-titres en anglais !  
Ce site permet aux enseignants de créer des quiz interactifs à partir de vidéos, de les partager aux élèves, et de consulter leurs résultats.

🔗 **Accéder à l'application : [https://auto-quiz.streamlit.app/](https://auto-quiz.streamlit.app/)**

---

## 📚 Scénario
1. L'enseignant trouve une vidéo YouTube intéressante (avec sous-titres anglais).
2. Il colle le lien de la vidéo dans l'application.
3. Il appuie sur le bouton généré.
4. Un quiz est automatiquement généré à partir de la transcription.
5. Il partage le lien du quiz aux élèves.
6. Chaque élève répond au quiz et obtient son score.

---

## 🚀 Fonctionnalités

- 🎯 Génération automatique de quiz à choix multiples via une vidéo
- 🎈 Score affiché avec animation

---

## 🛠️ Technologies utilisées

- [Streamlit](https://streamlit.io/) — Framework Python pour apps web
- [YouTube Transcript API](https://pypi.org/project/youtube-transcript-api/)
- [OpenAI API](https://platform.openai.com/)
- Python & JSON

---

## ▶️ Lancer en local

1. **Cloner le projet**

   ```bash
   git clone https://github.com/your-username/youtube-quiz-generator.git
   cd youtube-quiz-generator

2. **Installer les dépendances**

   ```bash
   pip install streamlit youtube-transcript-api openai

3. Configurer la clé API OpenAI
   ```bash
   PRIVATE_KEY = "votre_clé_api_openai"

4. Lancer l'application
   ```bash
   streamlit run app.py

---

## ✍️ Auteurs & Crédits

🛠️ Projet réalisé dans le cadre du **BTS CIEL - 1ère année**  
👥 Développé par : **Ynniis** & **NKRIDev**  
📅 Date : *11 avril 2025*
