# -*- coding: utf-8 -*-
"""
Diese Datei sollte nicht verändert werden und wird von uns gestellt und zurückgesetzt.
Skript testet das neu trainierte Modell
@author: Maurice Rohr
"""

from predict import predict_labels
from wettbewerb import load_references, save_predictions
import torch
import os

os.environ["CUDA_VISIBLE_DEVICES"] = "0,1,2,3,4,5,6,7"

if __name__ == '__main__':
    ecg_leads, ecg_labels, fs, ecg_names = load_references(
        './data_new/validation')  # Importiere EKG-Dateien, zugehörige Diagnose, Sampling-Frequenz (Hz) und Name                                                # Sampling-Frequenz 300 Hz

    predictions = predict_labels(ecg_leads, fs, ecg_names, use_pretrained=False, device=torch.device("cuda:7" if torch.cuda.is_available() else "cpu"))

    save_predictions(predictions)  # speichert Prädiktion in CSV Datei
