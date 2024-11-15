# **Sign Language Interpreter with Multilingual TTS Integration**  
This project leverages the Vulavula API and Qfrency Cloud TTS to translate South African Sign Language (SASL) into spoken text and convert it into multiple South African languages with Text-to-Speech (TTS) synthesis.

---

## **Table of Contents**
1. [Project Overview](#project-overview)  
2. [Features](#features)  
3. [Setup](#setup)  
4. [Usage](#usage)  
5. [Supported Languages and Voices](#supported-languages-and-voices)  
6. [Folder Structure](#folder-structure)  
7. [Contributing](#contributing)  
8. [License](#license)  
9. [Acknowledgements](#acknowledgements)  

---

## **Project Overview**  
This project was initiated during the **#VulavulaHack** hackathon with the goal of developing an interpreter that translates **South African Sign Language (SASL) gestures** into spoken text and synthesizes it into multiple South African languages using **Qfrency Cloud TTS**. 

The system leverages:
- **Vulavula API** for multilingual language translation.  
- **Qfrency Cloud TTS** to convert text into speech, supporting various **female voices** across multiple languages for richer accessibility.

This project emphasizes real-time gesture recognition, with modular support for different languages and voices, using technologies like **MediaPipe**, **OpenCV**, and **scikit-learn** to ensure smooth operation. The interpreter is designed to foster inclusive communication across South Africa’s linguistic diversity.


---
## **Features**  
- Real-time sign language interpretation with language translation.  
- Dynamic selection of TTS voices based on gender, age, and language.  
- Supports South African languages including Afrikaans, isiZulu, Sepedi, Setswana, and more.  
- Utilizes **MediaPipe** for efficient hand landmark extraction to enhance gesture recognition.  
- Implements **scikit-learn** for machine learning, specifically using Support Vector Machines (SVM) for model training and evaluation.  
- Integrates **TensorFlow** for preprocessing and managing deep learning models.  
- WAV audio synthesis and playback with PyAudio.  
- Incremental WAV file storage with unique filenames.  

---

## **Setup**  
Follow these steps to set up and run the project locally.

### Prerequisites  
- Python 3.x  
- [Vulavula API Key](https://lelapa.ai) (for translation)  
- [Qfrency Cloud TTS API Key](https://qfrency.com)  

### Installation  

1. **Create a virtual environment** (recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

2. **Clone this repository**:  
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set API Keys (Command Line):**
    On **Linux/macOS**:
    ```bash
    export X_ACCOUNT_KEY="your_account_key"
    export X_API_KEY="your_api_key"
    export VULAVULA_API_KEY="your_vulavula_api_key"
    ```

    On **Windows (Command Prompt)**:
    ```cmd
    set X_ACCOUNT_KEY=your_account_key
    set X_API_KEY=your_api_key
    set VULAVULA_API_KEY=your_vulavula_api_key
    ```

5. **Run the Project**:
    ```bash
    Each notebook must be run in order 1-4. The final notebook will have the active gesture interpretation and translation windows.
    ```


---

## **Usage**  
1. Each notebook must be run in order 1-4. The final notebook will have the active gesture interpretation and translation windows. 
2. Example output:  
   - If input is **SASL gesture**, it translates to a language such as **isiZulu** and produces a synthesized WAV file.  
   - Audio will automatically play after synthesis using the selected TTS voice.


## **Supported Languages and Voices**  
Below are the languages and sample voices supported by this project:  

| **Language** | **Male Voice**  | **Female Voice** |  
|--------------|-----------------|------------------|  
| Afrikaans    | Kobus, Bennie   | Maryna           |  
| isiZulu      | Sifiso          | Lindiwe          |  
| Sepedi       | Tshepo          | Mmapitsi         |  
| isiXhosa     | Vuyo            | Zoleka           |  
| Setswana     |      -          | Lethabo          |  
| Sesotho      | Tshepo          | Kamohelo         |  
| Siswati      |      -          | Temaswati        |  
| Xitsonga     |      -          | Sasekani         |  

*All South African languages are supported for translation, but qfrency doesn’t cover all languages. The female voice is preferred due to the wider range of options.*  

---

## **Folder Structure**  
```bash
repo-name-goes-here  
📂 synth_wav_files                      # Directory containing synthesized WAV audio files  
📂 data                                 # Directory created during data collection  
├── 1-collect_data.ipynb                # Jupyter notebook to collect gesture data for training the model  
├── 2- Hand_Landmarks_extraction.ipynb  # Extracts hand landmarks using MediaPipe or similar tools  
├── 3-train_mode.ipynb                  # Trains the model using collected data and SVM or other ML techniques  
├── 4- Real_time_deployment.ipynb       # Deploys the model for real-time gesture recognition and translation  
├── qfrency.py                          # Script for managing text-to-speech (TTS) frequency or voice settings  
├── readme.md                           # Project documentation with instructions, dependencies, and usage  
├── requirements.txt                    # List of dependencies to install (useful for setting up the environment)  
├── speech.py                           # Handles TTS operations for converting text to spoken audio  
└── translation.py                      # Manages text translations between supported languages  
```

## License
idk what. 

## **Contributing**  
We welcome contributions! If you’d like to help improve this project:  
1. Fork this repository.  
2. Create a feature branch:  
   ```bash
   git checkout -b feature/your-feature
## Acknowledgements
Special thanks to:
* Lelapa AI for the use of their Vulavula API
* The CSIR for the use of their qfrency TTS system


---

