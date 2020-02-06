from torchvision.datasets import MNIST
from torchvision import transforms

from neuralmagicML.datasets.utils import DATASET_MAPPINGS


__all__ = ['MNISTDataset']


class MNISTDataset(MNIST):
    def __init__(self, root: str, train: bool = True):
        """
        Wrapper for MNIST dataset to apply standard transforms

        :param root: The root folder to find the dataset at, if not found will download here
        :param train: True if this is for the training distribution, false for the validation
        """
        transform = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize((0.5,), (1.0,))
        ])
        super().__init__(root, train, transform, None, True)


DATASET_MAPPINGS['mnist'] = MNISTDataset, 10