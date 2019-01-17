import sys
import argparse
from polyglot.detect import Detector
parser=argparse.ArgumentParser()
parser.add_argument('--text','-t', help='Enter the sentence you want to detect')

def Language_id(text):

    for language in Detector(text).languages:
        if language.name == 'un':
            pass
        else:
            print('Language:'+language.name+'     '+'Confidence Ratio'+' '+str(language.confidence))
if __name__ == '__main__':
   args = parser.parse_args()
   if args.text == None:
       print('Please enter a sentence. Exiting.')
       sys.exit(0)
   print(args.text)
   Language_id(args.text)
