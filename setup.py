from setuptools import setup, find_packages
import os

# Function to read and replace lines in bot.py
def update_bot_py():
    bot_py_path = 'bot.py'
    
    # Read user inputs
    spotify_client_id = input('Enter your Spotify Client ID: ')
    spotify_client_secret = input('Enter your Spotify Client Secret: ')
    discord_bot_token = input('Enter your Discord Bot Token: ')
    text_channel_id = input('Enter the Channel ID for voice: ')

    # Read the bot.py content
    with open(bot_py_path, 'r') as file:
        lines = file.readlines()

    # Replace lines in bot.py
    lines[74] = f'SPOTIPY_CLIENT_ID = "{spotify_client_id}"\n'
    lines[75] = f'SPOTIPY_CLIENT_SECRET = "{spotify_client_secret}"\n'
    lines[520] = f'text_channel_id = {text_channel_id}\n'
    lines[1182] = f'bot.run("{discord_bot_token}")\n'

    # Write the updated lines back to bot.py
    with open(bot_py_path, 'w') as file:
        file.writelines(lines)

    print('Updated bot.py with your credentials.')

# Update bot.py with user inputs
update_bot_py()

setup(
    name='PanicPortal',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'discord.py',
        'requests',
        'pyautogui',
        'websockets',
        'mss',
        'sounddevice',
        'soundfile',
        'opencv-python',
        'gtts',
        'psutil',
        'pyaudio',
        'pycaw',
        'pynput',
        'pypresence',
        'spotipy',
        'pywin32',
        'pycryptodome',
    ],
    entry_points={
        'console_scripts': [
            'panicportal=bot:main',
        ],
    },
    include_package_data=True,
    description='PanicPortal: A Discord bot for emergency procedures and remote desktop control.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/haydenbanz/PanicPortal',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
    ],
)
