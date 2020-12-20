# <center>![](images/introduction.png)** Details **</center>

---

**Streamlit** is a python library that makes easy to create and share the web applications with out html, css and javascript.

#### <u> ** 1. Pre-requisites ** </u>
- Python Version > 3.6

#### <u> ** 2. Installation ** </u>
- [x] **Standalone**
    - pip install streamlit
    - streamlit hello

- [x] **Anaconda**
    - conda create --name streamlit (create new environment)
    - conda activate streamlit (activate)
    - pip install streamlit
    - streamlit hello
    - conda deactivate (to deactivate )

- [x] **Venv** (Built in python no need to do pip install)
    - python -m venv streamlit (create new environment)
    - cd pathtostreamlit\Scripts\activate.bat (activate)
    - pip install streamlit
    - streamlit hello
    - cd pathtostreamlit\Scripts\deactivate.bat (deactivate)

- [x] **Virtualenv**
    - pip install virtualenv
    - virtual streamlit (create new environment)
    - cd pathtostreamlit\Scripts\activate.bat (activate)
    - pip install streamlit
    - streamlit hello
    - cd pathtostreamlit\Scripts\deactivate.bat (deactivate)

- [x] **Pipenv**
    - pip install pipenv
    - pipenv install streamlit
    - pipenv shell or pipenv run (activate)
    - streamlit hello
    - exit (deactivate)

#### <u> ** 3. Uninstallation ** </u>
- pip uninstall streamlit

#### <u> ** 4. Commands ** </u>
- [x] **Basic Commands**
    - streamlit --help
    - streamlit hello
    - streamlit config show
    - streamlit cache clear
    - streamlit docs
    - streamlit --version

- [x] **Run Command**
    - streamlit run scriptname.py
    - streamlit run 'url.py' (Github or Gist)
        - **Gist Example** - streamlit run https://gist.github.com/SurendraRedd/feaa6f29961501fa9fce7a45abc14651/raw/Example.py
        - **GitHub Example** - streamlit run https://github.com/SurendraRedd/StreamlitProjects/blob/master/Example.py
    - streamlit run app.py --server.port 8503 (to run in different port)

#### <u> ** 5. Run Gist/GitHub** </u>

=== "Gist Example"
    streamlit run https://gist.github.com/SurendraRedd/eaa6f29961501fa9fce7a45abc14651/raw/Example.py

=== "GitHub Example"
    streamlit run https://github.com/SurendraRedd/StreamlitProjects/blob/master/Example.py