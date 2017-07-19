![2017071915004751124509.png](http://7xihe6.com1.z0.glb.clouddn.com/2017071915004751124509.png)

# What is ErGo?
An intelligent bot based on TensorFlow.

ErGo comes with the following choices:

- chat: simple chat,only support Englist now.


## Features 

* NLP
* RNN
* Seq2seq
* QA

## Installation
The program requires the following dependencies (easy to install using pip):

- python 3.5+
- tensorflow (tested with v1.0+)
- numpy
- tqdm
- Flask (web interface)
- Redis (web interface)

## Usage

To train the model,simple run `main.py`.Before you chat ,you should train,just run `python3 main.py [-t chat] --train`.
Once trained,you can test the results with  `main.py [-t chat] --no-train` (have fun).

#### Results

```text
hello
-------------
master: hello
ergo:  hey .
``
What color ?
-------------
master: what color
ergo: i don 't know .
```

#### Data

- [data](https://dl.ysicing.net/download/tensorflow/)  
- [nltk](http://www.nltk.org/data.html) `nltk.download() `


