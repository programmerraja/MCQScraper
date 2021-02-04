# QuestionScraper
Scrap questions from sanfoundry website

<!-- TABLE OF CONTENTS -->

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

<p>I created the project for my online exam preparation.i used to study from the sanfoundry website for my exam.</p>
<p>The thing I hate from the website is I need to navigate lot to study so I get frusted</p>
<p>So I plan to write web scrapper using python that scrap all the questions from the website and put it on a single html file </p>

### Built With

<ol>
<li> Python</li>
<li> HTML</li>
<li> Css</li>
<li> Java Script</li>
</ol>


## Getting Started

Just clone this repository 

### Prerequisites

Need to have python3  

Package required for python scraper
<ol>
<li> BS4</li>
<li> Request</li>
</ol>

## Installation

To install bs4 

```
pip3 install bs4
```
To install request

```
pip3 install request
```

## Usage

<p> Add the link that you want to convert in to html file in the list</p>

```py
links=[link,....]
```
<p> Run the program by </p>


```
python3 MCQScraper.py
```

<p>once program finsihed running you will get the html file under the CSe folder</p>

### Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

<p> Write Scraper that scrap questions and answer from any other website and convert that in to the html file. and do the following</p>

1. Fork the Project
2. Create your Scraper Branch (`git checkout -b scraper/examvedascraper`)
3. Commit your Changes (`git commit -m 'Add some scraper'`)
4. Push to the Branch (`git push origin scraper/examvedascraper`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

