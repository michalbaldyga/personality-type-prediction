
# MBTI Prediction using BERT

The BERT model was proposed in BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding by Jacob Devlin, Ming-Wei Chang, Kenton Lee and Kristina Toutanova. It’s a bidirectional transformer pretrained using a combination of masked language modeling objective and next sentence prediction on a large corpus comprising the Toronto Book Corpus and Wikipedia.


## Installation

Installation of all necessary libraries:

```bash
  pip3 install transformers datasets evaluate scikit-learn
  pip3 install git+https://github.com/JustAnotherArchivist/snscrape.git
```

PyTorch for Windows:

```bash
  pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117
```

Using the `Trainer` with `PyTorch` requires `accelerate`: Run `pip3 install --upgrade accelerate`
    
## Optimizations

If you want to use `memorry_efficient_attention` to accelerate training use the following command to install Xformers: `pip3 install xformers`

## Training

In order to train the model, head to `train_model` directory and run `train.py`

```bash
  cd backend/train_model/
  python3 train.py
```

The model will be saved in the `backend/model` directory

## Documentation

https://huggingface.co/docs/transformers/tasks/sequence_classification

## License

[MIT](https://choosealicense.com/licenses/mit/)

