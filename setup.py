from setuptools import setup, find_packages

setup(
    name='PanicPortal',  # Package name
    version='1.0.0',  # Version number
    packages=find_packages(),  # Automatically find all packages under the current directory
    
    # Dependencies required by your package
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
    
    # Entry points for console scripts
    entry_points={
        'console_scripts': [
            'panicportal=bot:main',  # Command to run the bot
        ],
    },
    
    include_package_data=True,  # Include additional files specified in MANIFEST.in
    description='PanicPortal: A Discord bot for emergency procedures and remote desktop control.',
    long_description=open('README.md', encoding='utf-8').read(),  # Readme file
    long_description_content_type='text/markdown',  # Readme content type
    author='Your Name',  # Author information
    author_email='your.email@example.com',  # Author email
    url='https://github.com/haydenbanz/PanicPortal',  # Project URL
    classifiers=[
        'Programming Language :: Python :: 3',  # Python version compatibility
        'License :: OSI Approved :: MIT License',  # License information
        'Operating System :: Microsoft :: Windows',  # Operating system compatibility
    ],
)
