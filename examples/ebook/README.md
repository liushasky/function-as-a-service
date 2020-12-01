# Deploy the function service at Local

```bash
pip install .
python -m nltk.downloader -d /usr/share/nltk_data punkt
faas-start --target text_processing
cd examples/ebook
pip install -r requirements.txt
```

Then open your browser with URL http://localhost:8080/?url=http://www.gutenberg.org/files/1342/1342-0.txt
or use curl 

```bash
curl http://localhost:8080/?url=http://www.gutenberg.org/files/1342/1342-0.txt
```

Note: using curl might crash because the response is a huge html histogram.

# Deploy the function service in Google Cloud Functions
## Prepare the container
