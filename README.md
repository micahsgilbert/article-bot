# News Bot

## Usage

`python3 main.py -u <url>`

## Configuration

When creating an article class for a specific source, it should be an extension of the `Article` class. There are 4 functions needed. Call the `generate_description` fucntion to generate everything.

|function|inputs|return|
|--------|------|------|
|`get_title`|none|string|
|`get_date`|none|string|
|`enumerate_paragraphs`|none|bs4 array of `<p>` tags to be used|
|`assemble_text`|`<p>` tag array|string of summary|
