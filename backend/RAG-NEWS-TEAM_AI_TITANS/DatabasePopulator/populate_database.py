import chromadb
from chromadb.utils import embedding_functions
from parse_xml import XMLContentParser

def add_content_to_collection(collection, xml_file_path):
    parser = XMLContentParser(xml_file_path)
    parser.parse()
    extracted_data = parser.get_extracted_data()

    for index, data in enumerate(extracted_data):
        domain_tags = ", ".join(data['domains'])
        document_content = f"{data['title']} Domains: {domain_tags}"
        collection.add(
            documents=document_content,
            metadatas=[{'link': data['link']}],
            ids=[f'item_{index}']
        )

if __name__ == "__main__":
    client = chromadb.PersistentClient(path="DatabaseFiles/data")
    embed_function = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="sentence-transformers/sentence-t5-base"
    )

    health_collection = client.get_or_create_collection(name="Health", embedding_function=embed_function)
    science_collection = client.get_or_create_collection(name="Science", embedding_function=embed_function)
    sports_collection = client.get_or_create_collection(name="Sports", embedding_function=embed_function)
    tech_collection = client.get_or_create_collection(name="Technology", embedding_function=embed_function)

    add_content_to_collection(health_collection, 'G:/Gen_AI_4/DatabasePopulator/NewsXMLs/Health.xml')
    add_content_to_collection(science_collection, 'G:/Gen_AI_4/DatabasePopulator/NewsXMLs/Science.xml')
    add_content_to_collection(sports_collection, 'G:/Gen_AI_4/DatabasePopulator/NewsXMLs/Sports.xml')
    add_content_to_collection(tech_collection, 'G:/Gen_AI_4/DatabasePopulator//NewsXMLs/Technology.xml')

    print(health_collection.peek())