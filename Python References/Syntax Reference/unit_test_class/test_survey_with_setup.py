import unittest
from survey import AnonymouseSurvery

class TestAnonymousSurvey(unittest.TestCase):
  def setUp(self):
    question = "What language did you learn to speak first?"
    self.my_survey = AnonymouseSurvery(question)
    self.responses = ['English', 'German', 'Spanish']

  def test_store_single_response(self):
    self.my_survey.store_response(self.responses[0])
    self.assertIn('English', self.my_survey.responses)

  def test_store_three_responses(self):
    responses = self.responses

    for response in responses:
      if response == 'German':
        response = 'French'
      self.my_survey.store_response(response)
    
    for response in responses:
      self.assertIn(response, self.my_survey.responses)

if __name__ == '__main__':
  unittest.main()