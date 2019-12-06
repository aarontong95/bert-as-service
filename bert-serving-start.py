from bert_serving_next_sentence_prediction.server import BertServer
from bert_serving_next_sentence_prediction.server.helper import get_run_args
with BertServer(get_run_args()) as server:
    server.join()
