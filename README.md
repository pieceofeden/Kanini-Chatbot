# Kanini-Chatbot
A Conversational bot to assist users visting the website according to their respective needs.

## Pre-requisites
- [Microsoft Visual C++ Redistributable](https://docs.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170)
- [Anaconda](https://www.anaconda.com)

## Setting up the environment
- Open anaconda prompt

  ``` conda create -n "rasaenv" python==3.8 ```
  
  ``` conda activate rasa ```
  
## Installation
``` pip3 install -U --user pip && pip3 install rasa ```

## Training the NLU model
``` rasa train ```

## Accessing the bot from the terminal
``` rasa shell ```

## Starting the NLU and Actions server
- Run the below codes in two different terminals:
  
  ``` rasa run actions ```
  
  ``` rasa run --enable-api --cors "*" ```
  
 
