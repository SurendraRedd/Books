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