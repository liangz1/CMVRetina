from .Inception import InceptionDR
from PIL import Image
import numpy as np
from .preprocess import preprocess

def predict(image_path: str, best_model) -> float:
    """

    :param image_path: str: path to image to be evaluated
    :param best_model: model
    :return: probability of having DR
    """
    pic = Image.open(image_path)
    pix = np.array(pic.getdata()).reshape(pic.size[0], pic.size[1], 3)

    pix = preprocess(pix)/255
    pix = np.expand_dims(pix, axis=0)

    # model = InceptionDR("eval")
    # model.load_best_model(best_model)
    y = best_model.model.predict(pix)
    return y[0][1]
