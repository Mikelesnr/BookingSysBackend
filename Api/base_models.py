
class BaseModel:
    def __init__(self, **kwargs):
        self.model = kwargs.get('model')
        self.serializer = kwargs.get('serializer')
        self.request = kwargs.get('request')

    def get_all(self):
        model = self.model.objects.all()
        serializer = self.serializer(model, many=True)
        return serializer.data

    def add(self):
        serializer = self.serializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        return False

    def get_one(self, entry):
        serializer = self.serializer(entry)
        return serializer.data

    def edit_entry(self, entry):
        serializer = self.serializer(entry, data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        return serializer.errors

    def delete_entry(self, entry):
        entry.delete()
