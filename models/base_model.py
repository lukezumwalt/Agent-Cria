# models/base_model.py
from abc import ABC, abstractmethod

class LLMModel(ABC):
    '''
    Parent Base Model.  Serves as inheritance source for other llama instances.
    '''
    @abstractmethod
    def load_weights(self, checkpoint_path: str) -> None:
        """Load the model weights from the specified checkpoint."""

    @abstractmethod
    def infer(self, input_text: str) -> str:
        """Perform inference on the given input text and return the result."""

    @abstractmethod
    def save_checkpoint(self, checkpoint_path: str) -> None:
        """Save the model state to a checkpoint at the specified path."""
