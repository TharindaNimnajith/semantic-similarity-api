from enum import Enum


class SummarizationSuggestions(Enum):
    SPELLING = 'Confused by English spelling? That’s totally understandable! Plenty of native speakers find it ' \
               'confusing, too. Don’t worry, though. It is possible to improve your English spelling. Please read ' \
               'this excellent article at https://www.fluentu.com/blog/english/how-to-improve-english-spelling/ as a ' \
               'start!'
    GRAMMAR = 'Grammar is a subject that stresses many students out, as it can be quite confusing and complicated. ' \
              'However, correct grammar is important for your writing and success. Please read this excellent ' \
              'article at https://www.varsitytutors.com/blog/7+tips+to+improve+your+grammar+skills as a start!'
    RELEVANCY = 'It is very important to first read the given paragraph carefully and understand the context. Only ' \
                'then you can successfully summarize the provided paragraph. Please be more cautious about the ' \
                'relevancy of your answer next time.'
    OBJECTIVITY = 'In academic English writing, objectivity is very important. If you are writing objectively, you ' \
                  'must remain as neutral as possible through the use of facts, statistics, and research. To keep ' \
                  'your writing objective, follow these 3 tips: Be specific instead of vague or general, Avoid using ' \
                  'first person to keep it more professional and less about you, Try not to over exaggerate your ' \
                  'writing.'
    GOOD = 'Congratulations on your great score! Your hard work and dedication surely impacted your result. Very ' \
           'well done!'
    COPIED = 'Your answer needs to be in your own words. Rewriting the original paragraph is not summarizing. ' \
             'Please refer the introduction again to understand the art of text summarization.'
    INSUFFICIENT = 'Come on, don\'t be lazy. You need to write more to improve your writing skills. Please try to ' \
                   'write more and get closer to the word limit next time.'
