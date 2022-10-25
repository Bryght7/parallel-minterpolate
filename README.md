<!-- PROJECT SHIELDS -->
<!--
See the bottom of this document for the declaration of the reference variables
-->

[![Project Status: Concept – Minimal implementation, the repository is only intended to be a limited example, demo, or proof-of-concept.](https://www.repostatus.org/badges/latest/concept.svg)](https://www.repostatus.org/#concept)
[![Issues][issues-shield]][issues-url]
[![MIT][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <p align="center">
  </p>
  <h2 align="center">parallel-minterpolate</h2>
  <p align="center">
    Parallelize video frame interpolation with FFmpeg.
    <br />
  </p>
</p>

<!-- TABLE OF CONTENTS -->

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Description](#description)
- [Options](#options)
- [Examples](#examples)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

- Windows only
- FFmpeg
- Python version 3.6+
- Installed `opencv-python` dependency:
  ```bash
  pip3 install opencv-python
  ```
- Only works with MP4 videos

## Installation

Retrieve the Python script:

- by cloning the repository:
  ```bash
  git clone https://github.com/Bryght7/parallel-minterpolate.git
  ```
- or directly retrieving the `parallel-minterpolate.py` source file.

## Description

**parallel-minterpolate** is a command-line program to help the user speed up the process of applying frame interpolation to longer videos, using the minterpolate filter from FFmpeg.

As that filter is only single threaded, a common practice is to split the videos into smaller chunks, process those in parallel, and join them back together. This tool generates and runs all the needed commands to do this, all at once.

```bash
py parallel-minterpolate.py inputVideo --split N [OPTIONS]
```

## Options

```
positional arguments:
  inputVideo            an input video file

options:
  -h, --help            show this help message and exit
  --split N             number of tasks to generate equally
  -o, --outputDir NAME  name of the output directory, default='output'
  --fps N               target FPS, default=60
  --shutdown            shutdown computer after tasks are completed
```

## Examples

```bash
py parallel-minterpolate.py input.mp4 --split 5
```

👆 Split the video `input.mp4` into `5` roughly equal chunks, apply the minterpolate filter to them, and join them back together.

```bash
py parallel-minterpolate.py input.mp4 --split 5 --shutdown
```

👆 Same but the computer shuts down when it is done. Useful for overnight tasks.

## Usage

After executing the Python script, with option `--split 5` for example, you should see `5` different command-line windows open, those are the parallel frame interpolation tasks. Do not close any of them and let them work.

When it is finished, everything should auto close, and you should see the result as a `final.mp4` file inside an newly created `output` directory (this can be changed using the `-o` option).

## Contributing

This script was originally developed hastily and without any serious testing. Therefore it probably contains bugs, may not work under all circumstances, or lack many options/features. Any contributions you make to improve this script are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m '✨ Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE.md` for more information.

<!-- MARKDOWN LINKS & IMAGES -->

[issues-shield]: https://img.shields.io/github/issues/Bryght7/parallel-minterpolate
[issues-url]: https://github.com/Bryght7/parallel-minterpolate/issues
[license-shield]: https://img.shields.io/github/license/Bryght7/parallel-minterpolate
[license-url]: https://github.com/Bryght7/parallel-minterpolate/blob/master/LICENSE.md
