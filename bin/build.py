#! /usr/bin/env python3

import os
import sys
import markdown

BIN_DIR = os.path.realpath(os.path.dirname(__file__))
SOURCE_DIR = os.path.join(BIN_DIR, '..', 'source')
TARGET_FILE = os.path.join(BIN_DIR, '..', 'index.html')

DOCUMENT_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">

<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
<!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
<title>Scottish Football Pyramid Proposal</title>

<!-- Bootstrap -->
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css" integrity="sha384-HSMxcRTRxnN+Bdg0JdbxYKrThecOKuH5zCYotlSAcp1+c8xmyTe9GYg1l9a69psu" crossorigin="anonymous">

<!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
<!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
<!--[if lt IE 9]>
  <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
  <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
<![endif]-->
<style>
body {
    font-family: Arial;
    padding: 20px;
}
</style>
</head>

<body>

<h1>Scottish Football Pyramid Proposal</h1>

%s

</body>

</html>
'''[1:]

def main():
    document = DOCUMENT_TEMPLATE % build_body()
    with open(TARGET_FILE, 'w') as file_out:
        file_out.write(document)

def build_body():
    return '\n\n'.join(
        build_section(filename)
        for filename in sorted(os.listdir(SOURCE_DIR))
    )

def build_section(filename):
    filepath = os.path.join(SOURCE_DIR, filename)
    with open(filepath, 'r') as file_in:
        content = file_in.read()
    return '%s\n%s' % (build_header(filename), markdown.markdown(content))

def build_header(filename):
    header_name = filename.split('_', 1)[1].replace('.md', '')
    return '<h2>%s</h2>' % header_name.replace('_', ' ').title()

if __name__ == '__main__':
    exitcode = main()
    sys.exit(exitcode)
