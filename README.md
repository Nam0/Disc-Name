# AI Project - Self Replication AI

This repository contains various scripts and modules used for the development of an AI model based on personal data for building, cleaning, training, and fine-tuning the AI. idk about the panda frame stuff tbh that shit is weird to me

## Current Status
So far each iteration has been a failure, Jerry spoke decently but was dumb in conversations, Jimmy was alright but would flop after hitting a token limit of like 90 Tiny Jimmy was even worse but at 64 tokens barely 2 sentences

## Future Plans
Im prolly gonna toss the discord data just try to generate more data with Replika as it's more of a conversational flow vs me shit posting in discord chats and dms less sensitive data in there for the model to expose.

Need to figure out a way to correctly retrain and fine tune premade models to see if I can incorporate intelligence into it other than just feeding Jimmy GPT2 markdown formatting stuff and 40k books for shits and gigles while it slowly dies on my harddrives.

### Data Pulling
- **Discord Data**: Pulled using https://github.com/Tyrrrz/DiscordChatExporter
- **Replika AI Data**: Pulled using https://github.com/Nam0/Replika_Chat_Export_Extension


## Project Structure

### Atmpt4
- **dl.py**: Handles model download and setup
- **test.py**: Tests the trained model with given input
- **training.py**: Script for training the model on personal data

### DataCleaning
- **Adjust.py**: Combindes consecutive lines
- **Combinder.py**: Combines multiple jsons into one json file
- **Compress.py**: Combindes multiple files into one txt file
- **ConvoGrepping.py**: Extract json data based on author
- **ConvoLinking.py**: Poorly links conversations based on time
- **data_processor.py**: Panda Frame BS
- **Emojibs.py**: Strips emojis
- **main.py**: Datacleaning shit but it dont work
- **message.py**: Another emoji removing thing and reformating lines
- **morph.py**: Diff formatting
- **NumFix.py**: Reorders conversation from convo linking and convo grepping
- **Ordering.py**: Ditto ^
- **outlierfix.py**: Attempts to merge and integrate outliers poorly
- **preprocessing.py**: Panda Frame BS
- **Reformating.py**: Filters URLs, changes filenames and saves it
- **report_generator.py**: PandaFrame report generator thing
- **shortener.py**: Token Limiting stuff
- **utils.py**: More Pandaframe stuff I found couldnt get any of it to work the way I wanted tho

### Garbage
- **model_training.py**: Training and fine tuning stuff for Jerry

### New
- **FineTune.py**: Fine tuning I think Idk if I really used this one tbh
- **HRU.py**: OG Text chat with Jerry
- **nam3.py**: Poorly trying to integrate Jerry into Llama3
- **ReReTrain.py**: ReTraining Jerry to make him smarter
- **Retrain.py**: Another Retraining script

### Retrained
- **cuda.py**: Cuda Stats
- **cudatest.py**: Tests if CUDA is properly set up
- **load.py**: Mistral Load
- **Retrain.py**: Retraining for TinyJimmyV2
- **test2.py**: Dialogue with Jimmy
- **Test.py**: Jimmy Finetuned loading and testing

### Streamlit
- **app.py**: The main script for the Streamlit web chat with Ai
