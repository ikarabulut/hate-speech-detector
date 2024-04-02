import torch
from torch.utils.data import DataLoader, TensorDataset
import pytorch_lightning as pl


class ClassificationData(pl.LightningDataModule):
    BATCH_SIZE = 32

    def __init__(self, train_tokens, test_tokens, train_labels, test_labels):
        super().__init__()

        train = [train_tokens["input_ids"], train_tokens["attention_mask"],
                 train_tokens["token_type_ids"], torch.tensor(train_labels)]
        test = [test_tokens["input_ids"], test_tokens["attention_mask"],
                test_tokens["token_type_ids"], torch.tensor(test_labels)]

        self.trn = DataLoader(TensorDataset(
            *train), batch_size=self.BATCH_SIZE)
        self.test = DataLoader(TensorDataset(
            *test), batch_size=self.BATCH_SIZE)

    def train_dataloader(self): return self.trn
    def test_dataloader(self): return self.test
