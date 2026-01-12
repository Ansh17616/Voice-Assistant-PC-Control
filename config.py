# Configuration file for Voice Assistant

# Voice settings
VOICE_RATE = 150  # Speech rate (words per minute)
VOICE_VOLUME = 0.9  # Volume level (0.0 to 1.0)

# Microphone settings
MIC_TIMEOUT = 5  # Timeout for listening (seconds)
MIC_AMBIENT_NOISE = 2  # Time to adjust for ambient noise

# Application paths (Windows specific)
APP_PATHS = {
    'notepad': 'notepad.exe',
    'chrome': 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    'firefox': 'C:\\Program Files\\Mozilla Firefox\\firefox.exe',
    'calculator': 'calc.exe',
    'vscode': 'code',
    'cmd': 'cmd.exe',
    'powershell': 'powershell.exe'
}

# Commands configuration
COMMAND_OPEN = ['open', 'launch', 'start']
COMMAND_CLOSE = ['close', 'quit', 'exit', 'shut']
COMMAND_TIME = ['time', 'what time', 'current time']
COMMAND_SHUTDOWN = ['shutdown', 'turn off', 'power off']
COMMAND_RESTART = ['restart', 'reboot']

# Logging settings
LOG_LEVEL = 'INFO'
LOG_FILE = 'voice_assistant.log'

# System settings
SYSTEM_OS = 'windows'  # windows, linux, darwin
