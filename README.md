# Google APIs Demo


## Setup

Setup your Google Cloud Client by following the instructions [here](https://cloud.google.com/natural-language/docs/quickstart-client-libraries#client-libraries-usage-python).

Download the service account file and move it to *~/.gce/

Clone the repo with:
```bash
$ mkdir ~/git
$ cd ~/git/
$ git clone https://github.com/athenian-robotics/google-apis-demo.git
```

Install required python modules with:
```bash
$ cd ~/git/google-apis-demo
$ pip install -r requirements.txt 
```

Add GOOGLE_APPLICATION_CREDENTIALS to your env to your *~/.bashrc*:
```bash
export GOOGLE_APPLICATION_CREDENTIALS=<path_to_service_account_file>
```

If you run an python script from within PyCharm, add *GOOGLE_APPLICATION_CREDENTIALS* and its value to 
the Run Configuration's "Environment variables".

## Sentiment Analysis

Test text with:
```bash
$ ./sentiment_analysis.py -t "I disagree very strongly"
$ ./sentiment_analysis.py -t "I agree very strongly"
```