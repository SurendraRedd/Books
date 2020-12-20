# <center>![](images/Code.png)** Example Snippets **</center>
---

#### <u> ** 1. Slider, SelectBox & Multiselect** </u>

- [x] **Usage of Slider, SelectBox & Multiselect**

        import streamlit as st
        import numpy as np

        x = st.slider('Select a value')
        st.write(x, 'squared value is', x * x)

        Exp = streamlit.selectbox("Choose your Experience: ", np.arange(1, 40, 1))

        lan = st.multiselect("Which is your favorite language?", 
                         ["Python", "JavaScript",
                         "Java", "C", "Julia"])

#### <u> ** 2. Dataframe** </u>

- [x] **Usage of dataframe**

        import pandas as pd
        import streamlit as st

        @st.cache
        def load_data():
            df = pd.read_csv("data.csv") # csv
            #df = pd.read_excel("data.excel") #excel
            return df

        # Will only run once if already cached
        df = load_data()

#### <u> ** 3. Notebook** </u>

- [x] **Jupyter Notebook**

        # Run jupyter notebook in streamlit using 3 steps below
        - jupyter nbconvert --to script scriptname.ipynb
        - awk '!/ipython/' scriptname.py > [temp.py](http://temp.py/) && mv [temp.py](http://temp.py/) [app.py](http://app.py/) && rm scriptname.py
        - streamlit run [app.py](http://app.py/)
        Refer the blog more details https://learnups2020.wordpress.com/2020/11/07/streamlit-code-running-from-jupyter-notebook/
        
#### <u> ** 4. Chart** </u>

- [x] **Altair Chart**

        # Alt Chart example
        import pandas as pd
        import numpy as np
        import altair as alt
        import streamlit as st

        df = pd.DataFrame(np.random.randn(100, 3), columns=['a', 'b', 'c'])
        c = alt.Chart(df).mark_circle().encode(x='a', y='b', size='c',  
                                        color='c')
        st.altair_chart(c, width=-1)

#### <u> ** 5. Database** </u>

- [x] **Simple Calculator App using sqlite DB**

        # Simple Calculator
        import pandas as pd
        from pathlib import Path
        import sqlite3
        from sqlite3 import Connection
        import streamlit as st

        URI_SQLITE_DB = "test.db"


        def main():
        st.title("Simple Calculator")
        st.markdown("Select two inputs from sidebar.")
        
        conn = get_connection(URI_SQLITE_DB)
        init_db(conn)

        build_sidebar(conn)
        display_data(conn)
        run_calculator(conn)


        def init_db(conn: Connection):
                conn.execute(
                        """CREATE TABLE IF NOT EXISTS test
                        (
                                INPUT1 INT,
                                INPUT2 INT
                        );"""
                )
                conn.commit()


        def build_sidebar(conn: Connection):
                st.sidebar.header("Inputs")
                input1 = st.sidebar.slider("value-1", 0, 100)
                input2 = st.sidebar.slider("value-2", 0, 100)
                if st.sidebar.button("Save to database"):
                        conn.execute(f"INSERT INTO test (INPUT1, INPUT2) VALUES ({input1}, {input2})")
                        conn.commit()


        def display_data(conn: Connection):
                if st.checkbox("Display data from the database"):
                        st.dataframe(get_data(conn))


        def run_calculator(conn: Connection):
                if st.button("Calculate Sum"):
                        st.info("Sum of two inputs function is called.")
                        df = get_data(conn)
                        st.write(df.sum())


        def get_data(conn: Connection):
                df = pd.read_sql("SELECT * FROM test", con=conn)
                return df


        @st.cache(hash_funcs={Connection: id})
        def get_connection(path: str):
                """Put the connection in cache to reuse if path does not change between Streamlit reruns.
                NB : https://stackoverflow.com/questions/48218065/programmingerror-sqlite-objects-created-in-a-thread-can-only-be-used-in-that-sa
                """
                return sqlite3.connect(path, check_same_thread=False)


        if __name__ == "__main__":
                main()

#### <u> ** 6. ProgressBar** </u>

- [x] **ProgressBar in sidebar and generate chart**

        import streamlit as st 
        import time 
        import numpy as np

        progress_bar = st.sidebar.progress(0)
        status_text = st.sidebar.empty()
        last_rows = np.random.randn(1, 1)
        chart = st.line_chart(last_rows)


        for i in range(1, 101):
        new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
        status_text.text("%i%% Complete" % i)
        chart.add_rows(new_rows)
        progress_bar.progress(i)
        last_rows = new_rows
        time.sleep(0.05)

        progress_bar.empty()

        st.button("Re-run")

#### <u> ** 7. Components** </u>

- [x] **Streamlit Components Example**

        import streamlit as st

        st.sidebar.subheader("Component 1")

        t1 = st.sidebar.text_input("Component 1 name")
        s1 = st.sidebar.slider("Component 1 value")

        st.sidebar.markdown("---")

        st.sidebar.subheader("Component 2")
        t2 = st.sidebar.text_input("Component 2 name")
        s2 = st.sidebar.slider("Component 2")

        st.title("Hello!")

        st.write(t1, s1)
        st.write(t2, s2)


        template = """
        <div class="markdown-text-container stText" style="width: 698px;">
        <div style="font-size: small;">This is paragraph 1 text.</div>
        <p>This is paragraph 2 text.</p>
        <p>This is paragraph 3 text.</p>
        </div>
        """

#### <u> ** 8. Code Share** </u>

- [x] **Streamlit Code Share Example**

        Prerequisites
        - pip install streamlit-embedcode
        import streamlit as st
        from streamlit_embedcode import github_gist, gitlab_snippet, pastebin_snippet, codepen_snippet, ideone_snippet, tagmycode_snippet

        st.title("Github Gist Snippet")
        github_gist("https://gist.github.com/SurendraRedd/feaa6f29961501fa9fce7a45abc14651")

        st.title("Gitlab Snippet")
        gitlab_snippet("https://gitlab.com/snippets/2037642", height=400)

        st.title("Pastebin Snippet")
        pastebin_snippet("https://pastebin.com/Ryr8q1kq", width = 600, scrolling = False)

        st.title("Code Pen Snippet")
        codepen_snippet("https://codepen.io/surendra1985/pen/wvGREBb", width = 600, scrolling = False)

        st.title("Ideone Snippet")
        ideone_snippet("https://ideone.com/tXCake")

        st.title("Tagmycode Snippet")
        tagmycode_snippet("https://tagmycode.com/snippet/14517/streamlit-basic-concepts#.X6fD8WgzZPY")