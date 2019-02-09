import os

import requests
from lxml import html
from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def current_subscribers():
    page_content = requests.get('https://volksbegehren-artenvielfalt.de/rathausmeldungen/')
    tree = html.fromstring(page_content.content)

    numbers = tree.xpath('//tr[@data-row_id]/td[6]/text()')

    count = 0
    for number in numbers:
        number_as_text = '%s' % number
        count += int(number_as_text.replace('.', ''))

    return '%s' % count


if __name__ == '__main__':
    app.run(host=os.getenv('VC_HOST', '0.0.0.0'),
            port=os.getenv('VC_PORT', 5000))
