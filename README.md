# Micronuclei detection

Utilizes pretrained networks to detect nuclei.

The main program in this package is `micronuclei_labeling.py` which will download any necessary models and run them on the given input image.

# Installation
- Clone this repository
- pip3 install -r requirements.txt

# Run example
`python3 micronuclei_labeling.py input_image.png output_image.png`

To get the resulting image as pure black and white without different values for each nucleus:

`python3 micronuclei_labeling.py input_image.png output_image.png --binarize`
