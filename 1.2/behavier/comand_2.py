class PDFDocument:
    def __init__(self):
        self.commands = {
            'save': SaveCommand(self),
            'open': OpenCommand(self),
        }

    def save(self):
        print('Saving PDFDocument')

    def open(self):
        print('Opening PDFDocument')

    def execute_command(self, command_name):
        self.commands[command_name].execute()

class XMLDocument:
    def __init__(self):
        self.commands = {
            'save': SaveCommand(self),
            'open': OpenCommand(self),
        }

    def save(self):
        print('Saving XMLDocument')

    def open(self):
        print('Opening XMLDocument')

    def execute_command(self, command_name):
        self.commands[command_name].execute()



class SaveCommand:
    def __init__(self, document: PDFDocument):
        self.document = document

    def execute(self):
        print('SOME CODE 1')
        self.document.save()
        print('SOME CODE 2')


class OpenCommand:
    def __init__(self, document: PDFDocument):
        self.document = document

    def execute(self):
        self.document.open()


if __name__ == '__main__':
    doc1 = PDFDocument()
    doc1.execute_command('save')  # Saving
    doc1.execute_command('open')  # Opening

    doc2 = XMLDocument()
    doc2.execute_command('save')  # Saving
    doc2.execute_command('open')  # Opening

