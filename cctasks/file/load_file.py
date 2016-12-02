from captaincloud.task import field
from captaincloud.task import Task, TaskImpl
from captaincloud.task.registry import TaskRegistry

import codecs
import six


class LoadTextFileImpl(TaskImpl):
    def run(self):
        Input = self.task.Input
        Output = self.task.Output
        with codecs.open(Input.filepath, encoding=Input.encoding) as fd:
            Output.data = fd.read()


@TaskRegistry.register
class LoadTextFile(Task):
    ID = 'cctasks.file.text.load'
    NAME = 'Load Text File'
    impl = LoadTextFileImpl

    class Input:
        filepath = field.StringField()
        encoding = field.StringField(default=six.u('utf8'))

    class Output:
        data = field.StringField()


class LoadBinaryFileImpl(TaskImpl):
    def run(self):
        Input = self.task.Input
        Output = self.task.Output
        with open(Input.filepath, 'rb') as fd:
            Output.data = fd.read()


@TaskRegistry.register
class LoadBinaryFile(Task):
    ID = 'cctasks.file.binary.load'
    NAME = 'Load Binary File'
    impl = LoadBinaryFileImpl

    class Input:
        filepath = field.StringField()

    class Output:
        data = field.ByteField()
