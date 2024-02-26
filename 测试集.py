import os
f_test = open("dataset/test_list.txt", 'w', encoding='utf-8')
audio_path = "C:/科研/声音预测心衰模型/重庆数据/KCCQ/语音文件"
audios = os.listdir(audio_path)
for i in range(len(audios)):
    sounds = os.listdir(os.path.join(audio_path, audios[i]))
    for sound in sounds:
        sound_path = os.path.join(audio_path, audios[i], sound).replace('\\', '/')
        f_test.write('%s\t%d\n' % (sound_path, i))
f_test.close()