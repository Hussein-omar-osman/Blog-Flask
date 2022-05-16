## Blogster

This is a Blog flask application that can allow users to create blog posts for other users to view and comment

## Author Information

Written by Hussein Omar. My first class in using flask(a python framework)

## Installation

Clone the repository
Create a virtual environment and install flask in your repository folder
Run the IP address on the browser

## User Stories

These are the behaviours/features that the application implements for use by a user.

As a user I would like to:

- Can create an account and receive a welcoming e-mail.
- Can log in to his or her account.
- Can create a blog post.
- Can see all the blog post of other users in the home page and blogs page.
- Can comment on a blog post .

## Behaviour Driven Development

| Behavior                         | Input description | Output description                             |
| -------------------------------- | ----------------- | ---------------------------------------------- |
| Create a new account             | None              | Account will be created and logged in          |
| Create a new blog post for other | None              | A new blog will be added to the home page      |
| Add a comment to any blog        | None              | The comment will be shown below the exact blog |

## SetUp / Installation Requirements

### Prerequisites

- python3.9
- pip
- virtualenv

## Running the Application

- Creating the virtual environment

        $ python3.10.4 -m venv --without-pip env
        $ source env/bin/activate
        $ curl https://bootstrap.pypa.io/get-pip.py | python

- Installing Flask and other Modules

        $ python3.10.4 -m pip install Flask
        $ python3.10.4 -m pip install Flask-Bootstrap
        $ python3.10.4 -m pip install Flask-Script

## Technologies Used

- Python3.10.4
- Flask

## Contact Information

To reach me, email me at: > husseinomar6190@gmail.com

License
MIT License

Copyright (c) [2022] [**Hussein Omar**]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
