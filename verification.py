from speechbrain.pretrained import SpeakerRecognition
import os

# Set absolute path for audio files
sub_path = os.path.abspath("C:\\Users\\91991\\Desktop\\Streamlit\\Audio")

# Initialize the speaker recognition model
saved_model_dir = "C:\\Users\\91991\\Documents\\speechbrain_model"
model = SpeakerRecognition.from_hparams(source="speechbrain/spkrec-ecapa-voxceleb", savedir=saved_model_dir)

# Define audio file paths (fixed paths)
ref_audio = "C:/Users/91991/Desktop/Streamlit/Auth/Audio/reference.wav"
user_audio = "C:/Users/91991/Desktop/Streamlit/Auth/Audio/sample_input_12.wav"


# Check if files exist
if not os.path.exists(ref_audio) or not os.path.exists(user_audio):
    raise FileNotFoundError("One or both audio files not found!")

# Perform speaker verification
score, preds = model.verify_files(ref_audio, user_audio)

# Print similarity score
print(f"Speaker Similarity Score: {score.item()}")
if score.item() < 0.44:
    print("❌ Unidentified User")
else:
    print("✅ Successfully Verified")

