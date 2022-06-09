### News sentiment service app

Setup guide:

1. In nlp/:
    add a production directory with this structure:
        production:
            ---bert-base-uncased : download from hugging face)
            ---trained-bert : trained model saved with TFBertForSequenceClassification.save_pretrained method)
            ---label_encoder_classes.txt: classes for label encoder