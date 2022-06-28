# BWB Code Repo
This is a temporary repo to store codes written for specific task during application process. The content will eventually be deleted or made private.


## How To Use
### Dependencies
```Console
conda create --name <env> --file requirements.txt
```  
- `requests`  
- `flask`  
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
├── server.py               # Flask server
├── reponse.json            # Reponse as JSON
├── requirements.txt        # Dependencies
└── .gitignore
```
After setting up dependencies, run [server.py](https://github.com/vhoangTS/bwb/blob/main/server.py) to boot Flask server and then [app.py](https://github.com/vhoangTS/bwb/blob/main/app.py) to get response with specific payload.


## Further notes
### `googlesearch` vs `google-api-python-client`? 
`google-api-python-client` is an officical [Google service](https://github.com/googleapis/google-api-python-client) which offers more functionalities than `googlesearch` package. 
For example it would me much easier and more straight forward to extract further information (i.e. website name, description) on search results. 
However it requires [API key](https://cloud.google.com/docs/authentication/api-keys). 

### Implementiere eine Authentifizierungs-/Autorisierungsmechanismus? 
As I have very limited knowledge in this topic, I just pretty much "winging it" with an assumption that the request body contain username/password and it is checked against a dummy user credentials database in order to identify: 1. if the user has access and 2. which access level? Based on this, the JSON reponse is different per each case.

### TODO:
- Store previous search to avoid having to search for every payloads
- Sign-in, Search page
