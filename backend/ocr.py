from io import BytesIO

from PIL import Image
from transformers import TrOCRProcessor, VisionEncoderDecoderModel

processor = None
model = None


def load():
    global processor, model
    processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-handwritten")
    model = VisionEncoderDecoderModel.from_pretrained("trained")


def test_image(img: bytes) -> str:
    fp = BytesIO(img)
    im = Image.open(fp).convert("RGB")
    pixel_values = processor(im, return_tensors="pt").pixel_values
    generated_ids = model.generate(pixel_values)
    return processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
