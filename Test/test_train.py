from SRC.train import train_model
def test_accuracy():
    acc=train_model()
    assert acc>0.7, "Accuracy is too low"