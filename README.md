# Ciscodocs - GPT-3

GPT-3 is a relativelly new NLP algorithm from OpenAI which produces very impressive results. 
It is very good in generalization and adapts very well to new inputs. It can be "trained" 
by feeding it custom knowledge material in text form. When providing Cisco's documentation
as a source of knowledge, it is possible to create a chatbot that is able to answer detailed 
questions about Cisco's products and services. And this is exactly what I am trying to do right now.

This is a WiP. So far, it is a simple offline python chatbot trained only on the DNA Center data sheet.
The end goal of course is to create a public available Webex bot based on a much bigger knowledge base.

But even with such a rather small "training set" the results are very promising:

If you would like to contribute, please contact me via e-mail (mdemikho@cisco.com) or Webex.

---
## Table of Contents
  * [1. Requirements](#1-requirements)
  * [2. Setup](#2-setup)
    + [Install required Python libraries](#install-required-python-libraries)
    + [Edit config file](#edit-config-file)
    + [Add knowledge base](#add-knowledge-base)
  * [3. Start chatting](#3-start-chatting)

---

## 1. Requirements

In order to run the bot you need Python 3 and the OpenAI python package and jsonlines.

Also, you need to have access to the GPT-3 API. More infos here:
https://openai.com/blog/openai-api/

---

## 2. Setup

Just copy the files to your host and follow the setup steps below.

### Install required Python libraries
Open up the terminal and type in:

```bash
pip3 install -r requirements.txt
```
### Edit config file
Just insert your GPT-3 API key in `config.json`

### Add knowledge base
Currently the bot is trained with the DNA Center data sheet. If you would like to add more training material, add it
to the `sources` folder. The knowledge base needs to be in text form and each chapter needs to be separated by `###`.
Thereafter, the file needs to be converted into a JSONLINES format and uploaded to the OpenAI cloud. This can be done
by `file2jsonl` and `uploadFile`functions of the `utils` library. Or just use `refreshtest.py`. It deletes the current
knowledge base and replaces it with the one you define. In order to use it, just replace the file paths in the code with
your own and you are good to go (but do not change the paths of `config.json` and `file_id`).

---

## 3. Start chatting
In order to chat with the bot, just start `main.py`

```bash
python main.py
```
