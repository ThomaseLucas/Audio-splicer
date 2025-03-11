import whisper
import string
import re


def find_audio_data(audio_file):

    #load the model
    model = whisper.load_model("base")

    result = model.transcribe(audio_file, word_timestamps=True,)

    segments = result["segments"]

    print()
    print(result["text"])
    print()

    return result

def normalize_word(word):
    return word.strip(string.punctuation + " ").lower()

def find_last_word(text_sentences, current_sentence):
    
    current_sentence = text_sentences[current_sentence]
    last_word = current_sentence.split()[-1]
    return last_word

def divide_by_sentence(text):
    sentences = re.split(r"[!.?]", text) # add more punctuation marks as needed
    return [sentence.strip() for sentence in sentences if sentence.strip()]

def get_word_timestamps(data):
    return [word for segment in data["segments"] for word in segment["words"]]

def find_time_of_last_word(last_word, word_timestamps):
    normalized_last_word = normalize_word(last_word)

    for word in word_timestamps:
        print(f"Comparing {normalize_word(word['word'])} with {normalized_last_word}")
        if normalize_word(word["word"]) == normalized_last_word:
            return word["end"]
        
    return "Word not found"

def engine():
    english_data = find_audio_data("audio_files/english_oaks_short.mp3")
    spanish_data = find_audio_data("audio_files/spanish_oaks_short.mp3")
    
    english_sentences = divide_by_sentence(english_data["text"])
    spanish_sentences = divide_by_sentence(spanish_data["text"])

    en_word_timestamps = get_word_timestamps(english_data)
    sp_word_timestamps = get_word_timestamps(spanish_data)

    print()
    print(english_sentences)
    print()
    print(spanish_sentences)
    print()


    en_last_word_test = find_time_of_last_word("me", en_word_timestamps)
    sp_last_word_test = find_time_of_last_word("personas", sp_word_timestamps)
    print(en_last_word_test)
    print(sp_last_word_test)


if __name__ == "__main__":
    engine()



    


        

    






