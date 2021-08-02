from azure.cognitiveservices.vision.computervision import ComputerVisionClient

from msrest.authentication import CognitiveServicesCredentials


ENDPOINT = "https://image-analyzer1.cognitiveservices.azure.com/"
KEY = "3f8fb94c6c804e02b661a15997a76809"
IMAGE_URL = "C:\Users\SONDOS\Desktop\photo-1626296051075-13a2c43258f1.webp"

client = ComputerVisionClient(ENDPOINT, CognitiveServicesCredentials(KEY))
description = client.describe_image(IMAGE_URL)

for caption in description.captions:
  print(caption.text)
