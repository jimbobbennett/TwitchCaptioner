# Twitch Captioner

A simple Python app that takes an audio stream from your microphone and converts the speech to text which is output in a window.

To configure this:

1. Sign up for the Azure speech SDK here - [portal.azure.com](https://portal.azure.com/?WT.mc_id=twitchcaptions-github-jabenn#create/Microsoft.CognitiveServicesSpeechServices)
2. Add your key and region to the `config.py` file.
3. If you want to use a different microphone than the default one, get the device uid by [following these instructions](https://docs.microsoft.com/azure/cognitive-services/speech-service/how-to-select-audio-input-devices/?WT.mc_id=twitchcaptions-github-jabenn) and set it in the `config.py` file.

Run the app and a window will appear showing the live captions.
