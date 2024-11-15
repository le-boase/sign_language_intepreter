from vulavula import VulavulaClient
import qfrency
import wave
import pyaudio
import os
import re
from dotenv import load_dotenv
  
male_voices = [{'voice-code': 'afr-ZA-hmm-bennie', 'name': 'Bennie', 'description': 'Afrikaans male child voice with HMM acoustic models and mixed-excitation vocoder', 'technique': 'HMM', 'language': 'afrikaans', 'lang-code': 'afr', 'country-code': 'ZA', 'gender': 'male', 'age': 'child', 'sample-rate': 16000}, 
               {'voice-code': 'afr-ZA-dnn-kobus', 'name': 'Kobus', 'description': 'Afrikaans male voice with neural acoustic and vocoder models', 'technique': 'DNN', 'language': 'afrikaans', 'lang-code': 'afr', 'country-code': 'ZA', 'gender': 'male', 'age': 'adult', 'sample-rate': 22050}, 
               {'voice-code': 'afr-ZA-hmm-kobus', 'name': 'Kobus', 'description': 'Afrikaans male voice with HMM acoustic models and mixed-excitation vocoder', 'technique': 'HMM', 'language': 'afrikaans', 'lang-code': 'afr', 'country-code': 'ZA', 'gender': 'male', 'age': 'adult', 'sample-rate': 16000}, 
               {'voice-code': 'eng-ZA-dnn-tim', 'name': 'Tim', 'description': 'South African English male voice with neural acoustic and vocoder models', 'technique': 'DNN', 'language': 'englishza', 'lang-code': 'eng', 'country-code': 'ZA', 'gender': 'male', 'age': 'adult', 'sample-rate': 22050},
               {'voice-code': 'eng-ZA-hmm-tim', 'name': 'Tim', 'description': 'South African English male voice with HMM acoustic models and mixed-excitation vocoder', 'technique': 'HMM', 'language': 'englishza', 'lang-code': 'eng', 'country-code': 'ZA', 'gender': 'male', 'age': 'adult', 'sample-rate': 16000}, 
               {'voice-code': 'nbl-ZA-dnn-banele', 'name': 'Banele', 'description': 'isiNdebele male voice with neural acoustic and vocoder models', 'technique': 'DNN', 'language': 'isindebele', 'lang-code': 'nbl', 'country-code': 'ZA', 'gender': 'male', 'age': 'adult', 'sample-rate': 22050},
               {'voice-code': 'nbl-ZA-hmm-banele', 'name': 'Banele', 'description': 'isiNdebele male voice with HMM acoustic models and mixed-excitation vocoder', 'technique': 'HMM', 'language': 'isindebele', 'lang-code': 'nbl', 'country-code': 'ZA', 'gender': 'male', 'age': 'adult', 'sample-rate': 16000},
               {'voice-code': 'nso-ZA-dnn-tshepo', 'name': 'Tshepo', 'description': 'Sepedi male voice with neural acoustic and vocoder models', 'technique': 'DNN', 'language': 'sepedi', 'lang-code': 'nso', 'country-code': 'ZA', 'gender': 'male', 'age': 'adult', 'sample-rate': 22050},
               {'voice-code': 'nso-ZA-hmm-tshepo', 'name': 'Tshepo', 'description': 'Sepedi male voice with HMM acoustic models and mixed-excitation vocoder', 'technique': 'HMM', 'language': 'sepedi', 'lang-code': 'nso', 'country-code': 'ZA', 'gender': 'male', 'age': 'adult', 'sample-rate': 16000},
               {'voice-code': 'ven-ZA-dnn-rabelani', 'name': 'Rabelani', 'description': 'Tshivenda male voice with neural acoustic and vocoder models', 'technique': 'DNN', 'language': 'tshivenda', 'lang-code': 'ven', 'country-code': 'ZA', 'gender': 'male', 'age': 'adult', 'sample-rate': 22050},
               {'voice-code': 'ven-ZA-hmm-rabelani', 'name': 'Rabelani', 'description': 'Tshivenda male voice with HMM acoustic models and mixed-excitation vocoder', 'technique': 'HMM', 'language': 'tshivenda', 'lang-code': 'ven', 'country-code': 'ZA', 'gender': 'male', 'age': 'adult', 'sample-rate': 16000}, 
               {'voice-code': 'xho-ZA-dnn-vuyo', 'name': 'Vuyo', 'description': 'isiXhosa male voice with neural acoustic and vocoder models', 'technique': 'DNN', 'language': 'isixhosa', 'lang-code': 'xho', 'country-code': 'ZA', 'gender': 'male', 'age': 'adult', 'sample-rate': 22050},
               {'voice-code': 'xho-ZA-hmm-vuyo', 'name': 'Vuyo', 'description': 'isiXhosa male voice with HMM acoustic models and mixed-excitation vocoder', 'technique': 'HMM', 'language': 'isixhosa', 'lang-code': 'xho', 'country-code': 'ZA', 'gender': 'male', 'age': 'adult', 'sample-rate': 16000},
               {'voice-code': 'zul-ZA-dnn-sifiso', 'name': 'Sifiso', 'description': 'isiZulu male voice with neural acoustic and vocoder models', 'technique': 'DNN', 'language': 'isizulu', 'lang-code': 'zul', 'country-code': 'ZA', 'gender': 'male', 'age': 'adult', 'sample-rate': 22050}]

