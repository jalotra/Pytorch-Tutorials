# THis file creates a model using DenseNet Model


# Preparing the model
# Some tips to take care of
# The DenseModel requires a image input of the size (224, 224, 3).

# The preparation is done by the pytorch's torchvision module
# It gives us the methods to create a 1D tensor from the image pixels of the image
# THe resulting image-tensor size is (224*224*3, 1)

# Lets do some preproccessing
import io 
import torchvision.transforms as transforms
from PIL import Image
import json

# Transforms image into 3D tensor of size torch.Size([3, 224, 224]) 
def transform_image(image_bytes):
	my_transforms = transforms.Compose([transforms.Resize(255),
										transforms.CenterCrop(224),
										transforms.ToTensor(),
										transforms.Normalize(
											# Mean and Std deviation given are
											# First list is mean and second is for std
											[0.485, 0.456, 0.406], 
											[0.229, 0.244, 0.225 ])])

	image = Image.open(io.BytesIO(image_bytes))

	return my_transforms(image).unsqueeze(0)

# Lets define the Densenet Model
from torchvision import models
def model_define():
	model = models.densenet121(pretrained= True)
	model.eval()
	return model

def get_prediction(image_bytes):
	model = model_define()
	json_data = json.load(open('./imagenet_class_index.json'))
	tensor = transform_image(image_bytes)
	outputs = model.forward(tensor)
	_, y_predicted = outputs.max(1)
	predicted_idx = str(y_predicted.item())
	return json_data[predicted_idx]



if __name__ == "__main__":
	with open("./pokemon.jpeg", 'rb') as f:
		image_bytes = f.read()
		print(get_prediction(image_bytes))