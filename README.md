# Voice-Assistant-PC-Control

A powerful voice-controlled assistant that gives **total control of your PC through voice commands**. Built with Python, using speech recognition and AI to execute system commands, open applications, and manage your computer hands-free.

## Features ✨

- **Voice Recognition**: Real-time speech recognition using Google Speech-to-Text API
- **Text-to-Speech**: Natural audio responses from the assistant
- **PC Control**: 
  - Open and close applications
  - Get system information (time, date)
  - Shutdown, restart, or sleep PC
  - Run system commands
- **Customizable**: Easy configuration for voice settings and commands
- **Cross-Platform**: Works on Windows, Linux, and macOS
- **Lightweight**: Minimal resource usage

## Requirements 📋

- Python 3.7+
- Microphone connected to your PC
- Internet connection (for Google Speech-to-Text)
- PyAudio (may require additional system libraries)

## Installation 🚀

1. Clone the repository:
```bash
git clone https://github.com/Ansh17616/Voice-Assistant-PC-Control.git
cd Voice-Assistant-PC-Control
```

2. Create virtual environment:
```bash
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage 💻

Run the voice assistant:
```bash
python voice_assistant.py
```

Once running, speak your commands:
- "Open Notepad"
- "Open Chrome"
- "What time is it?"
- "Close Chrome"
- "Shutdown"

## Configuration ⚙️

Edit `config.py` to customize:
- Voice rate and volume
- Application paths
- Custom commands
- Logging settings

## File Structure 📁

```
Voice-Assistant-PC-Control/
├── voice_assistant.py     # Main assistant module
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore file
└── README.md             # This file
```

## Supported Commands 🎤

### Open Applications
- "Open Notepad"
- "Open Chrome"
- "Open Firefox"
- "Open Calculator"
- "Open VS Code"

### System Information
- "What time is it?"
- "Current time?"

### System Control
- "Shutdown"
- "Restart"
- "Close Chrome"

## Troubleshooting 🔧

### No Audio Input
- Check microphone is properly connected
- Verify microphone permissions in OS settings
- Test microphone in system settings

### Audio Recognition Issues
- Ensure internet connection is active
- Speak clearly and at normal pace
- Reduce background noise
- Adjust microphone settings in config.py

### ModuleNotFoundError
- Ensure virtual environment is activated
- Run `pip install -r requirements.txt` again

## Contributing 🤝

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License 📄

This project is open source and available under the MIT License.

## Author 👨‍💻

**Ansh17616** - Voice Assistant Project

## Disclaimer ⚠️

This voice assistant can execute system commands. Always use caution when granting voice control over critical system functions. Ensure proper authorization protocols are in place before deployment in production environments.

---

**Made with ❤️ for hands-free PC control**
