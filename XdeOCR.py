import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from XdeOCR_window import Ui_MainWindow
from rapid_latex_ocr import LatexOCR
import os


PROJECT_DIR = os.path.dirname(__file__)
MODEL_DIR = os.path.join(PROJECT_DIR,"models")

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def init_model(self, model):
        self.label.init_model(model)
    

if __name__ == "__main__":
    
    model = LatexOCR()
    
    # if you want to generate .exe, please move the weights to `.\models` and use the following code
    # model = LatexOCR(config_path=os.path.join(MODEL_DIR, 'config.yaml'),
    #                  image_resizer_path=os.path.join(MODEL_DIR, 'image_resizer.onnx'),
    #                  encoder_path=os.path.join(MODEL_DIR, 'encoder.onnx'),
    #                  decoder_path=os.path.join(MODEL_DIR, 'decoder.onnx'),
    #                  tokenizer_json=os.path.join(MODEL_DIR, 'tokenizer.json'))
    

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.init_model(model=model)


    sys.exit(app.exec_())
