import subprocess
import json

import os
import platform

# install homebrew because.
list = ['cd ~'
'mkdir autoScript',
'cd autoScript',
'ruby -e "$(curl -fsSkL raw.github.com/mistydemeo/tigerbrew/go/install)"']

#atom #sublime
#firefox
#numpy
#scipy
#android studio
#flux


# install latest stable python version

# Hardware available at hardware.mlh.io that require files are:
# Myo - C
# Arduino, Intel Edison - Arduino
# spark - spark
# oculus



# the list will take a list of software names and the installation command in a dictionary.

def pushToStorage():
    d = {"one":1, "two":2}
    json.dump(d, open("text.txt",'w'))

def installMenu(softwareDisc):




    message = "Please select from the list "

    print(message)

hardwareSoftware = ["spark":"brew install %d",
"adafruit-arduino":"brew install %d",
"arduino":"brew install %d",
"galileo-arduino":"brew install %d",
"myo-connect":"brew install %d"
]

def brewInstall():

    list = ['brew update',
    'brew install python3',
    'brew install node',
    'brew upgrade node',
    'brew install git'
    'brew install ghc cabal-install',
    'cabal update',
    'cabal install ghc-mod',
    'brew tap homebrew/versions',
    'brew install gcc48',
    'brew tap caskroom/cask',
    'brew cask install google-chrome',
    "brew cask install atom",
    "brew cask install mactex",
    "pip install numpy",
    "brew install gfortran",
    "pip install scipy",
    "pip install matplotlib",
    ]

    for i in brewInstall:
        subprocess.call(i,shell=True)
