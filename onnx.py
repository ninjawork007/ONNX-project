import torch
import networks
import torch.nn as nn
from torch.autograd import Variable
import torch.onnx as torch_onnx
import trainer


# Use this an input trace to serialize the model
input_shape = (3, 100, 100)
model_onnx_path = "torch_model.onnx"
model = trainer.UNIT_Trainer()
model.train(False)

# Export the model to an ONNX file
dummy_input = Variable(torch.randn(1, *input_shape))
output = torch_onnx.export(model, 
                          dummy_input, 
                          model_onnx_path, 
                          verbose=False)
print("Export of torch_model.onnx complete!")
