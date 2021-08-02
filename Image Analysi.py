from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

ENDPOINT = "https://image-analyzer1.cognitiveservices.azure.com/"
KEY = "3f8fb94c6c804e02b661a15997a76809"

image_url1 = "https://i.ibb.co/c8v6JP5/image.jpg"
image_url2 = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/landmark.jpg"

client = ComputerVisionClient(ENDPOINT, CognitiveServicesCredentials(KEY))
description = client.describe_image(image_url1)

for caption in description.captions:
  print(caption.text)

