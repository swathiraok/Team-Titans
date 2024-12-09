import xml.etree.ElementTree as ET

class XMLContentParser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.xml_root = None
        self.extracted_data = []

    def parse(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        self.xml_root = ET.fromstring(content)

    def get_extracted_data(self):
        if self.xml_root is None:
            raise ValueError("XML not parsed. Call parse() first.")
        
        for item in self.xml_root.findall('.//item'):
            title = item.find('title').text
            link = item.find('link').text
            description = item.find('description').text
            domains = [category.text for category in item.findall('.//category[@domain]')]

            self.extracted_data.append({
                'title': title,
                'link': link,
                'description': description,
                'domains': domains
            })

        return self.extracted_data

if __name__ == '__main__':
    xml_path = "G:/Gen_AI_4/DatabasePopulator/NewsXMLs/Health.xml" # path for any particular article xml file
    parser = XMLContentParser(xml_path)
    parser.parse()
    data = parser.get_extracted_data()
    for entry in data:
        print(entry)