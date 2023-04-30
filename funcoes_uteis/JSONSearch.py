import json


class JSONSearch:

    def json_key_search(self, json_source, search_key):
        value_found = None
        
        if isinstance(json_source, str):
            try:
                value_found = self.json_key_search(json_source = json.loads(json_source), search_key=search_key)
            except Exception as e:
                pass

        elif isinstance(json_source, list):
            for json_element in json_source:
                if self.json_key_search(json_source=json_element, search_key=search_key) != None:
                    value_found = self.json_key_search(json_source=json_element, search_key=search_key)    

        elif search_key in json_source.keys():
            value_found = json_source[search_key]
        
        else:
            for key, value in json_source.items():
                if isinstance(value, list) or isinstance(value, dict) or isinstance(value, str):
                    if self.json_key_search(json_source=value, search_key=search_key) != None:
                        value_found = self.json_key_search(json_source=value, search_key=search_key)

        return value_found

if __name__=="__main__":
    JSONSearch()