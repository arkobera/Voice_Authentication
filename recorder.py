import pyaudio
import wave
import os
import numpy as np

def list_microphones():
    """Lists all available microphone devices."""
    p = pyaudio.PyAudio()
    print("\nAvailable Microphones:")
    for i in range(p.get_device_count()):
        info = p.get_device_info_by_index(i)
        print(f"ID {i}: {info['name']}")
    p.terminate()

def get_next_filename(output_directory, base_filename="sample_input"):
    """Finds the next available filename by checking existing files in the directory."""
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)  # Create directory if it does not exist

    # Find the highest 'i' in existing files
    existing_files = [f for f in os.listdir(output_directory) if f.startswith(base_filename) and f.endswith(".wav")]
    existing_indices = [int(f[len(base_filename)+1:-4]) for f in existing_files if f[len(base_filename)+1:-4].isdigit()]
    next_index = max(existing_indices, default=0) + 1  # Increment the highest found index

    return os.path.join(output_directory, f"{base_filename}_{next_index}.wav")

def record_audio(duration, output_directory, device_index=None):
    """Records audio from the microphone and saves it as 'sample_input_i.wav' in the specified directory."""

    RATE = 44100  # Sampling rate (44.1kHz)
    CHANNELS = 1  # Change to 2 if using stereo microphone
    FORMAT = pyaudio.paInt16  # 16-bit depth
    CHUNKSIZE = 1024  # Buffer size

    # Initialize PyAudio
    p = pyaudio.PyAudio()

    # Use the default device if none is provided
    if device_index is None:
        device_index = p.get_default_input_device_info()["index"]

    # Open the microphone stream
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNKSIZE,
                    input_device_index=device_index)

    print(f"\nRecording from device {device_index}... Speak now!\n")

    frames = []
    for _ in range(0, int(RATE / CHUNKSIZE * duration)):
        data = stream.read(CHUNKSIZE, exception_on_overflow=False)
        
        # Convert audio bytes to numpy array to check volume level
        audio_array = np.frombuffer(data, dtype=np.int16)
        volume = np.abs(audio_array).mean()  # Simple volume estimate
        print(f"Volume Level: {int(volume)}", end="\r", flush=True)  # Realtime volume feedback
        
        frames.append(data)

    print("\nRecording Complete!")

    # Stop stream
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Get next available filename
    output_path = get_next_filename(output_directory)

    # Save to .wav file
    with wave.open(output_path, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

    print(f"Recording saved to {output_path}")

# List available microphones
list_microphones()

# Define output directory
output_directory = "Auth//Audio"

# Record from default device (or specify `device_index` from `list_microphones()`)
record_audio(duration=3, output_directory=output_directory)