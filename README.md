# SkillsClasses
Main repository with all skills classes

### Workshop 1 - Julian

29/10/2024 - 13:00

**Recording**:

https://ucl.zoom.us/rec/share/FVLYWCoCKu2Z12xUrbx9NaJLq75dYMsqfZdrQnWXIVCq24ZvxqaZ6T-TW-vkyDSf.jbStV09RnKPhvQgC
Passcode: `dpDs3D*&`

Sorry I forgot to unpause recording after the break so there is a portion missing on the dimensionality reduction (See article by Miro Roman in homework, or check out the wikipedia page on SVD). There is also a part missing on the use of the LLM models but this should be self-explanatory based on the contents of the notebook.

**Homework**:

- Read Miro Roman's article in Eigen Architecture (https://liveuclac.sharepoint.com/:b:/r/sites/RC11-202425/Shared%20Documents/General/Resources/Literature/EigenArchitecture.pdf?csf=1&web=1&e=JSoZuE)
- Go through the lecture notebook and make sure you can run everything on your own computer with files of your choice. (ebook and pdf)  
- Start combining the many single line pieces of code in the lecture notebook into functions that are easy to use. Do this in a new notebook where you can start experimenting with the use of these techniques
  - first the preprocessing function
  - Then the vectorisation by tfidf and svd
- Once you have these aspects as functions start creating a combined function that returns the best `n` matches for a given search query in the function argument. the signature should be: `def search_paragraphs(query_text, n):`
- Figure out how to save a dictionary of processed text in a pickle file. Then also save the vectorised texts. This allows you to load your progress where you left off without having to run everything again (which can take long if you're working with many texts)
- Make it so that you are able to search in more than 1 book (at least 10)
- Then make similar functions that allow you to search for words with `w2v` and texts using an one of the two `llm` models shown in the lecture. 
- Compare the results of the different methods

_Suggestions:_
- Create one function in which you can you can specify which method you're using to search
- Make it so that it also works for a set of pdfs

_Challenge:_
- Read Miro Roman's Play among books and implement his word vectorisation based on books. (this is described in the appendix from page 288) (https://liveuclac.sharepoint.com/:b:/r/sites/RC11-202425/Shared%20Documents/General/Resources/Literature/PlayAmongBooks.pdf?csf=1&web=1&e=7QaJSr)
