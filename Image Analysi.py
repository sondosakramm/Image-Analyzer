from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

ENDPOINT = "YOUR ENDPOINT"
KEY = "YOUR KEY"

image_url1 = "https://i.ibb.co/c8v6JP5/image.jpg"
image_url2 = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/landmark.jpg"

client = ComputerVisionClient(ENDPOINT, CognitiveServicesCredentials(KEY))
description = client.describe_image(image_url1)

for caption in description.captions:
  print(caption.text)

