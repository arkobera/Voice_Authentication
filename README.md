# Voice Authentication System

## Overview

This project implements a **voice authentication system** using **SpeechBrain** to verify users based on their voice. The system calculates the **cosine similarity score** between a provided voice sample and stored reference samples, determining authentication based on a manually set threshold.

## Project Structure

- **Audio/**: Stores all recorded voice samples.
- **verification.py**: Loads the **SpeechBrain** model and computes cosine similarity between voice embeddings to verify users.

## Installation

### Prerequisites

1. Python 3.6 or higher.
2. Install the required dependencies:

   ```bash
   pip install speechbrain torchaudio


### Running the Verification

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/voice-authentication.git
   cd voice-authentication
   ```

2. Run the verification script:

   ```bash
   python verification.py
   ```

3. The script will prompt for an input voice sample and compare it against stored samples.

## How It Works

1. **Voice Embeddings**: The system extracts embeddings from voice samples using **SpeechBrain**.
2. **Cosine Similarity**: It computes the similarity score between the test sample and reference samples.
3. **Threshold-Based Authentication**: If the score exceeds the manually set threshold, the user is authenticated; otherwise, access is denied.

## Usage

- **Record a reference voice sample** and store it in the `Audio/` folder. Use the recorder.py it will automatically store it in the correct directory
- **Provide a test voice sample**, and the system will determine whether the speaker matches the reference.
- Adjust the **threshold** in `verification.py` to fine-tune authentication sensitivity.

## Contributing

Feel free to fork the repository, improve the system, and submit a pull request! If you encounter any issues, create a GitHub issue to discuss it.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [SpeechBrain](https://speechbrain.github.io/) for providing powerful speech processing models.
```