female_voices = [{'voice-code': 'afr-ZA-dnn-maryna', 'name': 'Maryna', 'description': 'Afrikaans female voice with neural acoustic and vocoder models', 'technique': 'DNN', 'language': 'afrikaans', 'lang-code': 'afr', 'country-code': 'ZA', 'gender': 'female', 'age': 'adult', 'sample-rate': 22050}, 
                 {'voice-code': 'afr-ZA-hmm-maryna', 'name': 'Maryna', 'description': 'Afrikaans female voice with HMM acoustic models and mixed-excitation vocoder', 'technique': 'HMM', 'language': 'afrikaans', 'lang-code': 'afr', 'country-code': 'ZA', 'gender': 'female', 'age': 'adult', 'sample-rate': 16000},
                 {'voice-code': 'eng-ZA-dnn-candice', 'name': 'Candice', 'description': 'South African English female voice with neural acoustic and vocoder models', 'technique': 'DNN', 'language': 'englishza', 'lang-code': 'eng', 'country-code': 'ZA', 'gender': 'female', 'age': 'adult', 'sample-rate': 22050}, 
                 {'voice-code': 'eng-ZA-hmm-candice', 'name': 'Candice', 'description': 'South African English female voice with HMM acoustic models and mixed-excitation vocoder', 'technique': 'HMM', 'language': 'englishza', 'lang-code': 'eng', 'country-code': 'ZA', 'gender': 'female', 'age': 'adult', 'sample-rate': 16000},
                 {'voice-code': 'nso-ZA-dnn-mmapitsi', 'name': 'Mmapitsi', 'description': 'Sepedi female voice with neural acoustic and vocoder models', 'technique': 'DNN', 'language': 'sepedi', 'lang-code': 'nso', 'country-code': 'ZA', 'gender': 'female', 'age': 'adult', 'sample-rate': 22050}, 
                 {'voice-code': 'nso-ZA-hmm-mmapitsi', 'name': 'Mmapitsi', 'description': 'Sepedi female voice with HMM acoustic models and mixed-excitation vocoder', 'technique': 'HMM', 'language': 'sepedi', 'lang-code': 'nso', 'country-code': 'ZA', 'gender': 'female', 'age': 'adult', 'sample-rate': 16000},
                 {'voice-code': 'sot-ZA-dnn-kamohelo', 'name': 'Kamohelo', 'description': 'Sesotho female voice with neural acoustic and vocoder models', 'technique': 'DNN', 'language': 'sesotho', 'lang-code': 'sot', 'country-code': 'ZA', 'gender': 'female', 'age': 'adult', 'sample-rate': 22050},
                 {'voice-code': 'sot-ZA-hmm-kamohelo', 'name': 'Kamohelo', 'description': 'Sesotho female voice with HMM acoustic models and mixed-excitation vocoder', 'technique': 'HMM', 'language': 'sesotho', 'lang-code': 'sot', 'country-code': 'ZA', 'gender': 'female', 'age': 'adult', 'sample-rate': 16000},
                 {'voice-code': 'ssw-ZA-dnn-temaswati', 'name': 'Temaswati', 'description': 'siSwati female voice with neural acoustic and vocoder models', 'technique': 'DNN', 'language': 'siswati', 'lang-code': 'ssw', 'country-code': 'ZA', 'gender': 'female', 'age': 'adult', 'sample-rate': 22050},
                 {'voice-code': 'ssw-ZA-hmm-temaswati', 'name': 'Temaswati', 'description': 'siSwati female voice with HMM acoustic models and mixed-excitation vocoder', 'technique': 'HMM', 'language': 'siswati', 'lang-code': 'ssw', 'country-code': 'ZA', 'gender': 'female', 'age': 'adult', 'sample-rate': 16000}, 
                 {'voice-code': 'tsn-ZA-dnn-lethabo', 'name': 'Lethabo', 'description': 'Setswana female voice with neural acoustic and vocoder models', 'technique': 'DNN', 'language': 'setswana', 'lang-code': 'tsn', 'country-code': 'ZA', 'gender': 'female', 'age': 'adult', 'sample-rate': 22050},
                 {'voice-code': 'tsn-ZA-hmm-lethabo', 'name': 'Lethabo', 'description': 'Setswana female voice with HMM acoustic models and mixed-excitation vocoder', 'technique': 'HMM', 'language': 'setswana', 'lang-code': 'tsn', 'country-code': 'ZA', 'gender': 'female', 'age': 'adult', 'sample-rate': 16000}, 
                 {'voice-code': 'tso-ZA-dnn-sasekani', 'name': 'Sasekani', 'description': 'Xitsonga female voice with neural acoustic and vocoder models', 'technique': 'DNN', 'language': 'xitsonga', 'lang-code': 'tso', 'country-code': 'ZA', 'gender': 'female', 'age': 'adult', 'sample-rate': 22050},
                 {'voice-code': 'tso-ZA-hmm-sasekani', 'name': 'Sasekani', 'description': 'Xitsonga female voice with HMM acoustic models and mixed-excitation vocoder', 'technique': 'HMM', 'language': 'xitsonga', 'lang-code': 'tso', 'country-code': 'ZA', 'gender': 'female', 'age': 'adult', 'sample-rate': 16000}, 
                 {'voice-code': 'xho-ZA-dnn-zoleka', 'name': 'Zoleka', 'description': 'isiXhosa female voice with neural acoustic and vocoder models', 'technique': 'DNN', 'language': 'isixhosa', 'lang-code': 'xho', 'country-code': 'ZA', 'gender': 'female', 'age': 'adult', 'sample-rate': 22050}, 
                 {'voice-code': 'xho-ZA-hmm-zoleka', 'name': 'Zoleka', 'description': 'isiXhosa female voice with HMM acoustic models and mixed-excitation vocoder', 'technique': 'HMM', 'language': 'isixhosa', 'lang-code': 'xho', 'country-code': 'ZA', 'gender': 'female', 'age': 'adult', 'sample-rate': 16000},
                 {'voice-code': 'zul-ZA-dnn-lindiwe', 'name': 'Lindiwe', 'description': 'isiZulu female voice with neural acoustic and vocoder models', 'technique': 'DNN', 'language': 'isizulu', 'lang-code': 'zul', 'country-code': 'ZA', 'gender': 'female', 'age': 'adult', 'sample-rate': 22050},
                 {'voice-code': 'zul-ZA-hmm-lindiwe', 'name': 'Lindiwe', 'description': 'isiZulu female voice with HMM acoustic models and mixed-excitation vocoder', 'technique': 'HMM', 'language': 'isizulu', 'lang-code': 'zul', 'country-code': 'ZA', 'gender': 'female', 'age': 'adult', 'sample-rate': 16000}]


