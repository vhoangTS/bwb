# BWB Code Repo
This is a temporary repo to store codes written for specific task during application process. The content will eventually be deleted or made private.


## How To Use
### Dependencies
```Console
conda create --name <env> --file requirements.txt
```  
- `requests`  
- `pandas`  
- `googlesearch`

### Content
```
.
├── src/
│   └── auth.py             # Authetication & authorization modules
│   ├── search.py           # Google search
│   └── database.pickle     # User credentials database
├── app.py                  # Main application
├── reponse.json            # Reponse as JSON
├── requirements.txt        # Dependencies
└── .gitignore
```
After setting up dependencies, run [app.py](https://github.com/vhoangTS/bwb/blob/main/app.py) to test the code.
You can modify values of `payload` body to test different scenarios.

```python
if __name__ == '__main__':
    # Request body
    payload = {
        'username': 'vhoang',
        'password': 'bar',
        'keyword': 'bosch',
        'nr_results': 10}

    # Output as json
    # r = to_json(response(payload))

    # Output to file
    to_json_file(response(payload))
```

## JSON Response

### Scenario 1: User does not exists (not found in `database.pickle`)
```json
{
    "code": "401: Unsuccessful authentication.",
    "number-search-results": 10,
    "permission": "no-access",
    "search-data": "",
    "search-keyword": "bosch"
}
```

### Scenario 2: User found with `limited` access.
The program returns a JSON with link and short description of the website. Short description means the program only extract the first content wrapped in `description` tag in html data. 
Example of html data with `description` tag:
```html
<meta name="description" content="Moving stories and inspiring interviews. Experience the meaning of &#34;invented for life&#34; by Bosch completely new. Visit our international website."> 
```

### Scenario 3: User found with `limited` access.
The program returns a JSON with link and complete description of the website. Complete description means the program extract all the content wrapped in `description` tag in html data. Some website has shot description == complete description but not all.
```json
{
    "code": "200: Sucessful authentication.",
    "number-search-results": 10,
    "permission": "limited",
    "search-data": {
        "search_result_0": {
            "description": "Technik fürs Leben: Unsere Produkte begeistern Menschen, verbessern ihre Lebensqualität und tragen zur Schonung der natürlichen Ressourcen bei.",
            "link": "https://www.bosch.de/"
        },
        "search_result_1": {
            "description": "Aufgrund der hohen Innovationskraft begeistert Bosch mit überraschend einfachen Lösungen in ästhetisch-funktionalem Design.",
            "link": "https://www.bosch.de/produkte-und-services/"
        },
        "search_result_2": {
            "description": "Bosch bietet Ihnen individuelle Lösungen für Ihr Zuhause, um Ihr Leben jeden Tag ein wenig einfacher zu machen.",
            "link": "https://www.bosch.de/produkte-und-services/zuhause/"
        },
        "search_result_3": {
            "description": "Grow. Enjoy. Inspire. Work #LikeABosch. Lernen Sie unseren globalen Arbeitgeber kennen und finden Sie Jobs weltweit. Willkommen bei Bosch Karriere.",
            "link": "https://www.bosch.de/karriere/"
        },
        "search_result_4": {
            "description": "Für alle Anliegen wenden Sie sich bitte an unsere Kundenberatung oder das Bosch Service Center +49 (0)711 400 40990. Hier ist man 24 Stunden am Tag, sieben Tage die Woche für Sie da.",
            "link": "https://www.bosch.de/kontakt/"
        },
        "search_result_5": {
            "description": "Technik fürs Leben: Unsere Produkte begeistern Menschen, verbessern ihre Lebensqualität und tragen zur Schonung der natürlichen Ressourcen bei.",
            "link": "http://www.bosch.de/"
        },
        "search_result_6": {
            "description": "",
            "link": "https://de.wikipedia.org/wiki/Datei:Bosch-logotype.svg"
        },
        "search_result_7": {
            "description": "",
            "link": "https://de.wikipedia.org/wiki/Robert_Bosch_GmbH"
        },
        "search_result_8": {
            "description": "Moving stories and inspiring interviews. Experience the meaning of \"invented for life\" by Bosch completely new. Visit our international website.",
            "link": "https://www.bosch.com/"
        },
        "search_result_9": {
            "description": "Grow. Enjoy Inspire. Work #LikeABosch. Get to know our global employer and find jobs worldwide. Welcome to Bosch Careers.",
            "link": "https://www.bosch.com/careers/"
        }
    },
    "search-keyword": "bosch"
}
```


## Further notes
### Search: `googlesearch` vs `google-api-python-client`? 
`google-api-python-client` is an officical [Google service](https://github.com/googleapis/google-api-python-client) which offers more functionalities than `googlesearch` package. 
For example it would me much easier and more straight forward to extract further information (i.e. website name, description) on search results. 
However it requires [API key](https://cloud.google.com/docs/authentication/api-keys). 

### Search: Event handler
Currently there are no even handler for the search module. This should be looked into in future steps.

### Implementiere eine Authentifizierungs-/Autorisierungsmechanismus? 
As I have very limited knowledge in this topic, I just pretty much "winging it" with an assumption that the request body contain username/password and it is checked against a dummy user credentials database in order to identify: 1. if the user has access and 2. which access level? Based on this, the JSON reponse is different per each case.
