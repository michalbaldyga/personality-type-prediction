# MBTI Prediction using BERT

https://huggingface.co/docs/transformers/tasks/sequence_classification

## Installation of all necessary libraries:
`pip3 install transformers datasets evaluate scikit-learn`\
`pip3 install git+https://github.com/JustAnotherArchivist/snscrape.git`

## PyTorch for Windows:
`pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117`

Using the `Trainer` with `PyTorch` requires `accelerate`: Run `pip3 install --upgrade accelerate`


## Additional improvement:
If you want to use `memorry_efficient_attention` to accelerate training use the following command to install Xformers: `pip3 install xformers`
