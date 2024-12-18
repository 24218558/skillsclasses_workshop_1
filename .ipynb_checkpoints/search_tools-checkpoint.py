{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "3ac1ce8e-0796-459e-aa12-99704bd23269",
   "metadata": {},
   "outputs": [],
   "source": [
    "import sys\n",
    "import os"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "7039f9e0-72cf-4927-9710-34624bfe3c93",
   "metadata": {},
   "outputs": [],
   "source": [
    "sys.path.append(os.getcwd())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "00d8fa5b-87d4-4551-862b-eefa7df414e7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Simple Search: [{'TEXT': ' Sonny was the only one happy there. His wife and daughters always seemed washed with dread and exhaustion. You would probably go past the small shop owned by Miss Jeanne and think the bottles of dinner mints and sweet plums dull.', 'NR': 38, 'Book ID': 'A Map to the Door of No Return - Dionne Brand', 'Processed Text': 'sonni wa one happi wife daughter alway wash dread exhaust would probabl past small shop miss think bottl dinner mint sweet plum dull'}, {'TEXT': ' Being in the Diaspora braces itself in virtuosity or despair. 9 One has this sense as one observes bodies in the Diaspora, virtuosity or despair, on the brink of both. A body pushing a grocery cart through the city housing at Lawrence and Bathurst in Toronto, her laundry, her shopping all contained there, dressed as if on her way to a party, gold chain around her neck, lipstick — as if moving with all her possessions.', 'NR': 122, 'Book ID': 'A Map to the Door of No Return - Dionne Brand', 'Processed Text': 'brace virtuos despair one ha sens one bodi virtuos despair brink bodi push groceri cart citi hous laundri shop dress way parti gold chain around neck lipstick move possess'}, {'TEXT': ' 3 At seventeen on Raglan Avenue, it wasn’t wine but loneliness that woke me up to reach for Prevert, whose Paroles I had found in an old book shop. “Pierre tell me the truth” hissing through my sleep.', 'NR': 241, 'Book ID': 'A Map to the Door of No Return - Dionne Brand', 'Processed Text': 'seventeen raglan avenu wine loneli woke reach whose parol found old book shop tell truth hiss sleep'}, {'TEXT': ' I know the narrowness of the street; I know the circus I’m walking toward. I know the pace of other pedestrians and I know how long I will have to wait at a coffee shop to be noticed and then to ask for my coffee.', 'NR': 347, 'Book ID': 'A Map to the Door of No Return - Dionne Brand', 'Processed Text': 'know narrow street know circu walk toward know pace pedestrian know long wait coffe shop ask coffe'}, {'TEXT': ' I remember another shebeen — a rum shop, it’s called there — in a village in Dominica. One night some friends and I drive through country darkness, stopped where the car could go no further, and climbed a hill, bumping into tree stumps, arriving at a rum shop.', 'NR': 443, 'Book ID': 'A Map to the Door of No Return - Dionne Brand', 'Processed Text': 'rememb anoth shebeen rum shop villag one night friend drive countri dark stop car could hill bump tree stump rum shop'}]\n",
      "TF-IDF Search: [{'TEXT': 'Early on, we did everything we could to avoid exhibiting work in a white cube and everything it stood for. We showed in shop windows, homes, shopping centers, cafes, gardens. But always, the work became about the space itself, or the context, rather than the ideas we wished to explore.', 'NR': 623, 'Book ID': 'Speculative Everything by Anthony Dunne', 'Processed Text': 'earli everyth could avoid work white cube everyth stood shop window home shop center garden alway work space context rather idea wish explor'}, {'TEXT': ' I remember another shebeen — a rum shop, it’s called there — in a village in Dominica. One night some friends and I drive through country darkness, stopped where the car could go no further, and climbed a hill, bumping into tree stumps, arriving at a rum shop.', 'NR': 443, 'Book ID': 'A Map to the Door of No Return - Dionne Brand', 'Processed Text': 'rememb anoth shebeen rum shop villag one night friend drive countri dark stop car could hill bump tree stump rum shop'}, {'TEXT': ' This trend is also reflected in “free stores” or “give-away shops,” which work like second-hand shops, just without money and without the logic of exchange. These are not to be understood as places where things are “given,” that is, transferred from one private owner to another, but as places where people bring things that have “fallen out of possession,” since they are no longer used.', 'NR': 2568, 'Book ID': 'Society After Money Dialogue', 'Processed Text': 'trend also reflect free store give away shop work like second hand shop without money without logic exchang understood place thing given transfer one privat owner anoth place peopl bring thing fallen possess sinc longer use'}, {'TEXT': ' On one of his visits to Sacramento he discovered an opportunity in commerce, and so opened a general store on K Street, not far from where Leland Stanford set up shop..', 'NR': 2106, 'Book ID': 'The Age of Gold - H. W. Brands', 'Processed Text': 'one visit discov opportun commerc gener store street far set shop'}, {'TEXT': ' Being a ritual passage as a part of a pastoral Herculean landscape, the latter was like the Via Tecta in Pergamon in that it was multi-functional and included market halls and shops (Tilburg, 2007, p.', 'NR': 390, 'Book ID': 'Architecture and the Body by Kim Sexton', 'Processed Text': 'ritual passag part pastor landscap latter wa like via wa function includ market hall shop'}]\n",
      "SVD Search: [{'TEXT': ' Figure 11.1 Van den Broek and Bakema, Het Dorp, Arnhem, Netherlands, 1963–65, aerial perspective view from the southwest (‘Het Dorp: A Village’) Photo: Collection Het Nieuwe Instituut/BROX Figure 11.2 Het Dorp, (a) (above) view of shops from plaza; (b) (below) residents in road among low housing units near the top of the site Photos: author Several things are striking about the village Bakema and the Dutch public built.', 'NR': 1786, 'Book ID': 'Architecture and the Body by Kim Sexton', 'Processed Text': 'figur van den het dorp aerial perspect view southwest het dorp villag photo collect het figur het dorp view shop plaza resid road among low hous unit near top site photo author sever thing strike villag dutch public built'}, {'TEXT': '1 Van den Broek and Bakema, Het Dorp, Arnhem, Netherlands, 1963–65 11.2 Het Dorp, view of shops from plaza; residents in road among low housing units near the top of the site 11.3 Het Dorp, sectional elevations of building phase 4 (‘Het Dorp: A Village’); Jachtweg (Hunt Way), the first completed street/phase, with brick floor 11.', 'NR': 34, 'Book ID': 'Architecture and the Body by Kim Sexton', 'Processed Text': 'van den het dorp het dorp view shop plaza resid road among low hous unit near top site het dorp section elev build phase het dorp villag hunt way first street phase brick floor'}, {'TEXT': 'P. Bijleveld, Het Dorp’s director from 1966 to 1978, compared to integrating black and white families in U.S. residential neighborhoods (‘Het Dorp: A Village,’ 1971, p. 57). The commercial zone depended on customers from both Het Dorp and outside, thereby enabling a limited intermingling of disabled and able-bodied populations (‘Het Dorp: A Village,’ 1971, pp.', 'NR': 1831, 'Book ID': 'Architecture and the Body by Kim Sexton', 'Processed Text': 'het dorp director black white famili residenti neighborhood het dorp villag commerci zone custom het dorp outsid therebi limit disabl abl bodi popul het dorp villag'}, {'TEXT': ' Het Dorp. Architectural Review, 149, 227–36. Het Dorp van de grond. (1966, June 14). [Television broadcast]. The Netherlands: AVRO. Het Dorp Kwam Er. (1967, November 27). [Television broadcast]. The Netherlands: AVRO.', 'NR': 1948, 'Book ID': 'Architecture and the Body by Kim Sexton', 'Processed Text': 'het dorp architectur review het dorp van june televis broadcast het dorp televis broadcast'}, {'TEXT': ' The Netherlands: AVRO. Het Dorp Na 7.5 Jaar Officiel Geopend. (1970, May 30). [Television broadcast]. The Netherlands: AVRO. Het Dorp: A Village for the Handicapped in Arnhem, Netherlands. (1971). Plan: maandblad voor ontwerp en omgeving, 4, 54–70.', 'NR': 2206, 'Book ID': 'Architecture and the Body by Kim Sexton', 'Processed Text': 'het dorp may televis broadcast het dorp villag handicap plan'}]\n"
     ]
    }
   ],
   "source": [
    "# Import necessary libraries\n",
    "from search_word import simple_search, tfidf_search, svd_search"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "b4c1aaa6-4aad-4875-9637-cc3f182302f3",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Execute search with user input\n",
    "def search_database(query, method='simple', num_results=5):\n",
    "    if method == 'simple':\n",
    "        return simple_search(query, num_results)\n",
    "    elif method == 'tfidf':\n",
    "        return tfidf_search(query, num_results)\n",
    "    elif method == 'svd':\n",
    "        return svd_search(query, num_results)\n",
    "    else:\n",
    "        print(\"Invalid search method.\")\n",
    "        return []"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "466cbec1-6037-4f3e-bfb2-dd28bc15be29",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your search query:  shop\n",
      "Enter search method (simple, tfidf, svd):  simple\n",
      "Enter number of results:  5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Book ID: A Map to the Door of No Return - Dionne Brand, Paragraph Number: 38\n",
      "Full Text:  Sonny was the only one happy there. His wife and daughters always seemed washed with dread and exhaustion. You would probably go past the small shop owned by Miss Jeanne and think the bottles of dinner mints and sweet plums dull.\n",
      "Processed Text: sonni wa one happi wife daughter alway wash dread exhaust would probabl past small shop miss think bottl dinner mint sweet plum dull\n",
      "\n",
      "Book ID: A Map to the Door of No Return - Dionne Brand, Paragraph Number: 122\n",
      "Full Text:  Being in the Diaspora braces itself in virtuosity or despair. 9 One has this sense as one observes bodies in the Diaspora, virtuosity or despair, on the brink of both. A body pushing a grocery cart through the city housing at Lawrence and Bathurst in Toronto, her laundry, her shopping all contained there, dressed as if on her way to a party, gold chain around her neck, lipstick — as if moving with all her possessions.\n",
      "Processed Text: brace virtuos despair one ha sens one bodi virtuos despair brink bodi push groceri cart citi hous laundri shop dress way parti gold chain around neck lipstick move possess\n",
      "\n",
      "Book ID: A Map to the Door of No Return - Dionne Brand, Paragraph Number: 241\n",
      "Full Text:  3 At seventeen on Raglan Avenue, it wasn’t wine but loneliness that woke me up to reach for Prevert, whose Paroles I had found in an old book shop. “Pierre tell me the truth” hissing through my sleep.\n",
      "Processed Text: seventeen raglan avenu wine loneli woke reach whose parol found old book shop tell truth hiss sleep\n",
      "\n",
      "Book ID: A Map to the Door of No Return - Dionne Brand, Paragraph Number: 347\n",
      "Full Text:  I know the narrowness of the street; I know the circus I’m walking toward. I know the pace of other pedestrians and I know how long I will have to wait at a coffee shop to be noticed and then to ask for my coffee.\n",
      "Processed Text: know narrow street know circu walk toward know pace pedestrian know long wait coffe shop ask coffe\n",
      "\n",
      "Book ID: A Map to the Door of No Return - Dionne Brand, Paragraph Number: 443\n",
      "Full Text:  I remember another shebeen — a rum shop, it’s called there — in a village in Dominica. One night some friends and I drive through country darkness, stopped where the car could go no further, and climbed a hill, bumping into tree stumps, arriving at a rum shop.\n",
      "Processed Text: rememb anoth shebeen rum shop villag one night friend drive countri dark stop car could hill bump tree stump rum shop\n",
      "\n"
     ]
    }
   ],
   "source": [
    "#Testing\n",
    "query = input(\"Enter your search query: \")\n",
    "method = input(\"Enter search method (simple, tfidf, svd): \")\n",
    "num_results = int(input(\"Enter number of results: \"))\n",
    "results = search_database(query, method, num_results)\n",
    "for result in results:\n",
    "    print(f\"Book ID: {result['Book ID']}, Paragraph Number: {result['NR']}\\nFull Text: {result['TEXT']}\\nProcessed Text: {result['Processed Text']}\\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f0496940-27b6-4367-9c15-2e1177b2fb39",
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
