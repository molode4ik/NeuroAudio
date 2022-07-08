import os
import sys

def make_unique(dataset_path, phrases_path, audio_path):
    files = open(phrases_path, mode='r', encoding='utf-8')
    unique_audios = {}
    for path in files:
        name, file = path.strip().split('\t')
        if name not in unique_audios.keys():
            unique_audios.update({
                name : []
            })

        unique_audios[name].append(file)

    folder = os.listdir(audio_path)
    for key, names in unique_audios.items():
        if len(names) > 5:
            path_to = f"{dataset_path}DATASET\\{key}\\"
            os.makedirs(path_to)
            for name in names:
                for audio in folder:
                    if name == audio:
                        try: 
                            print(os.replace(f"{audio_path}{audio}", f"{path_to}{audio}"))
                        except:
                            pass
                        

if __name__ == "__main__":
    dataset_path, phrases_path, audio_path = sys.argv[1:4]
    make_unique(dataset_path, phrases_path, audio_path)