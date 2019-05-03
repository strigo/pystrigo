# pystrigo

`pystrigo` is Strigo's official Python REST API client and CLI. It allows to easily retrieve information from Strigo's REST API and to automate processes.

Visit [Strigo's REST API Reference](http://docs.strigo.io/api/reference) from more information on the API and on retrieving your `ORG_ID` and `API_KEY`.


## Installation

`pystrigo` supports Linux, Windows and OSX on Python 3.4+

```shell
git clone git@github.com:strigo/pystrigo.git
cd pystrigo
pip install .
```

To install the CLI run:

```shell
pip install .[cli]
```


## Usage

### Python

```python
from strigo import Strigo
from strigo.logger import log


ORG_ID = os.getenv('STRIGO_ORG_ID')
API_KEY = os.getenv('STRIGO_API_KEY')
STRIGO_API_ENDPOINT = 'https://app.strigo.io/api/v1'

# To have the logger log both requests and responses to the console
log.set_level('debug')

strigo = Strigo(org_id=ORG_ID, api_key=API_KEY, endpoint=STRIGO_API_ENDPOINT)

strigo.classes.get(class_id='DsAnDSjmPe2wnCRw2')
# >> GET /classes/DsAnDSjmPe2wnCRw2...
# >> GET /classes/DsAnDSjmPe2wnCRw2 response
# >>   status_code=200
# >>   data={
# >>     "result": "success",
# >>     "data": {
# >>         "id": "DsAnDSjmPe2wnCRw2",
# >>         "name": "Coding",
# >>         "owner": {
# >>             "id": "rMWNrMT2PCySh2PGo",
# >>             "email": "nir+1@strigo.io"
# >>         },
# >>         "resources": [
# >>             {
# >>                 "type": "lab_instance",
# >>                 "id": "oqgcyawx6PXsu4r43",
# >>                 "name": "Lab",
# >>                 "instance_type": "t2.large",
# >>                 "image_id": "ami-614dcd0e",
# >>                 "image_user": "ubuntu",
# >>                 "is_custom_image": false
# >>             }
# >>         ],
# >>         "presentation_notes": [],
# >>         "created_at": "2019-04-11T21:51:49.274Z"
# >>     }
# >> }

response = client.events.post({
    'class_id': 'DsAnDSjmPe2wnCRw2',
    'name': 'My Event',
    'owner': 'nir+1@strigo.io',
    'date_start': '2019-08-01 00:00:00.000Z',
    'date_end': '2019-08-01 01:00:00.000Z'
})
assert response.status_code == 200
event_id = response.data['id']
...

```

### CLI

```shell

$ siesta --help
Usage: siesta [OPTIONS] METHOD ENDPOINT [ARGUMENTS]...

Options:
  --help  Show this message and exit.

# e.g.
$ siesta GET classes :class_id="DsAnDSjmPe2wnCRw2"
...

$ siesta POST events \
    class_id="DsAnDSjmPe2wnCRw2" \
    name="My Event" \
    owner="nir+1@strigo.io" \
    date_start="2019-08-01 00:00:00.000Z" \
    date_end="2019-08-01 01:00:00.000Z"
...
```

