```javascript
/** * * * * * * * * * * * * * * ** * * * * * * * ** * * * * * * * * * * * * * * * * * * * *
*                                                                                         *
*                                                                                         *
*         ___        _                        _           _  ___  ___      _     _        *
*        / _ \      | |                      | |         | | |  \/  |     (_)   | |       *
*       / /_\ \_   _| |_ ___  _ __ ___   __ _| |_ ___  __| | | .  . | __ _ _  __| |       *
*       |  _  | | | | __/ _ \| '_ ` _ \ / _` | __/ _ \/ _` | | |\/| |/ _` | |/ _` |       *
*       | | | | |_| | || (_) | | | | | | (_| | ||  __/ (_| | | |  | | (_| | | (_| |       *  
*       \_| |_/\__,_|\__\___/|_| |_| |_|\__,_|\__\___|\__,_| \_|  |_/\__,_|_|\__,_|       *
*                                                                                         *
*                                     Copyrights © 2019                                   *
*                             <Author name="Daniel Eze"                                   *
*                                url="https://twitter.com/theghostyced" />                *
*                                                                                         *
*                                                                                         *
* * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * * * * * * * * * * **  * */
```

<p align="center">
  <a href="#">
    <img alt="SProgress" title="SProgress" src="https://forthebadge.com/images/badges/built-with-love.svg">
  </a>
  <a href="#">
    <img alt="SProgress" title="SProgress" src="https://forthebadge.com/images/badges/made-with-python.svg">
  </a>
</p>

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

## Introduction

Automated maid is a python 🐍 script that watches a particular directory and help organise the directory by grouping and sorting files according to their extension
type and date created.
<br />

It should look something like this 👇
<br />

![Automated Maid](/images/am.png)

## Setup

To install, git clone this brandh by running,

```bash

$ git clone <BRANCH_NAME> <OPTIONAL_FOLDER_NAME>
$ cp env/.env.example env/.env
```

then open the `env/.env` file and add the directory path you want to watch. 

then run the following `pipenv install` if you don't have `pipenv` I recommend installing it. Follow this [link](https://github.com/pypa/pipenv) to do so.

### Usage

After installing the required packages, you can simply make use of it by running the following command.

```bash

$ pipenv shell
$ python init.py
```