def choose_voice_code(target_lang, user_gender, user_age):
    # Combine male and female voices into one list
    all_voices = male_voices + female_voices
    
    # Loop through all voices to find a match
    for voice in all_voices:
        if voice['language'] == target_lang and voice['gender'] == user_gender and voice['age'] == user_age:
            return voice['voice-code'], voice['sample-rate']
    
    # Return None if no match is found
    return None, None
    
      
def convert_lang_code(lang_code):
  lang_mapping = {
    "nso_Latn": "sepedi",
    "afr_Latn": "afrikaans",
    "sot_Latn": "sesotho",
    "ssw_Latn": "siswati",
    "tso_Latn": "xitsonga",
    "tsn_Latn": "setswana",
    "xho_Latn": "isixhosa",
    "zul_Latn": "isizulu",
    "eng_Latn": "english",
    "swh_Latn": "swahili"
  }
  return lang_mapping.get(lang_code, lang_code)

def get_next_synth_wav_filename():
    
    # Define the folder name using the current date and time
    folder_name = "synth_wav_files"
    
    # Check if the folder exists; if not, create it
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        
    # List all files in the current directory
    files = os.listdir(folder_name)
    
    # Filter files that match the synth_wav pattern and extract numbers
    synth_wav_files = [f for f in files if re.match(r'synthed_wav_(\d+)\.wav', f)]
    max_number = 0
    for file in synth_wav_files:
        # Extract number from filename
        number = int(re.search(r'(\d+)', file).group(0))
        if number > max_number:
            max_number = number
    # Increment the highest number found by 1 for the new filename
    new_filename = f"synthed_wav_{max_number + 1}.wav"
    return new_filename,folder_name

