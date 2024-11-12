{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "fdbb05cd-7c24-466a-bc7a-79aad9830818",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Traceback (most recent call last):\n",
      "  File \"C:\\Users\\Patrick\\anaconda3\\envs\\urbandesignenv\\Lib\\site-packages\\nbconvert\\filters\\markdown_mistune.py\", line 24, in <module>\n",
      "    from mistune import (  # type:ignore[attr-defined]\n",
      "  File \"C:\\Users\\Patrick\\anaconda3\\envs\\urbandesignenv\\Lib\\site-packages\\mistune\\__init__.py\", line 4, in <module>\n",
      "    from .renderers import AstRenderer, HTMLRenderer\n",
      "ImportError: cannot import name 'AstRenderer' from 'mistune.renderers' (C:\\Users\\Patrick\\anaconda3\\envs\\urbandesignenv\\Lib\\site-packages\\mistune\\renderers\\__init__.py)\n",
      "\n",
      "During handling of the above exception, another exception occurred:\n",
      "\n",
      "Traceback (most recent call last):\n",
      "  File \"C:\\Users\\Patrick\\anaconda3\\envs\\urbandesignenv\\Scripts\\jupyter-nbconvert-script.py\", line 6, in <module>\n",
      "    from nbconvert.nbconvertapp import main\n",
      "  File \"C:\\Users\\Patrick\\anaconda3\\envs\\urbandesignenv\\Lib\\site-packages\\nbconvert\\__init__.py\", line 7, in <module>\n",
      "    from .exporters import (\n",
      "  File \"C:\\Users\\Patrick\\anaconda3\\envs\\urbandesignenv\\Lib\\site-packages\\nbconvert\\exporters\\__init__.py\", line 4, in <module>\n",
      "    from .html import HTMLExporter\n",
      "  File \"C:\\Users\\Patrick\\anaconda3\\envs\\urbandesignenv\\Lib\\site-packages\\nbconvert\\exporters\\html.py\", line 29, in <module>\n",
      "    from nbconvert.filters.markdown_mistune import IPythonRenderer, MarkdownWithMath\n",
      "  File \"C:\\Users\\Patrick\\anaconda3\\envs\\urbandesignenv\\Lib\\site-packages\\nbconvert\\filters\\markdown_mistune.py\", line 39, in <module>\n",
      "    from mistune import (  # type: ignore[attr-defined]\n",
      "  File \"C:\\Users\\Patrick\\anaconda3\\envs\\urbandesignenv\\Lib\\site-packages\\mistune\\__init__.py\", line 4, in <module>\n",
      "    from .renderers import AstRenderer, HTMLRenderer\n",
      "ImportError: cannot import name 'AstRenderer' from 'mistune.renderers' (C:\\Users\\Patrick\\anaconda3\\envs\\urbandesignenv\\Lib\\site-packages\\mistune\\renderers\\__init__.py)\n"
     ]
    }
   ],
   "source": [
    "!jupyter nbconvert --to script search_tools.ipynb"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a23631b7-bfe4-4e04-a19d-1620e49d730a",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Import Modules\n",
    "import os\n",
    "import pickle\n",
    "import numpy as np\n",
    "from sklearn.feature_extraction.text import TfidfVectorizer\n",
    "from sklearn.decomposition import TruncatedSVD\n",
    "from sklearn.metrics.pairwise import cosine_similarity"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "3ee7c932-9329-4250-b0ae-56fdc39826be",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Load Database (pickle_file)\n",
    "pickle_folder = \".\\pickle_file\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "2c30de68-fb3c-46a5-ad1e-e8c0f5ab6ed8",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Load all pickle files and merge into single database\n",
    "database = []\n",
    "for pickle_file in os.listdir(pickle_folder):\n",
    "    if pickle_file.endswith('.pkl'):\n",
    "        with open(os.path.join(pickle_folder, pickle_file), \"rb\") as f:\n",
    "            database.extend(pickle.load(f))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "2fa613d3-f80c-4208-beeb-66117117a026",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Simple Search\n",
    "def simple_search(query, num_results=5):\n",
    "    results = []\n",
    "    query = query.lower()\n",
    "    for entry in database:\n",
    "        if query in entry['KEYWORD'].lower():\n",
    "            results.append(entry)\n",
    "    \n",
    "    results = results[:num_results]\n",
    "    \n",
    "    for result in results:\n",
    "        print(f\"TEXT: {result['TEXT']}\\nLINE: {result['LINE']}\\nBOOK: {result['BOOK']}\\nKEYWORD: {result['KEYWORD']}\\n\")\n",
    "    \n",
    "    return results"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "51dd230f-08d1-48b7-ac3f-98f63c903ffe",
   "metadata": {},
   "outputs": [],
   "source": [
    "#TF-IDF Search\n",
    "def tfidf_search(query, num_results=5):\n",
    "    documents = [entry['KEYWORD'] for entry in database]\n",
    "    vectorizer = TfidfVectorizer(min_df=2)\n",
    "    tfidf_matrix = vectorizer.fit_transform(documents)\n",
    "    query_vec = vectorizer.transform([query.lower()])\n",
    "    scores = cosine_similarity(query_vec, tfidf_matrix).flatten()\n",
    "    top_indices = scores.argsort()[-num_results:][::-1]\n",
    "    \n",
    "    results = [database[i] for i in top_indices]\n",
    "    for result in results:\n",
    "        print(f\"TEXT: {result['TEXT']}\\nLINE: {result['LINE']}\\nBOOK: {result['BOOK']}\\nKEYWORD: {result['KEYWORD']}\\n\")\n",
    "    \n",
    "    return results, vectorizer, tfidf_matrix"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "a2a05aff-e549-49eb-abff-25a70fff1bf9",
   "metadata": {},
   "outputs": [],
   "source": [
    "def svd_search(query, num_results=5):\n",
    "    documents = [entry['KEYWORD'] for entry in database]\n",
    "    vectorizer = TfidfVectorizer(min_df=2)\n",
    "    tfidf_matrix = vectorizer.fit_transform(documents)\n",
    "    svd = TruncatedSVD(n_components=100)\n",
    "    svd_matrix = svd.fit_transform(tfidf_matrix)\n",
    "    query_vec = svd.transform(vectorizer.transform([query.lower()]))\n",
    "    scores = cosine_similarity(query_vec, svd_matrix).flatten()\n",
    "    top_indices = scores.argsort()[-num_results:][::-1]\n",
    "    top_terms = [vectorizer.get_feature_names_out()[idx] for idx in svd.components_.argsort()[::-1][:10]]\n",
    "    \n",
    "    results = [database[i] for i in top_indices]\n",
    "    for result in results:\n",
    "        print(f\"TEXT: {result['TEXT']}\\nLINE: {result['LINE']}\\nBOOK: {result['BOOK']}\\nKEYWORD: {result['KEYWORD']}\\n\")\n",
    "    \n",
    "    print(\"Top Keywords:\\n\")\n",
    "    for terms in top_terms:\n",
    "        print(terms)\n",
    "\n",
    "    return results, top_terms"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "64190e02-6b6e-4dee-9e6a-03e1ae8537d8",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Testing\n",
    "query = \"shop\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "d1fe1caa-15f7-4b89-ab39-60a1670ac972",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "TEXT:  Sonny was the only one happy there. His wife and daughters always seemed washed with dread and exhaustion. You would probably go past the small shop owned by Miss Jeanne and think the bottles of dinner mints and sweet plums dull.\n",
      "LINE: 38\n",
      "BOOK: A Map to the Door of No Return - Dionne Brand\n",
      "KEYWORD: sonni wa one happi wife daughter alway wash dread exhaust would probabl past small shop miss think bottl dinner mint sweet plum dull\n",
      "\n",
      "TEXT:  Being in the Diaspora braces itself in virtuosity or despair. 9 One has this sense as one observes bodies in the Diaspora, virtuosity or despair, on the brink of both. A body pushing a grocery cart through the city housing at Lawrence and Bathurst in Toronto, her laundry, her shopping all contained there, dressed as if on her way to a party, gold chain around her neck, lipstick — as if moving with all her possessions.\n",
      "LINE: 122\n",
      "BOOK: A Map to the Door of No Return - Dionne Brand\n",
      "KEYWORD: brace virtuos despair one ha sens one bodi virtuos despair brink bodi push groceri cart citi hous laundri shop dress way parti gold chain around neck lipstick move possess\n",
      "\n",
      "TEXT:  3 At seventeen on Raglan Avenue, it wasn’t wine but loneliness that woke me up to reach for Prevert, whose Paroles I had found in an old book shop. “Pierre tell me the truth” hissing through my sleep.\n",
      "LINE: 241\n",
      "BOOK: A Map to the Door of No Return - Dionne Brand\n",
      "KEYWORD: seventeen raglan avenu wine loneli woke reach whose parol found old book shop tell truth hiss sleep\n",
      "\n",
      "TEXT:  I know the narrowness of the street; I know the circus I’m walking toward. I know the pace of other pedestrians and I know how long I will have to wait at a coffee shop to be noticed and then to ask for my coffee.\n",
      "LINE: 347\n",
      "BOOK: A Map to the Door of No Return - Dionne Brand\n",
      "KEYWORD: know narrow street know circu walk toward know pace pedestrian know long wait coffe shop ask coffe\n",
      "\n",
      "TEXT:  I remember another shebeen — a rum shop, it’s called there — in a village in Dominica. One night some friends and I drive through country darkness, stopped where the car could go no further, and climbed a hill, bumping into tree stumps, arriving at a rum shop.\n",
      "LINE: 443\n",
      "BOOK: A Map to the Door of No Return - Dionne Brand\n",
      "KEYWORD: rememb anoth shebeen rum shop villag one night friend drive countri dark stop car could hill bump tree stump rum shop\n",
      "\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "[{'TEXT': ' Sonny was the only one happy there. His wife and daughters always seemed washed with dread and exhaustion. You would probably go past the small shop owned by Miss Jeanne and think the bottles of dinner mints and sweet plums dull.',\n",
       "  'LINE': 38,\n",
       "  'BOOK': 'A Map to the Door of No Return - Dionne Brand',\n",
       "  'KEYWORD': 'sonni wa one happi wife daughter alway wash dread exhaust would probabl past small shop miss think bottl dinner mint sweet plum dull'},\n",
       " {'TEXT': ' Being in the Diaspora braces itself in virtuosity or despair. 9 One has this sense as one observes bodies in the Diaspora, virtuosity or despair, on the brink of both. A body pushing a grocery cart through the city housing at Lawrence and Bathurst in Toronto, her laundry, her shopping all contained there, dressed as if on her way to a party, gold chain around her neck, lipstick — as if moving with all her possessions.',\n",
       "  'LINE': 122,\n",
       "  'BOOK': 'A Map to the Door of No Return - Dionne Brand',\n",
       "  'KEYWORD': 'brace virtuos despair one ha sens one bodi virtuos despair brink bodi push groceri cart citi hous laundri shop dress way parti gold chain around neck lipstick move possess'},\n",
       " {'TEXT': ' 3 At seventeen on Raglan Avenue, it wasn’t wine but loneliness that woke me up to reach for Prevert, whose Paroles I had found in an old book shop. “Pierre tell me the truth” hissing through my sleep.',\n",
       "  'LINE': 241,\n",
       "  'BOOK': 'A Map to the Door of No Return - Dionne Brand',\n",
       "  'KEYWORD': 'seventeen raglan avenu wine loneli woke reach whose parol found old book shop tell truth hiss sleep'},\n",
       " {'TEXT': ' I know the narrowness of the street; I know the circus I’m walking toward. I know the pace of other pedestrians and I know how long I will have to wait at a coffee shop to be noticed and then to ask for my coffee.',\n",
       "  'LINE': 347,\n",
       "  'BOOK': 'A Map to the Door of No Return - Dionne Brand',\n",
       "  'KEYWORD': 'know narrow street know circu walk toward know pace pedestrian know long wait coffe shop ask coffe'},\n",
       " {'TEXT': ' I remember another shebeen — a rum shop, it’s called there — in a village in Dominica. One night some friends and I drive through country darkness, stopped where the car could go no further, and climbed a hill, bumping into tree stumps, arriving at a rum shop.',\n",
       "  'LINE': 443,\n",
       "  'BOOK': 'A Map to the Door of No Return - Dionne Brand',\n",
       "  'KEYWORD': 'rememb anoth shebeen rum shop villag one night friend drive countri dark stop car could hill bump tree stump rum shop'}]"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "simple_search(query)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "7c6a75bb-82c3-48b5-830f-1835f6588a68",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "TEXT: Early on, we did everything we could to avoid exhibiting work in a white cube and everything it stood for. We showed in shop windows, homes, shopping centers, cafes, gardens. But always, the work became about the space itself, or the context, rather than the ideas we wished to explore.\n",
      "LINE: 623\n",
      "BOOK: Speculative Everything by Anthony Dunne\n",
      "KEYWORD: earli everyth could avoid work white cube everyth stood shop window home shop center garden alway work space context rather idea wish explor\n",
      "\n",
      "TEXT:  I remember another shebeen — a rum shop, it’s called there — in a village in Dominica. One night some friends and I drive through country darkness, stopped where the car could go no further, and climbed a hill, bumping into tree stumps, arriving at a rum shop.\n",
      "LINE: 443\n",
      "BOOK: A Map to the Door of No Return - Dionne Brand\n",
      "KEYWORD: rememb anoth shebeen rum shop villag one night friend drive countri dark stop car could hill bump tree stump rum shop\n",
      "\n",
      "TEXT:  This trend is also reflected in “free stores” or “give-away shops,” which work like second-hand shops, just without money and without the logic of exchange. These are not to be understood as places where things are “given,” that is, transferred from one private owner to another, but as places where people bring things that have “fallen out of possession,” since they are no longer used.\n",
      "LINE: 2568\n",
      "BOOK: Society After Money Dialogue\n",
      "KEYWORD: trend also reflect free store give away shop work like second hand shop without money without logic exchang understood place thing given transfer one privat owner anoth place peopl bring thing fallen possess sinc longer use\n",
      "\n",
      "TEXT:  On one of his visits to Sacramento he discovered an opportunity in commerce, and so opened a general store on K Street, not far from where Leland Stanford set up shop..\n",
      "LINE: 2106\n",
      "BOOK: The Age of Gold - H. W. Brands\n",
      "KEYWORD: one visit discov opportun commerc gener store street far set shop\n",
      "\n",
      "TEXT:  Being a ritual passage as a part of a pastoral Herculean landscape, the latter was like the Via Tecta in Pergamon in that it was multi-functional and included market halls and shops (Tilburg, 2007, p.\n",
      "LINE: 390\n",
      "BOOK: Architecture and the Body by Kim Sexton\n",
      "KEYWORD: ritual passag part pastor landscap latter wa like via wa function includ market hall shop\n",
      "\n",
      "TF-IDF Search: [{'TEXT': 'Early on, we did everything we could to avoid exhibiting work in a white cube and everything it stood for. We showed in shop windows, homes, shopping centers, cafes, gardens. But always, the work became about the space itself, or the context, rather than the ideas we wished to explore.', 'LINE': 623, 'BOOK': 'Speculative Everything by Anthony Dunne', 'KEYWORD': 'earli everyth could avoid work white cube everyth stood shop window home shop center garden alway work space context rather idea wish explor'}, {'TEXT': ' I remember another shebeen — a rum shop, it’s called there — in a village in Dominica. One night some friends and I drive through country darkness, stopped where the car could go no further, and climbed a hill, bumping into tree stumps, arriving at a rum shop.', 'LINE': 443, 'BOOK': 'A Map to the Door of No Return - Dionne Brand', 'KEYWORD': 'rememb anoth shebeen rum shop villag one night friend drive countri dark stop car could hill bump tree stump rum shop'}, {'TEXT': ' This trend is also reflected in “free stores” or “give-away shops,” which work like second-hand shops, just without money and without the logic of exchange. These are not to be understood as places where things are “given,” that is, transferred from one private owner to another, but as places where people bring things that have “fallen out of possession,” since they are no longer used.', 'LINE': 2568, 'BOOK': 'Society After Money Dialogue', 'KEYWORD': 'trend also reflect free store give away shop work like second hand shop without money without logic exchang understood place thing given transfer one privat owner anoth place peopl bring thing fallen possess sinc longer use'}, {'TEXT': ' On one of his visits to Sacramento he discovered an opportunity in commerce, and so opened a general store on K Street, not far from where Leland Stanford set up shop..', 'LINE': 2106, 'BOOK': 'The Age of Gold - H. W. Brands', 'KEYWORD': 'one visit discov opportun commerc gener store street far set shop'}, {'TEXT': ' Being a ritual passage as a part of a pastoral Herculean landscape, the latter was like the Via Tecta in Pergamon in that it was multi-functional and included market halls and shops (Tilburg, 2007, p.', 'LINE': 390, 'BOOK': 'Architecture and the Body by Kim Sexton', 'KEYWORD': 'ritual passag part pastor landscap latter wa like via wa function includ market hall shop'}]\n"
     ]
    }
   ],
   "source": [
    "tfidf_results, vectorizer, tfidf_matrix = tfidf_search(query)\n",
    "print(\"TF-IDF Search:\", tfidf_results)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "f92f0e31-3f5c-4b79-8bbd-21d09ade4ef7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "TEXT:  Designed by Jaap Bakema (1914–1981), a cluster of low-slung monolithic brick buildings, topped by yellow painted fascias, emerges below in a pastoral scene of meadow and trees (Figure 11.2a). The entrance to Het Dorp turns off the main road into a parking lot, edged by a few small shops, ending vehicular connection to the surrounding neighborhood.\n",
      "LINE: 1781\n",
      "BOOK: Architecture and the Body by Kim Sexton\n",
      "KEYWORD: design cluster low slung monolith brick build top yellow paint fascia pastor scene meadow tree figur entranc het dorp turn main road park lot edg small shop end vehicular connect surround neighborhood\n",
      "\n",
      "TEXT: IN THE BEACH HOUSE The doors open and the heat undoes itself, everyone undoes himself, everyone walks naked. Two of them walk on the table. They are not afraid of God’s displeasure. They will have no truck with the angel who hoots from the fog horn and throws the ocean into the rocks outside.\n",
      "LINE: 263\n",
      "BOOK: Anne Sexton Poems\n",
      "KEYWORD: beach hous door open heat everyon everyon walk nake two walk tabl afraid god displeasur truck angel hoot fog horn throw ocean rock outsid\n",
      "\n",
      "TEXT:  To Cipero Street, Rushworth Avenue, High Street, Carib Street, Coffee Street to Harris Promenade; Cipero Street and Coffee Street. Places whose names carried the last whiff of receded cane estates; Carib Street, curling up a shattered mountain, and High Street, rising from a wharf.\n",
      "LINE: 733\n",
      "BOOK: A Map to the Door of No Return - Dionne Brand\n",
      "KEYWORD: street avenu high street street coffe street promenad street coffe street place whose name carri last whiff cane estat street curl mountain high street rise wharf\n",
      "\n",
      "TEXT:  Then after school his chest bare, his mouth slightly open, his tongue emphasizing his hands beating and burnishing the metal face, brightly, brilliantly copper. My second uncle had no such reserve to beat out.\n",
      "LINE: 577\n",
      "BOOK: A Map to the Door of No Return - Dionne Brand\n",
      "KEYWORD: school chest bare mouth slightli open tongu hand beat burnish metal face brightli brilliantli copper second uncl reserv beat\n",
      "\n",
      "TEXT:  But perhaps they are unperturbed; some of them are veterans. The doors open and we all troop in through the turnstiles and the metal detectors. The corridors and vestibules fill up; there aren’t enough seats in Courtroom No.\n",
      "LINE: 482\n",
      "BOOK: A Map to the Door of No Return - Dionne Brand\n",
      "KEYWORD: perhap unperturb veteran door open troop turnstil metal detector corridor vestibul fill enough seat courtroom\n",
      "\n",
      "Top Keywords:\n",
      "\n",
      "['first' 'know' 'futur' ... 'public' 'flow' 'howev']\n",
      "['futur' 'medium' 'citi' ... 'case' 'commun' 'two']\n",
      "['first' 'even' 'live' ... 'point' 'come' 'histori']\n",
      "['part' 'photograph' 'gener' ... 'even' 'life' 'case']\n",
      "['thing' 'cultur' 'cost' ... 'citi' 'case' 'well']\n",
      "['modern' 'practic' 'public' ... 'institut' 'centuri' 'live']\n",
      "['institut' 'mean' 'data' ... 'part' 'treati' 'relat']\n",
      "['book' 'centuri' 'question' ... 'activ' 'without' 'interest']\n",
      "['nation' 'process' 'part' ... 'becom' 'polici' 'live']\n",
      "['free' 'could' 'origin' ... 'chang' 'even' 'use']\n"
     ]
    }
   ],
   "source": [
    "svd_results, top_terms = svd_search(query)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a3226a1f-165f-48d0-9648-2a79828e61c6",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
