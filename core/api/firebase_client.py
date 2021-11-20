import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from django.conf import settings

class FirebaseClient:

    
    def __init__(self):

        if not firebase_admin._apps: # Necessário para que não conecte novamente
            cred = credentials.Certificate(
                settings.FIREBASE_ADMIN_CERT # Importa a variável que contém os dados de conexão
            )
            firebase_admin.initialize_app(cred)
        

        self._db = firestore.client()
        self._collection = self._db.collection('resumo') # evento é o nome da coleção
  
    # GET ALL RESUMO
    def all(self):
        """Get all todo from firestore database"""
        docs = self._collection.get()
        docs = self._collection.stream()
        return [{**doc.to_dict(), "id": doc.id} for doc in docs]

    # GET RESUMO BY ID
    def get_by_id(self, id):
        """Get todo on firestore database using document id"""
        doc_ref = self._collection.document(id)
        doc = doc_ref.get()

        if doc.exists:
            return {**doc.to_dict(), "id": doc.id}
        return
        
    # INSERT RESUMO
    def create(self, data):
        """Create todo in firestore database"""
        doc_ref = self._collection.document()
        id = doc_ref.id
        data = {
            'id': id,
            'company': data['company'],
            'occupation': data['occupation'],
            'activities': data['activities'],
            'tags': data['tags'].split(),
            'start_date': data['start_date'],
            'departure_date': data['departure_date'],
        }
        doc_ref.set(data)
        
    # UPDATE RESUMO BY ID
    def update(self, id, data):
        """Update todo on firestore database using document id"""
        doc_ref = self._collection.document(id)
        data = {
            'id': id,
            'company': data['company'],
            'occupation': data['occupation'],
            'activities': data['activities'],
            'tags': data['tags'].split(),
            'start_date': data['start_date'],
            'departure_date': data['departure_date'],
        }
        doc_ref.update(data)
    
    # DROP RESUMO BY ID
    def delete_by_id(self, id):
        """Delete todo on firestore database using document id"""
        self._collection.document(id).delete()

    # FILTER RESUMO BY TAGS
    def filter(self, tags):
        docs = {}
        docs = self._collection.where("tags", "array_contains", tags).get()
        return docs