def write_wav_to_file(wav, filename,folder_name):
     # Ensure the folder exists
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    # Construct the full file path
    file_path = os.path.join(folder_name, filename)
    
    # Write the WAV data to the file
    with open(file_path, "wb") as p:
        p.write(wav)
    
# instansiate a cloud API instance
load_dotenv()
X_ACCOUNT_KEY = os.getenv("X_ACCOUNT_KEY", "default_account_key")
X_API_KEY = os.getenv("X_API_KEY", "default_api_key")

cloud_api = qfrency.QfrencyCloudTTS(X_ACCOUNT_KEY, X_API_KEY)
    
def synthesize_and_play(spoken_text, target_lang, user_gender="female", user_age="adult"): #remannt from when I wanted t odetect gender and age on screen, defaults female and adult
    # Convert the provided target language code
    target_lang = convert_lang_code(target_lang)
    
    # Choose the voice code and sample rate based on target language, gender, and age
    voice_code, sample_rate = choose_voice_code(target_lang, user_gender, user_age)
    
    if not voice_code:
        print(f"No voice found for language: {target_lang}, gender: {user_gender}, age: {user_age}")
        return
    
    # Generate the next filename for the synthesized audio
    new_filename, folder_name = get_next_synth_wav_filename()
    
    # Call the cloud API to synthesize the audio
    synthed_wav = cloud_api.synth(voice_code, spoken_text, {"sample-rate": sample_rate})
    
    # Write the synthesized WAV file to disk
    write_wav_to_file(synthed_wav, new_filename, folder_name)
    
    # Construct the file path for the synthesized audio
    file_path = os.path.join(folder_name, new_filename)
    
    # Play the synthesized audio
    with wave.open(file_path, 'rb') as wav_file:
        # Create an instance of the PyAudio class
        audio = pyaudio.PyAudio()

        # Open a stream to play the WAV file
        stream = audio.open(format=audio.get_format_from_width(wav_file.getsampwidth()),
                            channels=wav_file.getnchannels(),
                            rate=wav_file.getframerate(),
                            output=True)

        # Read the data from the WAV file and play it
        data = wav_file.readframes(1024)
        while data:
            stream.write(data)
            data = wav_file.readframes(1024)

        # Close the stream and terminate PyAudio
        stream.stop_stream()
        stream.close()
        audio.terminate()


# # Example usage
# spoken_text = "Ek is honger?"
# target_lang = "afr_Latn" 
# synthesize_and_play(spoken_text, target_lang, user_gender="male", user_age="adult")
