from captaincloud.task import field
from captaincloud.task import Task, TaskImpl

import codecs


class WriteTextFileImpl(TaskImpl):
    def run(self):
        Input = self.task.Input
        with codecs.open(Input.filepath, 'w', encoding=Input.encoding) as fd:
            data = Input.stream.read(self.task.Input.buffersize)
            while data:
                fd.write(data)
                data = Input.stream.read(self.task.Input.buffersize)
            fd.close()


class WriteTextFile(Task):
    ID = 'cctasks.file.text.writer'
    NAME = 'Write Text File'
    impl = WriteTextFileImpl

    class Input:
        filepath = field.StringField()
        buffersize = field.IntegerField(default=102400)
        encoding = field.StringField(default='utf8')
        stream = field.StringStreamField()

    class Output:
        pass


class WriteBinaryFileImpl(TaskImpl):
    def run(self):
        Input = self.task.Input
        with open(Input.filepath, 'wb') as fd:
            data = Input.stream.read(self.task.Input.buffersize)
            while data:
                fd.write(data)
                data = Input.stream.read(self.task.Input.buffersize)
            fd.close()


class WriteBinaryFile(Task):
    ID = 'cctasks.file.binary.writer'
    NAME = 'Write Binary File'
    impl = WriteBinaryFileImpl

    class Input:
        filepath = field.StringField()
        buffersize = field.IntegerField(default=102400)
        stream = field.ByteStreamField()

    class Output:
        pass
