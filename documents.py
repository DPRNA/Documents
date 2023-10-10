import typing


class Document(typing.NamedTuple):
    doc_id: str
    text: str


class TransformedDocument(typing.NamedTuple):
    doc_id: str
    terms: list[str]


class ListDocumentStore:
    def __init__(self):
        self.docs = []

    def add_document(self, doc: Document):
        self.docs.append(doc)

    # *typing.Optional[Document]* is the same as *Document | None*
    def get_by_doc_id(self, doc_id: str) -> typing.Optional[Document]:
        for d in self.docs:
            if d.doc_id == doc_id:
                return d
        return None

    def list_all(self) -> list[Document]:
        return self.docs


class DictDocumentStore:
    def __init__(self):
        # dictionary to store docs
        # keys: IDS
        # values: docs
        self.docs = {}

    def add_document(self, doc: Document):
        # add doc to dictionary using its id as key
        self.docs[doc.doc_id] = doc

    def get_by_doc_id(self, doc_id: str) -> typing.Optional[Document]:
        # return doc related to given id with dictionary lookup
        return self.docs.get(doc_id)

    def list_all(self) -> list[Document]:
        # return list of all docments by getting values from dicitinary
        return list(self.docs.values())
