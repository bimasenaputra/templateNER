import pandas as pd
import logging
from seq2seq_model import Seq2SeqModel
logging.basicConfig(level=logging.INFO)
transformers_logger = logging.getLogger("transformers")
transformers_logger.setLevel(logging.WARNING)


train_data = pd.read_csv("./mit-restaurant/train.csv", sep=',').values.tolist()
train_df = pd.DataFrame(train_data, columns=["input_text", "target_text"])

model_args = {
    "reprocess_input_data": True,
    "overwrite_output_dir": True,
    "max_seq_length": 50,
    "train_batch_size": 3,
    "num_train_epochs": 10,
    "save_eval_checkpoints": False,
    "save_model_every_epoch": True,
    "evaluate_during_training": False,
    "evaluate_generated_text": True,
    "evaluate_during_training_verbose": True,
    "use_multiprocessing": False,
    "max_length": 25,
    "manual_seed": 4,
    "save_steps": 11898,
    "gradient_accumulation_steps": 1,
    "output_dir": "./exp/mit-restaurant-src"
}

# Initialize model
model = Seq2SeqModel(
    encoder_decoder_type="bart",
    encoder_decoder_name="facebook/bart-large",
    args=model_args,
    # use_cuda=False,
)



# Train the model
model.train_model(train_df, args=model_args)