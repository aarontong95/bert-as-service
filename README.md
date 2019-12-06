# bert-as-service_next_sentence_prediction
Using [bert-as-service](https://github.com/hanxiao/bert-as-service) to make next sentence prediction

## Get Started

#### 1. Download and Unzip a Pre-trained BERT Model
<table>
<tr><td><a href="https://storage.googleapis.com/bert_models/2018_10_18/uncased_L-12_H-768_A-12.zip">BERT-Base, Uncased</a></td><td>12-layer, 768-hidden, 12-heads, 110M parameters</td></tr>
<tr><td><a href="https://storage.googleapis.com/bert_models/2018_10_18/uncased_L-24_H-1024_A-16.zip">BERT-Large, Uncased</a></td><td>24-layer, 1024-hidden, 16-heads, 340M parameters</td></tr>
<tr><td><a href="https://storage.googleapis.com/bert_models/2018_10_18/cased_L-12_H-768_A-12.zip">BERT-Base, Cased</a></td><td>12-layer, 768-hidden, 12-heads , 110M parameters</td></tr>
<tr><td><a href="https://storage.googleapis.com/bert_models/2018_10_18/cased_L-24_H-1024_A-16.zip">BERT-Large, Cased</a></td><td>24-layer, 1024-hidden, 16-heads, 340M parameters</td></tr>
<tr><td><a href="https://storage.googleapis.com/bert_models/2018_11_23/multi_cased_L-12_H-768_A-12.zip">BERT-Base, Multilingual Cased (New)</a></td><td>104 languages, 12-layer, 768-hidden, 12-heads, 110M parameters</td></tr>
<tr><td><a href="https://storage.googleapis.com/bert_models/2018_11_03/multilingual_L-12_H-768_A-12.zip">BERT-Base, Multilingual Cased (Old)</a></td><td>102 languages, 12-layer, 768-hidden, 12-heads, 110M parameters</td></tr>
<tr><td><a href="https://storage.googleapis.com/bert_models/2018_11_03/chinese_L-12_H-768_A-12.zip">BERT-Base, Chinese</a></td><td>Chinese Simplified and Traditional, 12-layer, 768-hidden, 12-heads, 110M parameters</td></tr>
</table>

#### 2. Install the package
<pre>
pip install -r requirements.txt
</pre>

#### 3. Start the BERT service
<pre>
python bert-serving-start.py -model_dir ~/cased_L-24_H-1024_A-16/  -show_tokens_to_client -return_probit
</pre>
It will return the score instead of the probability if you don't pass the argument '-return_probit' 
#### 4. Use client to get the probability between sentences
<pre>
from bert_serving.client import BertClient
bc = BertClient()
bc.encode(['How old are you? ||| I am 18.'], show_tokens=True)
</pre>
Make sure to use ||| (with whitespace before and after) to divide two sentences.

#### 5. Result
<pre>
(array([[9.999869e-01, 1.315439e-05]], dtype=float32),
[['[CLS]','how','old','are','you','?','[SEP]','i','am','18','.','[SEP]']])
</pre>
It will return the probability that sentence B is the next sentence of sentence A [True,False]

## Reference
This repository is referenced from [bert-as-service](https://github.com/hanxiao/bert-as-service).
