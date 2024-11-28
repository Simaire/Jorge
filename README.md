
# JORGE

<p align="center">
  <h1 align="center">JORGE</h1>
</p>
<p align="center">
  <em><code>❯ À REMPLACER</code></em>
</p>
<p align="center">
  <img src="https://img.shields.io/github/license/Simaire/Jorge?style=flat&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
  <img src="https://img.shields.io/github/last-commit/Simaire/Jorge?style=flat&logo=git&logoColor=white&color=0080ff" alt="dernière-commit">
  <img src="https://img.shields.io/github/languages/top/Simaire/Jorge?style=flat&color=0080ff" alt="langage-principal">
  <img src="https://img.shields.io/github/languages/count/Simaire/Jorge?style=flat&color=0080ff" alt="nombre-langages">
</p>
<p align="center">Construit avec les outils et technologies suivants :</p>
<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
</p>
<br>

## 🔗 Table des Matières

- [📍 Aperçu](#-aperçu)
- [👾 Fonctionnalités](#-fonctionnalités)
- [📁 Structure du Projet](#-structure-du-projet)
  - [📂 Index du Projet](#-index-du-projet)
- [🚀 Démarrage](#-démarrage)
  - [☑️ Prérequis](#-prérequis)
  - [⚙️ Installation](#-installation)
  - [🤖 Utilisation](#🤖-utilisation)
  - [🧪 Tests](#🧪-tests)
- [📌 Feuille de Route](#-feuille-de-route)
- [🔰 Contribution](#-contribution)
- [🎗 Licence](#-licence)
- [🙌 Remerciements](#-remerciements)

---

## 📍 Aperçu

<code>❯ Jorge est un programme permettant de connecter Discord à une IA conversationnelle des services d'OpenAI. Ce projet a été réalisé dans le but d'apprendre l'utilisation d'API avec Python.</code>

---

## 👾 Fonctionnalités

<code>❯ Connecte deux API pour une conversation sur Discord avec une IA.</code>

---

## 📁 Structure du Projet

```sh
└── Jorge/
    ├── README.md
    ├── config
    └── main.py
```
---

## 🚀 Démarrage

### ☑️ Prérequis

Avant de commencer, assurez-vous que votre environnement de développement répond aux exigences suivantes :

- **Langage de programmation :** Python

### ⚙️ Installation

Installez Jorge en suivant ces étapes :

**Depuis la source :**

1. Clonez le dépôt Jorge :
```sh
❯ git clone https://github.com/Simaire/Jorge
```

2. Accédez au répertoire du projet :
```sh
❯ cd Jorge
```

3. Installez les dépendances du projet :
```sh
❯ pip install -r requirements.txt
```

> **Important :** Configurez vos clés dans le fichier `Clef`.

### 🤖 Utilisation

Exécutez Jorge avec la commande suivante :
```sh
❯ python nom_du_script.py
```

## 🔰 Contribution

- **🐛 [Signaler des Problèmes](https://github.com/Simaire/Jorge/issues)** : Soumettez les bogues trouvés ou proposez des idées d'amélioration pour le projet `Jorge`.
- **💡 [Soumettre des Pull Requests](https://github.com/Simaire/Jorge/pulls)** : Consultez les PR ouvertes et proposez vos contributions.

---

## 🎗 Licence

Ce projet est protégé par la [licence MIT](https://choosealicense.com/licenses/mit/). Pour plus de détails, consultez le fichier [LICENSE](https://github.com/Simaire/Jorge/blob/master/LICENSE).

---

## 🙌 Remerciements

- Utilisation de l'API Discord
- Utilisation de l'API OpenAI

---

# Jorge
Un bot Discord en Python, libre de droit.

**À noter :**  
Évitez de spammer et attendez la réponse du bot !

**Bibliothèques nécessaires :**
- `os`
- `discord`
- `openai`
- `dotenv`

Pour faire fonctionner le bot, vous devez créer un fichier nommé `Clef`, identique au fichier "config", et le remplir comme suit :

```plaintext
TOKEN=[Votre token privé de votre bot Discord]

openaikey=[Votre clé API OpenAI]
```
