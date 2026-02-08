# Duck typing: it is a concept where the type of an object is determined
# by its behaviour not by  its class 
class InkjetPrinter:
    def printdocument(self,document):
        print("InkjetPrinter printing :",document)

class LaserPrinter:
    def printdocument(self,document):
        print("Laser Printer printing :",document)

class PDFWriter:
    def printdocument(self,document):
        print(f"Saving {document} as PDF")


def startprinting(device):
    device.printdocument("Marvellous Notes")

def main():
    startprinting(InkjetPrinter())
    startprinting(LaserPrinter())
    startprinting(PDFWriter())

main()