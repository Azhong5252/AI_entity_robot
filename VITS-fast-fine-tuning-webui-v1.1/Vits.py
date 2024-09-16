import os
import numpy as np
import torch
from torch import no_grad, LongTensor
import argparse
import commons
import time
from mel_processing import spectrogram_torch
import utils
from models import SynthesizerTrn
import soundfile as sf
from text import text_to_sequence, _clean_text
device = "cuda:0" if torch.cuda.is_available() else "cpu"
language_marks = {
    "Japanese": "",
    "日本語": "[JA]",
    "简体中文": "[ZH]",
    "English": "[EN]",
    "Mix": "",
}

lang = ['日本語', '简体中文', 'English', 'Mix']
def vits(gpt_msg):
    def get_text(text, hps, is_symbol):
        text_norm = text_to_sequence(text, hps.symbols, [] if is_symbol else hps.data.text_cleaners)
        if hps.data.add_blank:
            text_norm = commons.intersperse(text_norm, 0)
        text_norm = LongTensor(text_norm)
        return text_norm

    def create_tts_fn(model, hps, speaker_ids):
        def tts_fn(text, speaker, language, speed):
            if language is not None:
                text = language_marks[language] + text + language_marks[language]
            speaker_id = speaker_ids[speaker]
            stn_tst = get_text(text, hps, False)
            with no_grad():
                x_tst = stn_tst.unsqueeze(0).to(device)
                x_tst_lengths = LongTensor([stn_tst.size(0)]).to(device)
                sid = LongTensor([speaker_id]).to(device)
                audio = model.infer(x_tst, x_tst_lengths, sid=sid, noise_scale=.667, noise_scale_w=0.8,
                                    length_scale=1.0 / speed)[0][0, 0].data.cpu().float().numpy()
            del stn_tst, x_tst, x_tst_lengths, 
            
            t_remove = "[ZH]"
            while t_remove in text:
                text = text.replace(t_remove, '')
            return text, (hps.data.sampling_rate, audio)  
        return tts_fn

    def tts_result(gpt_msg, char_dropdown_value, language_dropdown_value, duration_slider_value):
        output_folder = os.getcwd() + "\\Audio\\"
        output_path = "" 
        tts_result, audio_data = tts_fn(gpt_msg, char_dropdown_value, language_dropdown_value, duration_slider_value)
        # print("Ayaka:", tts_result)
        output_path = os.path.join(output_folder, time.strftime("%Y-%m-%d-%H-%M-%S") + ".wav")
        sf.write(output_path, audio_data[1], audio_data[0])
        return tts_result,output_path

    parser = argparse.ArgumentParser()
    parser.add_argument("--model_dir", default="./G_latest.pth", help="directory to your fine-tuned model")
    parser.add_argument("--config_dir", default="./finetune_speaker.json", help="directory to your model config file")
    parser.add_argument("--share", default=False, help="make link public (used in colab)")

    args = parser.parse_args()
    hps = utils.get_hparams_from_file(args.config_dir)

    net_g = SynthesizerTrn(
        len(hps.symbols),
        hps.data.filter_length // 2 + 1,
        hps.train.segment_size // hps.data.hop_length,
        n_speakers=hps.data.n_speakers,
        **hps.model).to(device)
    _ = net_g.eval()

    _ = utils.load_checkpoint(args.model_dir, net_g, None)
    speaker_ids = hps.speakers
    speakers = list(hps.speakers.keys())
    tts_fn = create_tts_fn(net_g, hps, speaker_ids)

    char_dropdown_value = speakers[0]  
    language_dropdown_value = lang[1]  
    duration_slider_value = 1 
    Audio_text,Audio_path = tts_result(gpt_msg, char_dropdown_value, language_dropdown_value, duration_slider_value)
    return Audio_text,Audio_path