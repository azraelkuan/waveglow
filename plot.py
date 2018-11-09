import matplotlib
matplotlib.use('Agg')
import librosa.display as dsp
import matplotlib.pyplot as plt


def waveplot(path, real_wav, fake_wav, sr):

    plt.figure(figsize=(12, 6))
    ax = plt.subplot(2, 1, 1)
    dsp.waveplot(real_wav, sr=sr)
    ax.set_title('Target waveform')
    ax = plt.subplot(2, 1, 2)
    dsp.waveplot(fake_wav, sr=sr)
    ax.set_title('Prediction waveform')

    plt.tight_layout()
    plt.savefig(path, format="png")
    plt.close()



