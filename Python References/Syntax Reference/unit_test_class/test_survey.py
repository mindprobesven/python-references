import unittest
from survey import AnonymouseSurvery

class TestAnonymousSurvey(unittest.TestCase):
  def test_store_single_response(self):
    question = "What language did you learn to speak first?"
    my_survey = AnonymouseSurvery(question)
    my_survey.store_response('English')
    self.assertIn('English', my_survey.responses)

  def test_store_three_responses(self):
    question = "What language did you learn to speak first?"
    my_survey = AnonymouseSurvery(question)
    responses = ['English', 'German', 'Spanish']
    for response in responses:
      if response == 'German':
        response = 'French'
      my_survey.store_response(response)
    
    for response in responses:
      self.assertIn(response, my_survey.responses)

if __name__ == '__main__':
  unittest.main()