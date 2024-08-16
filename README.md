<p align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/6295/6295417.png" width="100" />
</p>
<p align="center">
    <h1 align="center">BOOK-SUMMARIZER</h1>
</p>
<p align="center">
    <em>Streamlined Book Insights: Unveil & Absorb Wisdom!</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/wazox23/book-summarizer?style=flat&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/wazox23/book-summarizer?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/wazox23/book-summarizer?style=flat&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/wazox23/book-summarizer?style=flat&color=0080ff" alt="repo-language-count">
<p>
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
</p>
<hr>

##  Quick Links

> - [ Overview](#-overview)
> - [ Features](#-features)
> - [ Repository Structure](#-repository-structure)
> - [ Modules](#-modules)
> - [ Getting Started](#-getting-started)
>   - [ Installation](#-installation)
>   - [ Running book-summarizer](#-running-book-summarizer)
>   - [ Tests](#-tests)
> - [ Project Roadmap](#-project-roadmap)
> - [ Contributing](#-contributing)
> - [ License](#-license)
> - [ Acknowledgments](#-acknowledgments)

---

##  Overview

The book-summarizer project aims to automate the process of summarizing books using AI. The main.py file orchestrates the summarization by extracting text from PDFs, generating prompts, and utilizing OpenAI to create summaries based on specified topics. The prompts.py file defines guidelines for expert text summarizers to extract insights from manuscripts. The project's core value lies in efficiently summarizing books, streamlining content digestion, and aiding in knowledge acquisition.

---

##  Features

|    |   Feature         | Description                                                                                                                      |
|----|-------------------|----------------------------------------------------------------------------------------------------------------------------------|
| ⚙️  | **Architecture**  | *The project adopts a simple modular architecture with clearly defined components. It follows a script-based execution flow.*          |
| 🔩 | **Code Quality**  | *The codebase maintains a good level of quality with consistent style and adherence to PEP 8 standards. Comments are used for clarity.* |
| 📄 | **Documentation** | *The project includes descriptive inline comments within the code files. However, comprehensive external documentation is missing.*    |
| 🔌 | **Integrations**  | *Key dependencies include Python for core functionalities and the `py` library for additional functionalities like PDF text extraction.* |
| 🧩 | **Modularity**    | *The codebase is moderately modular, allowing for reusability of components within the project. Separation of concerns is evident.*     |
| 🧪 | **Testing**       | *Testing frameworks and tools are not explicitly mentioned in the project. Manual testing may have been used during development.*       |
| ⚡️  | **Performance**   | *Performance seems satisfactory but could be enhanced by optimizing resource usage during PDF processing and summarization tasks.*        |
| 🛡️ | **Security**      | *No specific mention of security measures. Data protection and access control should be considered for any sensitive information handling.* |
| 📦 | **Dependencies**  | *Dependencies include Python and the `py` library. Any vulnerabilities in these libraries should be monitored and updated regularly.*   |


---

##  Repository Structure

```sh
└── book-summarizer/
    ├── __pycache__
    │   └── prompts.cpython-311.pyc
    ├── main.py
    ├── naval.pdf
    └── prompts.py
```

---

##  Modules

<details closed><summary>.</summary>

| File                                                                            | Summary                                                                                                                                                                                                                               |
| ---                                                                             | ---                                                                                                                                                                                                                                   |
| [main.py](https://github.com/wazox23/book-summarizer/blob/master/main.py)       | Code Summary:** `main.py` orchestrates book summarization in `book-summarizer`. It extracts text from PDF, generates prompts, and uses OpenAI for summarization based on provided topic.                                              |
| [prompts.py](https://github.com/wazox23/book-summarizer/blob/master/prompts.py) | Summary:**`prompts.py` serves to generate specific task prompts for expert text summarizers within the `book-summarizer` repository. It defines the format and guidelines for extracting insights on a given topic from a manuscript. |

</details>

---

##  Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

* **Python**: `version x.y.z`

###  Installation

1. Clone the book-summarizer repository:

```sh
git clone https://github.com/wazox23/book-summarizer
```

2. Change to the project directory:

```sh
cd book-summarizer
```

3. Install the dependencies:

```sh
pip install -r requirements.txt
```

###  Running book-summarizer

Use the following command to run book-summarizer:

```sh
python main.py
```

###  Tests

To execute tests, run:

```sh
pytest
```

---

##  Project Roadmap

- [X] `► INSERT-TASK-1`
- [ ] `► INSERT-TASK-2`
- [ ] `► ...`

---

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/wazox23/book-summarizer/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/wazox23/book-summarizer/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/wazox23/book-summarizer/issues)**: Submit bugs found or log feature requests for Book-summarizer.

<details closed>
    <summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
   ```sh
   git clone https://github.com/wazox23/book-summarizer
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.

Once your PR is reviewed and approved, it will be merged into the main branch.

</details>

---

##  License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

##  Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#-quick-links)

---
